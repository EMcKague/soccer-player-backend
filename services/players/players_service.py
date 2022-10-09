from typing import List
from services.players.players import Player


class PlayerService:
    @classmethod
    def get_players(cls) -> List[Player]:
        players = Player.index()
        return [player.dict() for player in players]