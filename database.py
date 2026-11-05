import sqlite3
from matches import fetch_match_ids

def create_database():

    connection = sqlite3.connect('league_analyzer.db')
    cursor = connection.cursor()
    
    player_table = "CREATE TABLE IF NOT EXISTS players(puuid TEXT PRIMARY KEY, riot_id TEXT)"

    cursor.execute(player_table)

    matches_table = "CREATE TABLE IF NOT EXISTS matches(puuid TEXT, match_id TEXT, PRIMARY KEY (puuid, match_id), FOREIGN KEY(puuid) REFERENCES players(puuid))"

    cursor.execute(matches_table)

    connection.commit()
    connection.close()


def save_matches(puuid, riot_id, match_ids):

    connection = sqlite3.connect('league_analyzer.db')
    cursor = connection.cursor()

    cursor.execute("INSERT OR IGNORE INTO players VALUES (?, ?)", (puuid, riot_id))

    for match_id in match_ids:
        cursor.execute("INSERT OR IGNORE INTO matches VALUES (?, ?)", (puuid, match_id))

    connection.commit()
    connection.close()


def get_stored_match_ids(puuid):

    connection = sqlite3.connect('league_analyzer.db')
    cursor = connection.cursor()

    cursor.execute("SELECT match_id FROM matches WHERE puuid = (?)", (puuid,))

    results = cursor.fetchall()

    stored_match_ids = [match_id[0] for match_id in results]

    connection.close()
    
    return stored_match_ids




