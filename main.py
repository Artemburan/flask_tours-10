from flask import Flask, render_template, redirect, url_for, request

from data import data


app = Flask(__name__)


@app.context_processor
def global_data():
    return dict(
        title = data.title,
        departures = data.departures
    )



@app.get("/")
def index():
    return render_template("index.html", tours=data.tours)


@app.get("/departure/<dep_eng>/")
def departure(dep_eng):
    return render_template("departure.html")


@app.get("/tour/")
def tour():
    return render_template("tour.html")


if __name__ == "__main__":
    app.run(debug=True)
