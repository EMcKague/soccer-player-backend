# from flask import Flask

# app = Flask(__name__)

# #Memeber API route 
# @app.route("/")
# def memebers():
#     return {
#         "members": ["Member1", "Member2", "Member3"]
    # }

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from flask_cors import CORS, cross_origin
from json_api import JSONAPIData, JSONAPIList
from services.players.players import Player

from services.players.players_service import PlayerService


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# test
# @app.route("/players")
# @cross_origin()
# def hello_world():
#     return {
        
#     }

@app.route("/members")
@cross_origin()
def memebers():
    return {
        "members": ["Member1", "Member2", "Member3"]
    }
# ---- 
# end test
# ----

# application
@app.route("/players")
@cross_origin()
def players():
    return PlayerService.get_players()
    # return JSONAPIList[Player](data=[_player_transform(player) for player in players])

# def _player_transform(player: Player):
#     return JSONAPIData[Player](id=player.id, attributes=player, type='player')

# @app.route("/players/<name>")
# @cross_origin()
# def get_player_by_name(name: str):
#     return name

# @app.route("/countries")
# @cross_origin()
# def get_countries():
#     return 

# @app.route("/clubs")
# @cross_origin()
# def get_clubs():
#     return

# @app.route("/attributes")
# @cross_origin()
# def get_attributes():
#     return

if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")