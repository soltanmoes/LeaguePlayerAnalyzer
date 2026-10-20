import requests

def get_champion_names():

    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version_response = requests.get(version_url, timeout=10)
    version = version_response.json()
    latest = version[0]

    champ_url = f"https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion.json" 

    champ_response = requests.get(champ_url, timeout=10)

    champion_data = champ_response.json()

    champion_names = {
            int(champion["key"]): champion["name"]
            for champion in champion_data["data"].values()
    }

    return champion_names

