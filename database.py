import sqlite3
from matches import get_matches_id

connection = sqlite3.connect('league_analyzer.db')
cursor = connection.cursor()



def create_database():

    player_table = "CREATE TABLE IF NOT EXISTS players(puuid TEXT PRIMARY KEY, riot_id TEXT)"

    cursor.execute(player_table)

    matches_table = "CREATE TABLE IF NOT EXISTS matches(puuid TEXT, match_id TEXT, PRIMARY KEY (puuid, match_id), FOREIGN KEY(puuid) REFERENCES players(puuid))"

    cursor.execute(matches_table)



def save_matches(puuid, riot_id):

    cursor.execute("INSERT OR IGNORE INTO players VALUES (?, ?)", (puuid, riot_id))
    
    match_ids = get_matches_id(puuid)

    for match_id in match_ids:
        cursor.execute("INSERT OR IGNORE INTO matches VALUES (?, ?)", (puuid, match_id))

    connection.commit()


def get_matches(puuid):

    cursor.execute("SELECT match_id FROM matches WHERE puuid = (?)", (puuid,))

    results = cursor.fetchall()

    print(results)

