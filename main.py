import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station_id>/<date>")
def about(station_id, date):
    fname = f"data_small/TG_STAID{station_id.zfill(6)}.txt"
    df = pd.read_csv(fname, skiprows=20, parse_dates=["    DATE"])
    temp = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10
    return {
        "station_id": station_id,
        "date": date,
        "temperature": temp
    }


if __name__ == "__main__":
    app.run(debug=True)