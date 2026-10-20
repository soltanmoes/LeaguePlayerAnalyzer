import os
from dotenv import load_dotenv
import requests

from config import HEADERS

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}

def get_matches_id(puuid):

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    response = requests.get(url, headers=headers, timeout=10)

    # print("Match IDs:", response.text[:500])

    return response.json()

def get_matches(puuid):

    match_ids = get_matches_id(puuid)

    matches = []

    for matchId in match_ids[:10]:

        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}"

        response = requests.get(url, headers=headers, timeout=10)

        # print("Status code:", response.status_code)
        # print("Response:", response.text[:500])

        response.raise_for_status()

        match = response.json()

        matches.append(match)

    return matches

def calculate_winrate(matches, puuid):

    wins = 0
    losses = 0

    for match in matches[:10]:
        for participant in match["info"]["participants"]:
            if participant["puuid"] == puuid:
                
                if participant["win"]:
                    wins += 1
                else:
                    losses += 1
                
                break

    total = wins + losses
    
    if total != 0:
        winrate = wins / total * 100
    else: 
        winrate = 0

    return winrate
        


