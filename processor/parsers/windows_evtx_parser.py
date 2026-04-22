import pandas as pd
from evtx import PyEvtxParser
from dateutil import parser

def parse_evtx(file_path, host):
    events = []
    for record in PyEvtxParser(file_path).records():
        try:
            ts = parser.parse(record.timestamp())
            events.append({
                "timestamp": ts,
                "host": host,
                "message": record.message(),
                "raw": record.xml()
            })
        except Exception:
            continue

    evtx_df = pd.DataFrame(events)
    return evtx_df
