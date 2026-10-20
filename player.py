import os
from dotenv import load_dotenv
import requests

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}

def get_riot_id():

    while True:
        riotID = input("\nEnter Riot ID: ").strip()

        if "#" not in riotID:
            print(f"\n\"{riotID}\" is not a valid Riot ID")
            continue

        riot_id_split = riotID.split('#', 1)
        game_name = riot_id_split[0]
        tag_line = riot_id_split[1]

        if not game_name or not tag_line:
            print(f"\n\"{riotID}\" is not a valid Riot ID")
            continue

        return game_name, tag_line


def get_puuid(game_name, tag_line):

    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    response = requests.get(url, headers=headers, timeout=10)

    response.raise_for_status()

    data_riot_id = response.json()

    puuid = data_riot_id["puuid"]

    return puuid