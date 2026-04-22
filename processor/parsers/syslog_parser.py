import pandas as pd
from dateutil import parser

def parse_syslog(file_path, host):
    events = []
    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            try:
                timestamp = parser.parse(" ".join(line.split()[:3]))
                msg = " ".join(line.split()[4:])
                events.append({
                    "timestamp": timestamp,
                    "message": msg,
                    "host": host,
                    "raw": line.strip()
                })
            except Exception:
                continue

    events_df = pd.DataFrame(events)
    return events_df
