import sqlite3

def load_top_players():
    conn = sqlite3.connect("top_players.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS top_players (name TEXT, score INT)")
    conn.commit()
    conn.close()

def get_top_players():
    conn = sqlite3.connect("top_players.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM top_players ORDER BY score DESC LIMIT 5")
    top_players = cursor.fetchall()
    conn.close()
    return top_players