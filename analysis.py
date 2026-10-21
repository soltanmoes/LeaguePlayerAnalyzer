#Calculate win rate, KDA, and performance statistics

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
        return None

    return winrate

def calculate_match_kda(participant_list):

    kda_list = []
    
    for participant in participant_list:

        kda_list.append( (participant["kills"] + participant["assists"]) / max(1, participant["deaths"]) )

    return kda_list

def calculate_overall_kda(participant_list):

    kills, deaths, assists = 0, 0, 0
    
    for participant in participant_list:

        kills += participant["kills"]
        assists += participant["assists"]
        deaths +=  participant["deaths"]

    return (kills + assists) / max(1, deaths)