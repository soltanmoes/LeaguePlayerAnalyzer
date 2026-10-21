import requests

from config import HEADERS

def get_matches_id(puuid):

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    response = requests.get(url, headers=HEADERS, timeout=10)

    response.raise_for_status()

    # print("Match IDs:", response.text[:500])

    return response.json()

def get_matches(puuid):

    match_ids = get_matches_id(puuid)

    matches = []

    for matchId in match_ids[:10]:

        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}"

        response = requests.get(url, headers=HEADERS, timeout=10)

        # print("Status code:", response.status_code)
        # print("Response:", response.text[:500])

        response.raise_for_status()

        match = response.json()

        matches.append(match)

    return matches

def get_player_participants(matches, puuid):

    participants = []
    
    for match in matches:
        for participant in match["info"]["participants"]:
            if participant["puuid"] == puuid:

                participants.append(participant)
                
                break

    return participants



