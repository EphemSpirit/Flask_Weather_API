import pandas
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station_id>/<date>")
def about(station_id, date):
    # df = pandas.read_csv("")
    # temp = df.station
    temp = 23
    return {
        "station_id": station_id,
        "date": date,
        "temperature": temp
    }


if __name__ == "__main__":
    app.run(debug=True)