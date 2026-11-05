from analysis import calculate_win_rate
from matches import get_matches, fetch_match_ids, get_player_participants
from player import get_riot_id, get_puuid
from database import create_database, save_matches, get_stored_match_ids


def get_new_match_ids(api_match_ids, stored_match_ids):

    return list((set(api_match_ids)&set(stored_match_ids))^set(api_match_ids))




def main():

    game_name, tag_line = get_riot_id()

    puuid = get_puuid(game_name, tag_line)

    # matches = get_matches(puuid)

    # participant_list = get_player_participants(matches, puuid)

    # winrate = calculate_win_rate(participant_list)

    # if winrate == None:
    #     print("No recent matches found.\n")
    # else:
    #     print(f"Winrate over last 10 games is {winrate}%\n")
    
    riot_id = game_name + tag_line

    create_database()

    api_match_ids = fetch_match_ids(puuid)

    # save_matches(puuid, riot_id, match_ids)

    stored_match_ids = get_stored_match_ids(puuid)

    new_match_ids = get_new_match_ids(api_match_ids, stored_match_ids)

    print(f"api_matches: {api_match_ids}")
    
    print(f"stored_matches: {stored_match_ids}")
    
    print(f"unsaved_matches: {new_match_ids}")



if __name__ == "__main__":
    main()

