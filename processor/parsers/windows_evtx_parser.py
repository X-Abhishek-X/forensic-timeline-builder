import pandas as pd
from evtx import PyEvtxParser
from dateutil import parser

def parse_evtx(file_path, host):
    events = []
    evtx_parser = PyEvtxParser(file_path)
    
    for record in evtx_parser.records():
        try:
            # The record is a dictionary with keys: 'event_record_id', 'timestamp', 'data'
            ts = parser.parse(record['timestamp'])
            events.append({
                "timestamp": ts,
                "host": host,
                "message": f"Event ID: {record['event_record_id']}",
                "raw": record['data']  # This contains the XML data
            })
        except Exception as e:
            # Silently skip records that can't be parsed
            continue

    evtx_df = pd.DataFrame(events)
    return evtx_df
