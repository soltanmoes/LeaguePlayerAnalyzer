from analysis import calculate_win_rate, calculate_overall_kda
from matches import get_matches, fetch_match_ids, get_player_in_participants
from player import get_riot_id, get_puuid
from database import create_database, save_matches, get_stored_match_ids, save_participants, get_stored_participants
import json


def get_new_match_ids(api_match_ids, stored_match_ids):

    return list((set(api_match_ids)&set(stored_match_ids))^set(api_match_ids))


def add_participants_to_table(puuid, matches):

    participant_list = get_player_in_participants(puuid, matches)

    for match in matches:

        match_id = match["metadata"]["matchId"]

        for participant in participant_list:

            participant_json = json.dumps(participant, indent=4)
            save_participants(puuid, match_id, participant_json)


def main():

    game_name, tag_line = get_riot_id()
    riot_id = game_name + tag_line
    puuid = get_puuid(game_name, tag_line) # asks for riotId and extracts puuid

    create_database() # creates table if it doesn't already exist

    api_match_ids = fetch_match_ids(puuid)
    print(f"{len(api_match_ids)} matches found")

    stored_match_ids = get_stored_match_ids(puuid)
    print(f"{len(stored_match_ids)} matches already stored")

    new_match_ids = get_new_match_ids(api_match_ids, stored_match_ids)
    save_matches(puuid, riot_id, new_match_ids)
    
    stored_match_ids = get_stored_match_ids(puuid)
    matches = get_matches(stored_match_ids)

    add_participants_to_table(puuid, matches)
    participants_table = get_stored_participants(puuid)
    
    print(f"{len(new_match_ids)} new matches downloaded\n")

    print(participants_table)
    
    print("==== PLAYER ANALYSIS ====")
    # winrate = calculate_win_rate(participant_list)
    # overall_kda = calculate_overall_kda(participant_list)

    # print(f"Total matches analyzed: {len(stored_match_ids)}")
    # print(f"Winrate: {winrate:.1f}%")
    # print(f"Overall KDA: {overall_kda:.2f}")




    


if __name__ == "__main__":
    main()

