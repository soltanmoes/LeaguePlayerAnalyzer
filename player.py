import requests

from config import HEADERS

def get_riot_id():

    while True:
        riotID = input("\nEnter Riot ID: ").strip()

        if "#" not in riotID:
            print(f"\n\"{riotID}\" is not a valid Riot ID")
            continue

        riot_id_split = riotID.split('#', 1)
        game_name = riot_id_split[0]
        tag_line = riot_id_split[1]

        if not game_name.replace(' ','').isalnum() or not tag_line.isalnum():
            print(f"\n\"{riotID}\" is not a valid Riot ID")
            continue

        if not game_name or not tag_line:
            print(f"\n\"{riotID}\" is not a valid Riot ID")
            continue

        return game_name, tag_line


def get_puuid(game_name, tag_line):

    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    response.raise_for_status()
    
    while response.status_code != 200:
        
        print("\nPlayer not found.")

        game_name, tag_line = get_riot_id()
        
        url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        continue

    print("\nPlayer found!")
     
    data_riot_id = response.json()

    puuid = data_riot_id["puuid"]

    return puuid
