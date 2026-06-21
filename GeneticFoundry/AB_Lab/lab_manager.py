import sqlite3
import os
import shutil

AB_LAB_DIR = os.path.expanduser('~/Ryush/GeneticFoundry/AB_Lab')
DB_PATH = os.path.join(AB_LAB_DIR, 'ab_experiments.db')

def init_lab():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS experiments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            experiment_name TEXT,
            variant_a_hash TEXT,
            variant_b_hash TEXT,
            winner TEXT,
            metrics TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def log_experiment(name, v_a, v_b, winner, metrics):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO experiments (experiment_name, variant_a_hash, variant_b_hash, winner, metrics) VALUES (?, ?, ?, ?, ?)",
                (name, v_a, v_b, winner, metrics))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_lab()
    print("A/B Lab Initialized.")
