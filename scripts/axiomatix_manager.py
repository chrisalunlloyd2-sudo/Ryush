import sqlite3
import os

DB_PATH = os.path.expanduser('~/project_registry.db')

def update_topology(filepath, weight, axiomatix_set):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        UPDATE file_registry 
        SET topology_weight = ?, axiomatix_set = ?
        WHERE filepath = ?
    """, (weight, axiomatix_set, filepath))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Axiomatix Topology Manager Initialized.")
