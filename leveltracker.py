def remove_duplicates(players: list):
    player_ids = set()
    unique_players = []
    
    for player in players:
        if(player["player_id"] not in player_ids):
            player_ids.add(player["player_id"])
            unique_players.append(player)
    return unique_players


