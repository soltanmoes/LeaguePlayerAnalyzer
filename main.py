from analysis import calculate_win_rate, calculate_overall_kda
from matches import get_matches, fetch_match_ids
from player import get_riot_id, get_puuid
from database import *
from sync import add_participants_to_table

def get_new_match_ids(api_match_ids, stored_match_ids):

    return list((set(api_match_ids)&set(stored_match_ids))^set(api_match_ids))

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

    matches = get_matches(new_match_ids)
    add_participants_to_table(puuid, matches)

    stored_match_ids = get_stored_match_ids(puuid)
    
    print(f"{len(new_match_ids)} new matches downloaded\n")

    print("==== PLAYER ANALYSIS ====")
    
    for match_id in stored_match_ids:

        champion = get_player_champ(puuid, match_id)
        kills = get_player_kills(puuid, match_id)
        assists = get_player_assists(puuid, match_id)
        deaths = get_player_deaths(puuid, match_id)
        print(f"Champion: {champion} Kills: {kills} Assists: {assists} Deaths: {deaths}")


    
    # winrate = calculate_win_rate(participant_list)
    # overall_kda = calculate_overall_kda(participant_list)

    # print(f"Total matches analyzed: {len(stored_match_ids)}")
    # print(f"Winrate: {winrate:.1f}%")
    # print(f"Overall KDA: {overall_kda:.2f}")




    


if __name__ == "__main__":
    main()

