#Calculate win rate, KDA, and performance statistics

def calculate_win_rate(participants):

    wins = 0
    losses = 0

    for participant in participants:
        
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

def calculate_match_kda(participants):
    
    if not participants:
        return None

    kda_list = []
    
    for participant in participants:

        kda_list.append( (participant["kills"] + participant["assists"]) / max(1, participant["deaths"]) )

    return kda_list

def calculate_overall_kda(participants):

    if not participants:
        return None
    
    kills, deaths, assists = 0, 0, 0
    
    for participant in participants:

        kills += participant["kills"]
        assists += participant["assists"]
        deaths +=  participant["deaths"]

    return (kills + assists) / max(1, deaths)

def group_by_champion(participants):

    grouped_matches = {}

    for participant in participants:
        if participant["championName"] not in grouped_matches:
            grouped_matches[participant["championName"]] = []
        grouped_matches[participant["championName"]].append(participant)

    return grouped_matches