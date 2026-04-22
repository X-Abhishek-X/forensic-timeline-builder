import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project root directory (parent of processor directory)
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

def build_timeline_csv(events_df: pd.DataFrame):
    out = OUTPUT_DIR / "final_timeline.csv"
    events_df.to_csv(out, index=False)
    print(f"[+] CSV exported -> {out}")

def build_pdf(events_df: pd.DataFrame):
    # placeholder simple PDF generation using a saved figure; replace with better layout if needed
    plt.figure(figsize=(8, 10))
    plt.plot(events_df.index, events_df.index)
    plt.title("Timeline (Index Only Placeholder)")
    pdf_out = OUTPUT_DIR / "timeline.pdf"
    plt.savefig(pdf_out)
    plt.close()
    print(f"[+] PDF exported -> {pdf_out}")

def build_html(events_df: pd.DataFrame):
    html_out = OUTPUT_DIR / "timeline.html"
    html = events_df.to_html(index=False)
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[+] HTML exported -> {html_out}")
