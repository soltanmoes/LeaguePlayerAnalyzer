import json
from matches import get_player_in_participants
from database import save_participants

def add_participants_to_table(puuid, matches):

    for match in matches:

        match_id = match["metadata"]["matchId"]

        participant = get_player_in_participants(puuid, match)
        participant_json = json.dumps(participant, indent=4)
        
        save_participants(puuid, match_id, participant_json)

def get_new_match_ids(api_match_ids, stored_match_ids):

    return list((set(api_match_ids)&set(stored_match_ids))^set(api_match_ids))

