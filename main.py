import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

station_data = pd.read_csv("data_small/stations.txt", skiprows=17)
station_data = station_data[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    stations = station_data.to_html()
    return render_template("home.html", data=stations)


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


@app.route("/api/v1/<station_id>/")
def all_data(station_id):
    fname = f"data_small/TG_STAID{station_id.zfill(6)}.txt"
    df = pd.read_csv(fname, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station_id>/<year>/")
def yearly(station_id, year):
    fname = f"data_small/TG_STAID{station_id.zfill(6)}.txt"
    df = pd.read_csv(fname, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result



if __name__ == "__main__":
    app.run(debug=True)