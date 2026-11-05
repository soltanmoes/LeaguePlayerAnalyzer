import requests

from config import HEADERS

def fetch_match_ids(puuid):

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    response = requests.get(url, headers=HEADERS, timeout=10)

    response.raise_for_status()
    
    print("Checking match history...\n")

    return response.json()

def get_matches(puuid):

    match_ids = fetch_match_ids(puuid)

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

def get_player_in_participants(matches, puuid):

    participants = []
    
    for match in matches:
        for participant in match["info"]["participants"]:
            if participant["puuid"] == puuid:

                participants.append(participant)
                
                break

    return participants



