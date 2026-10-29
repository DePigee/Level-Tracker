def remove_duplicates(players: list) -> list:
    player_ids = set()
    unique_players = []
    
    for player in players:
        if(player["player_id"] not in player_ids):
            player_ids.add(player["player_id"])
            unique_players.append(player)
    return unique_players


def total_xp(xp_list: list) -> int:
    total = 0

    for xp in xp_list:
        try:
              converted_xp = int(xp)
              total += converted_xp 
        except ValueError:
            continue
    return total