from analysis import calculate_win_rate
from matches import get_matches, get_player_participants
from player import get_riot_id, get_puuid
    
def main():

    game_name, tag_line = get_riot_id()

    puuid = get_puuid(game_name, tag_line)

    matches = get_matches(puuid)

    participant_list = get_player_participants(matches, puuid)

    winrate = calculate_win_rate(participant_list)

    if winrate == None:
        print("No recent matches found.\n")
    else:
        print(f"Winrate over last 10 games is {winrate}%\n")
        


if __name__ == "__main__":
    main()

