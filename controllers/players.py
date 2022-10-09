def get_players():
    players = PlayerService.get_players()
    return JSONAPIList[Player](data=[transform(player)])