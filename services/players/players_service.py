from typing import List
from services.players.players import Player


class PlayerService:
    @classmethod
    def get_players(cls, args) -> List[Player]:
        players = Player.index()
        if "sort" in args and "column" in args:
            sort = args["sort"]
            column = args["column"]
            reverse = False if sort == "asc" else True
            players.sort(key=lambda x: getattr(x, column), reverse=reverse)
        return [player.dict() for player in players]

    @classmethod
    def get_player_by_name(cls, name: str) -> Player:
        players = Player.index()
        players = [player for player in players if player.name == name]
        return players[0].dict()
