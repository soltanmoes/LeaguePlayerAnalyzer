import os
from dotenv import load_dotenv
import requests

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}

def get_matches_id(puuid):

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    response = requests.get(url, headers=headers, timeout=10)

    return response.json()

def get_matches(puuid):

    match_ids = get_matches_id(puuid)

    for matchId in match_ids[:5]:

        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}"

        response = requests.get(url, headers=headers, timeout=10)

        # print("Status code:", response.status_code)
        # print("Response:", response.text[:500])

        # response.raise_for_status()

        match = response.json()

        for participant in match["info"]["participants"]:
            if participant["puuid"] == puuid:
                if participant["win"]:
                    print ("Won")
                else:
                    print ("Lost")


