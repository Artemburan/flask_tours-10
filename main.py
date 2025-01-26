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
    tours = {tour_id: tour for tour_id, tour in data.tours.items() if tour["departure"] == dep_eng}
    return render_template("departure.html", tours=tours, dep_eng=dep_eng)


@app.get("/tour/<int:tour_id>")
def get_tour(tour_id):
    tour=data.tours.get(tour_id)
    return render_template("tour.html", tour_id=tour_id, tour=tour)

@app.get("/buy_tour/<int:tour_id>")
def buy_tour(tour_id):
    tour = data.tours.get(tour_id)
    return f"Ви успішно купили тур '{tour['title']}'. Дякуюємо"


if __name__ == "__main__":
    app.run(debug=True)
