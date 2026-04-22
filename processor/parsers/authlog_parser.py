import pandas as pd
from dateutil import parser

def parse_authlog(file_path, host):
    rows = []
    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            try:
                timestamp = parser.parse(" ".join(line.split()[:3]))
                msg = " ".join(line.split()[4:])
                rows.append({
                    "timestamp": timestamp,
                    "host": host,
                    "message": msg,
                    "raw": line.strip()
                })
            except Exception:
                continue

    auth_df = pd.DataFrame(rows)
    return auth_df
