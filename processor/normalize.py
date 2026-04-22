import os
import pandas as pd
from pathlib import Path

from processor.parsers.syslog_parser import parse_syslog
from processor.parsers.authlog_parser import parse_authlog
from processor.parsers.windows_evtx_parser import parse_evtx

THIS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = THIS_DIR.parent
RAW_DIR = PROJECT_ROOT.joinpath("output", "raw_logs")

EXT_MAP = {
    "syslog": parse_syslog,
    "auth.log": parse_authlog,
    "evtx": parse_evtx
}

def normalize_all():
    df_list = []

    if not RAW_DIR.exists():
        print(f"[-] Raw log directory not found: {RAW_DIR}")
        return pd.DataFrame()

    for host_folder in os.listdir(RAW_DIR):
        hf = os.path.join(RAW_DIR, host_folder)
        host = host_folder.replace("_", ".")

        for log_file in os.listdir(hf):
            file_path = os.path.join(hf, log_file)

            for key, parser_fn in EXT_MAP.items():
                if key in log_file:
                    try:
                        parsed_df = parser_fn(file_path, host)
                        if not parsed_df.empty:
                            df_list.append(parsed_df)
                    except Exception as e:
                        print(f"[-] parser failed for {file_path}: {e}")

    if not df_list:
        return pd.DataFrame()

    normalized_df = pd.concat(df_list, ignore_index=True)
    normalized_df["timestamp"] = pd.to_datetime(normalized_df["timestamp"], utc=True)
    normalized_df = normalized_df.sort_values("timestamp")
    normalized_df.reset_index(drop=True, inplace=True)
    return normalized_df

if __name__ == "__main__":
    df_out = normalize_all()
    out_path = PROJECT_ROOT.joinpath("output", "normalized_timeline.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(out_path, index=False)
    print("[+] Normalization completed")
