from flask import Flask, request
from flask_cors import CORS, cross_origin
from services.clubs.clubs import Clubs
from services.countries.countries import Countries
from services.players.players import Player

from services.players.players_service import PlayerService


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/players")
@cross_origin()
def players():
    return PlayerService.get_players(args=request.args)


@app.route("/players/<name>")
@cross_origin()
def get_player_by_name(name: str):
    return PlayerService.get_player_by_name(name=name)


@app.route("/countries")
@cross_origin()
def get_countries():
    return Countries.countries_list


@app.route("/clubs")
@cross_origin()
def get_clubs():
    return Clubs.club_list


@app.route("/attributes")
@cross_origin()
def get_attributes():
    return Player.schema_json()


if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")
