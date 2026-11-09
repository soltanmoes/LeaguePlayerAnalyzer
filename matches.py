import requests

from config import HEADERS

def fetch_match_ids(puuid):

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    response = requests.get(url, headers=HEADERS, timeout=10)

    response.raise_for_status()
    
    print("Checking match history...\n")

    return response.json()


def get_matches(match_ids):

    matches = []

    for matchId in match_ids:

        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}"

        response = requests.get(url, headers=HEADERS, timeout=10)

        # print("Status code:", response.status_code)
        # print("Response:", response.text[:500])

        response.raise_for_status()

        match = response.json()

        matches.append(match)

    return matches


def get_player_in_participants(puuid, matches):

    participant_list = []
    
    for match in matches:
        for participant in match["info"]["participants"]:
            if participant["puuid"] == puuid:
                participant_list.append(participant)
                
                break

    return participant_list



