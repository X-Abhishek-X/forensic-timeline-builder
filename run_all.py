import subprocess
from processor.normalize import normalize_all
from processor.timeline_builder import build_timeline_csv, build_html, build_pdf

print("[1] Collecting logs from hosts")
subprocess.call(["python", "collector/collect_logs.py"])

print("[2] Normalizing logs")
normalized_df = normalize_all()

if normalized_df.empty:
    print("[-] No events found after normalization. Exiting.")
else:
    print("[3] Building timeline exports")
    build_timeline_csv(normalized_df)
    build_html(normalized_df)
    build_pdf(normalized_df)
    print("[DONE] All tasks complete")
