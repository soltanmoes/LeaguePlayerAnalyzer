from analysis import calculate_win_rate, calculate_overall_kda
from matches import get_matches, fetch_match_ids, get_player_in_participants
from player import get_riot_id, get_puuid
from database import create_database, save_matches, get_stored_match_ids


def get_new_match_ids(api_match_ids, stored_match_ids):

    return list((set(api_match_ids)&set(stored_match_ids))^set(api_match_ids))


def main():

    game_name, tag_line = get_riot_id()

    puuid = get_puuid(game_name, tag_line)
    
    riot_id = game_name + tag_line

    create_database()

    api_match_ids = fetch_match_ids(puuid)
    print(f"{len(api_match_ids)} matches found")

    stored_match_ids = get_stored_match_ids(puuid)
    print(f"{len(stored_match_ids)} matches already stored")

    new_match_ids = get_new_match_ids(api_match_ids, stored_match_ids)
    save_matches(puuid, riot_id, new_match_ids)
    print(f"{len(new_match_ids)} new matches downloaded\n")


    print("==== PLAYER ANALYSIS ====")
    stored_match_ids = get_stored_match_ids(puuid)
    matches = get_matches(stored_match_ids)
    participant_list = get_player_in_participants(matches, puuid)
    
    winrate = calculate_win_rate(participant_list)
    overall_kda = calculate_overall_kda(participant_list)

    print(f"Total matches analyzed: {len(stored_match_ids)}")
    print(f"Winrate: {winrate:.1f}%")
    print(f"Overall KDA: {overall_kda:.2f}")




    


if __name__ == "__main__":
    main()

