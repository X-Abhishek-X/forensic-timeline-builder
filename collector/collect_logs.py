# collector/collect_logs.py
"""
collector/collect_logs.py
Robust SSH/SFTP log collector that writes into `output/raw_logs/<host>/`.
Also supports a `local_path` entry per host for testing without SSH.
Local paths are resolved by trying several sensible locations so the collector
works whether you specify paths relative to the collector/ folder or the project root.
"""

import json
import shutil
from pathlib import Path
import paramiko
import sys

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parent.parent
SSH_HOSTS_PATH = THIS_FILE.parent.joinpath("ssh_hosts.json")
OUTPUT_DIR = PROJECT_ROOT.joinpath("output", "raw_logs")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def fetch_via_ssh(host: str, user: str, password: str, paths: list, timeout: int = 10):
    host_dir = OUTPUT_DIR.joinpath(host.replace(".", "_"))
    host_dir.mkdir(parents=True, exist_ok=True)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, username=user, password=password, timeout=timeout)
    except Exception as e:
        print(f"[-] SSH connect failed for {host}: {e}")
        return

    try:
        sftp = ssh.open_sftp()
    except Exception as e:
        print(f"[-] Could not open SFTP for {host}: {e}")
        ssh.close()
        return

    for p in paths:
        try:
            destination = host_dir.joinpath(Path(p).name)
            sftp.get(p, str(destination))
            print(f"[+] Downloaded {p} -> {destination} from {host}")
        except Exception as e:
            print(f"[-] Could not download {p} from {host}: {e}")

    try:
        sftp.close()
    except Exception:
        pass
    ssh.close()


def fetch_local(host: str, local_paths: list):
    """
    Copy files from local_paths into output dir for given host.
    For each entry we try several candidate locations:
      1. the path as given (if absolute)
      2. collector/<given>  (resolve relative to collector folder)
      3. project_root/<given> (resolve relative to project root)
      4. if given starts with 'collector/', also try collector/<given-without-leading-collector/>
    This allows the ssh_hosts.json to contain either 'sample_local_logs/...' or
    'collector/sample_local_logs/...' and still work.
    """
    host_dir = OUTPUT_DIR.joinpath(host.replace(".", "_"))
    host_dir.mkdir(parents=True, exist_ok=True)

    for src in local_paths:
        provided = Path(src)
        candidates = []

        # 1) absolute path as provided
        if provided.is_absolute():
            candidates.append(provided)

        # 2) path resolved relative to the collector folder
        candidates.append(THIS_FILE.parent.joinpath(src).resolve())

        # 3) path resolved relative to the project root
        candidates.append(PROJECT_ROOT.joinpath(src).resolve())

        # 4) if the user provided "collector/..." try stripping the leading "collector/"
        if src.startswith("collector" + str(Path("/")) ) or src.startswith("collector/"):
            stripped = src.split("/", 1)[1] if "/" in src else src
            candidates.append(THIS_FILE.parent.joinpath(stripped).resolve())

        # find the first candidate that exists
        found = None
        for p in candidates:
            if p.exists():
                found = p
                break

        if not found:
            # helpful debug output: show all candidates we tried
            cand_text = ", ".join(str(p) for p in candidates)
            print(f"[-] Local source not found for '{src}'. Tried: {cand_text}")
            continue

        try:
            if found.is_file():
                dest = host_dir.joinpath(found.name)
                shutil.copy2(found, dest)
                print(f"[+] Copied local file {found} -> {dest}")
            elif found.is_dir():
                for child in found.iterdir():
                    if child.is_file():
                        dest = host_dir.joinpath(child.name)
                        shutil.copy2(child, dest)
                        print(f"[+] Copied local file {child} -> {dest}")
        except Exception as e:
            print(f"[-] Failed to copy {found}: {e}")


def load_hosts(json_path: Path):
    if not json_path.exists():
        print(f"[-] Host file not found: {json_path}")
        return []
    try:
        return json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[-] Failed to read {json_path}: {e}")
        return []


def main():
    hosts = load_hosts(SSH_HOSTS_PATH)
    if not hosts:
        print("[-] No hosts found in ssh_hosts.json, exiting.")
        return

    for entry in hosts:
        host = entry.get("host")
        if not host:
            print("[-] Host entry missing 'host' field, skipping:", entry)
            continue

        if "local_path" in entry:
            local_paths = entry.get("local_path", [])
            fetch_local(host, local_paths)
            continue

        user = entry.get("user")
        password = entry.get("password")
        paths = entry.get("paths", [])

        if not (user and password and paths):
            print(f"[-] Host entry for {host} missing user/password/paths; skipping.")
            continue

        fetch_via_ssh(host, user, password, paths)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        sys.exit(1)
