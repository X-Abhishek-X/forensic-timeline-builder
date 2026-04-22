from pathlib import Path
from flask import Flask, render_template
import pandas as pd

THIS_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(THIS_DIR / "templates"),
    static_folder=str(THIS_DIR / "static")
)

@app.route("/")
def timeline():
    csv_path = THIS_DIR.parent.joinpath("output", "final_timeline.csv")
    if not csv_path.exists():
        # graceful fallback so the page doesn't crash in dev
        df_html = "<p><em>No timeline generated yet. Run the pipeline to create output/final_timeline.csv</em></p>"
        return render_template("timeline.html", tables=[df_html])
    df = pd.read_csv(str(csv_path))
    return render_template("timeline.html", tables=[df.to_html(classes='table', index=False)])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
