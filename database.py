import sqlite3
import json
from matches import fetch_match_ids

def get_connection():

    connection = sqlite3.connect('league_analyzer.db')
    connection.execute("PRAGMA foreign_keys = on")

    return connection


def create_database():

    connection = get_connection()

    cursor = connection.cursor()
    
    player_table = "CREATE TABLE IF NOT EXISTS players(puuid TEXT PRIMARY KEY, riot_id TEXT)"

    cursor.execute(player_table)

    matches_table = "CREATE TABLE IF NOT EXISTS matches(puuid TEXT, match_id TEXT, PRIMARY KEY (puuid, match_id), FOREIGN KEY(puuid) REFERENCES players(puuid))"

    cursor.execute(matches_table)

    
    participants_table = "CREATE TABLE IF NOT EXISTS participants(puuid TEXT, match_id TEXT, details TEXT, PRIMARY KEY (puuid, match_id), FOREIGN KEY(puuid) REFERENCES players(puuid), FOREIGN KEY(puuid, match_id) REFERENCES matches(puuid, match_id))"

    cursor.execute(participants_table)

    connection.commit()
    connection.close()


def save_matches(puuid, riot_id, match_ids):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT OR IGNORE INTO players VALUES (?, ?)", (puuid, riot_id))

    for match_id in match_ids:
        cursor.execute("INSERT OR IGNORE INTO matches VALUES (?, ?)", (puuid, match_id))

    connection.commit()
    connection.close()


def save_participants(puuid, match_id, details):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT OR IGNORE INTO participants (puuid, match_id, details) VALUES (?, ?, ?)", (puuid, match_id, details))

    connection.commit()
    connection.close()


def get_stored_match_ids(puuid):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT match_id FROM matches WHERE puuid = (?)", (puuid,))

    results = cursor.fetchall()

    stored_match_ids = [match_id[0] for match_id in results]

    connection.close()
    
    return stored_match_ids



def get_stored_participants(puuid):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT details FROM participants WHERE puuid = (?)", (puuid,))

    results = cursor.fetchall()

    participant_list_temp = [participant[0] for participant in results]
    
    participant_list = []

    for participant in participant_list_temp:
        participant_list.append(json.loads(participant))

    connection.close()
    
    return participant_list


def get_player_kills(puuid, match_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT json_extract(details, '$.kills') AS kills FROM participants WHERE puuid = (?) AND match_id = (?)", (puuid, match_id))

    results = cursor.fetchall()

    connection.close()
    
    return results[0][0]


def get_player_assists(puuid, match_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT json_extract(details, '$.assists') AS assists FROM participants WHERE puuid = (?) AND match_id = (?)", (puuid, match_id))

    results = cursor.fetchall()

    connection.close()
    
    return results[0][0]


def get_player_deaths(puuid, match_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT json_extract(details, '$.deaths') AS deaths FROM participants WHERE puuid = (?) AND match_id = (?)", (puuid, match_id))

    results = cursor.fetchall()

    connection.close()
    
    return results[0][0]


def get_player_champ(puuid, match_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT json_extract(details, '$.championName') AS champion FROM participants WHERE puuid = (?) AND match_id = (?)", (puuid, match_id))

    results = cursor.fetchall()

    connection.close()

    print(f"Results: {results}")
    
    return results[0][0]


def drop_participants_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS participants")

    connection.commit()
    connection.close()
