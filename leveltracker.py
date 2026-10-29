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

def get_level(xp: int) -> str:    
    if(xp >= 1000):
        return "Master"
    elif(xp >= 500):
        return "Expert"
    elif(xp >= 200):
        return "Skilled"
    elif(xp >= 1):
        return "Beginner"
    else:
        return "Unranked"

"""

4. print_report(players)
Loops through the cleaned list.
Calls total_xp and get_level for each player.
Prints the table below.

"""
def print_report(players: list) -> None:

    print("=" * 30)
    print("PLAYER LEVEL REPORT")
    print("=" * 30)
    print(f"{'ID':<6}{'NAME':<9}{'XP':<7}LEVEL")
    print("-" * 30)

    for player in players:
        player_xp = total_xp(player["xp"])
        player_level = get_level(player_xp)
        print(f"{player['player_id']:<6}{player['name']:<9}{player_xp:<7}{player_level}")

    print("-" * 30)
    print(f"Total Players: {len(players)}")
    print("=" * 30)





