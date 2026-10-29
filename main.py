from leveltracker import remove_duplicates, total_xp, get_level, print_report

def main():
    players = [
    {"player_id": "P1", "name": "Zara", "xp": [120, 80, 150]},
    {"player_id": "P2", "name": "Milo", "xp": [200, "lots", 90]},
    {"player_id": "P3", "name": "Juno", "xp": [40, 30]},
    {"player_id": "P1", "name": "Zara", "xp": [120, 80, 150]},  # Duplicate
    {"player_id": "P4", "name": "Kai", "xp": []},               # No XP
    {"player_id": "P5", "name": "Rhea", "xp": [500, 450, 300]},
    ]

    unique_players = remove_duplicates(players)
    player_xp = total_xp(unique_players[0]["xp"])
    player_level = get_level(player_xp)
    print_report(unique_players)
    
    
    
    
main()