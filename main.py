import os
from dotenv import load_dotenv
import requests

from champions import get_champion_names

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

headers = {
    "X-Riot-Token": API_KEY
}


champion_names = get_champion_names()



def get_player():

    print("Enter Riot ID: ")
    riotID = input()

    riot_id_split = riotID.split('#', 1) # I split the user input after the # , this in order to seperate game_name and tag_line
    game_name = riot_id_split[0]
    tag_line = riot_id_split[1]

    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    response = requests.get(url, headers=headers)

    data_riot_id = response.json()

    puuid = data_riot_id["puuid"]

    return puuid

def most_played_champions():

    puuid = get_player()

    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
    response = requests.get(url, headers=headers)

    data_champ_mastery = response.json()
    
    print(f"Top 3 most played champions are:\n1.{champion_names[data_champ_mastery[0]["championId"]]} - Points: {data_champ_mastery[0]["championPoints"]}\n2.{champion_names[data_champ_mastery[1]["championId"]]} - Points: {data_champ_mastery[1]["championPoints"]}\n3.{champion_names[data_champ_mastery[2]["championId"]]} - Points: {data_champ_mastery[2]["championPoints"]} ")


def main():

    most_played_champions()

if __name__ == "__main__":
    main()

