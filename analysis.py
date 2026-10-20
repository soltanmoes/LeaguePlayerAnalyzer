#Calculate win rate, KDA, and performance statistics

import requests
from config import HEADERS

def get_champion_mastery(puuid):

    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    response.raise_for_status()

    data_champ_mastery = response.json()

    return data_champ_mastery

def calculate_win_rate(participant_list):

    wins = 0
    losses = 0

    for participant in participant_list:
        
        if participant["win"]:
            wins += 1
        else:
            losses += 1

    total = wins + losses
    
    if total != 0:
        winrate = wins / total * 100
    else: 
        winrate = 0

    return winrate
        