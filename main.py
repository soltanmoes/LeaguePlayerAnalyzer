from analysis import calculate_win_rate, calculate_overall_kda, group_by_champion
from matches import get_matches, fetch_match_ids
from player import get_riot_id, get_puuid
from database import *
from sync import add_participants_to_table
import json

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

    participant_list = get_stored_participants(puuid)

    winrate = calculate_win_rate(participant_list)
    overall_kda = calculate_overall_kda(participant_list)

    print(f"Total matches analyzed: {len(stored_match_ids)}")
    print(f"Winrate: {winrate:.1f}%")
    print(f"Overall KDA: {overall_kda:.2f}")

    grouped_champions = group_by_champion(participant_list)
    print(f"\nChampion performance:")

    #for key in grouped_champions[index]:
        #print(grouped_champions[index][key])

    for grouped_champ in grouped_champions:
        winrate = calculate_win_rate(grouped_champ[1])
        overall_kda = calculate_overall_kda(grouped_champ[1])
        games_count = str(len(grouped_champ[1]))
        print(f"{grouped_champ[0]:10s} | {games_count:3s} games | {winrate:.1f}% WR | {overall_kda:.2f} KDA")


    print("\nMatch history (last 20 games):")
    for match_id in stored_match_ids[:-21:-1]:

        champion = get_player_champ(puuid, match_id)
        kills = str(get_player_kills(puuid, match_id))
        assists = str(get_player_assists(puuid, match_id))
        deaths = str(get_player_deaths(puuid, match_id))
        print(f"Champion: {champion:10s} | Kills: {kills:5s} | Deaths: {deaths:5s} | Assists: {assists:5s}")


    




    


if __name__ == "__main__":
    main()

