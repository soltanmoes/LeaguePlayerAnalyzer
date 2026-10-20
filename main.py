import os
from dotenv import load_dotenv
import requests

from config import HEADERS

from champions import get_champion_names
from matches import get_matches, calculate_winrate
from player import get_riot_id, get_puuid

champion_names = get_champion_names()

def most_played_champions(puuid):

    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
    response = requests.get(url, headers=headers, timeout=10)

    data_champ_mastery = response.json()

    print(f"Top 3 most played champions are:\n1.{champion_names[data_champ_mastery[0]["championId"]]} - Points: {data_champ_mastery[0]["championPoints"]}\n2.{champion_names[data_champ_mastery[1]["championId"]]} - Points: {data_champ_mastery[1]["championPoints"]}\n3.{champion_names[data_champ_mastery[2]["championId"]]} - Points: {data_champ_mastery[2]["championPoints"]} ")

def main():

    # most_played_champions(puuid)

    game_name, tag_line = get_riot_id()

    puuid = get_puuid(game_name, tag_line)

    matches = get_matches(puuid)

    winrate = calculate_winrate(matches, puuid)

    print(f"Winrate over last 10 games is {winrate}%")


if __name__ == "__main__":
    main()

