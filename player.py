import os
from dotenv import load_dotenv
import requests

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}

def get_player():

    print("Enter Riot ID: ")
    riotID = input()

    riot_id_split = riotID.split('#', 1)
    game_name = riot_id_split[0]
    tag_line = riot_id_split[1]

    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    response = requests.get(url, headers=headers, timeout=10)

    data_riot_id = response.json()

    puuid = data_riot_id["puuid"]

    return puuid