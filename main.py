from analysis import calculate_win_rate, calculate_overall_kda, group_by_champion
from matches import get_matches, fetch_match_ids
from player import get_riot_id, get_puuid
from database import *
from sync import add_participants_to_table
import json

def get_new_match_ids(api_match_ids, stored_match_ids):

    return list((set(api_match_ids)&set(stored_match_ids))^set(api_match_ids))

def main():

    # drop_all_tables()

    game_name, tag_line = get_riot_id()
    riot_id = game_name + tag_line
    puuid = get_puuid(game_name, tag_line) # asks for riotId and extracts puuid

    create_database() # creates table if it doesn't already exist

    api_match_ids = fetch_match_ids(puuid)
    print(f"{len(api_match_ids)} matches found") # fetches recent games using riot api

    participant_list = get_stored_participants(puuid) 
    print(f"{len(participant_list)} matches already stored")

    stored_match_ids = get_stored_match_ids(puuid) # returns how many match ids are stored in database
    new_match_ids = get_new_match_ids(api_match_ids, stored_match_ids) # using function to check which matches are not stored in database
    save_match_ids(puuid, riot_id, new_match_ids) # only stores those match_ids

    matches = get_matches(new_match_ids) # only gets the match information from non-stored matches
    add_participants_to_table(puuid, matches) # adds those matches to participants table
    participant_list = get_stored_participants(puuid)

    print(f"{len(participant_list)} new matches downloaded\n")

    print("==== PLAYER ANALYSIS ====")


    winrate = calculate_win_rate(participant_list)
    overall_kda = calculate_overall_kda(participant_list)

    stored_match_ids = get_stored_match_ids(puuid) # reassigns correct amount of stored match ids
    print(f"Total matches analyzed: {len(stored_match_ids)}")
    print(f"Winrate: {winrate:.1f}%")
    print(f"Overall KDA: {overall_kda:.2f}")

    grouped_champions = group_by_champion(participant_list)
    print(f"\nChampion performance:")

    #for key in grouped_champions[index]:
        #print(grouped_champions[index][key])

    for key, value in grouped_champions.items():
        winrate = calculate_win_rate(value)
        overall_kda = calculate_overall_kda(value)
        games_count = str(len(value))

        wr_text = f"{winrate:.1f}% WR"
        print(f"{key:10s} | {games_count:5s} games | {wr_text:10s} | {overall_kda:.2f} KDA")


    print("\nMatch history (last 20 games):")
    for match_id in stored_match_ids[:-21:-1]:

        champion = get_player_champ(puuid, match_id)
        kills = str(get_player_kills(puuid, match_id))
        assists = str(get_player_assists(puuid, match_id))
        deaths = str(get_player_deaths(puuid, match_id))
        print(f"Champion: {champion:10s} | Kills: {kills:5s} | Deaths: {deaths:5s} | Assists: {assists:5s}")


    




    


if __name__ == "__main__":
    main()

