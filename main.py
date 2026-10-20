import os
from dotenv import load_dotenv
import requests

from champions import get_champion_names
from matches import get_matches, calculate_winrate
from player import get_player

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}

champion_names = get_champion_names()

puuid = get_player()

def most_played_champions(puuid):

    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
    response = requests.get(url, headers=headers, timeout=10)

    data_champ_mastery = response.json()

    print(f"Top 3 most played champions are:\n1.{champion_names[data_champ_mastery[0]["championId"]]} - Points: {data_champ_mastery[0]["championPoints"]}\n2.{champion_names[data_champ_mastery[1]["championId"]]} - Points: {data_champ_mastery[1]["championPoints"]}\n3.{champion_names[data_champ_mastery[2]["championId"]]} - Points: {data_champ_mastery[2]["championPoints"]} ")

def main():

    # most_played_champions(puuid)

    matches = get_matches(puuid)

    winrate = calculate_winrate(matches, puuid)

    print(f"Winrate over last 20 games is {winrate}%")


if __name__ == "__main__":
    main()

