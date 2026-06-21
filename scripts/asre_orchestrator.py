#!/usr/bin/env python3
import os
import re
import sqlite3
import hashlib
from datetime import datetime
import difflib

# --- CONFIGURATION ---
RYUSH_DIR = os.path.expanduser("~/Ryush")
DB_PATHS = {
    "registry": os.path.expanduser("~/project_registry.db"),
    "knowledge": os.path.expanduser("~/code_knowledge.db"),
    "ledger": os.path.expanduser("~/hash_ledger.db")
}
FUZZY_THRESHOLD = 0.85  # Matches the 85% Levenshtein rule

class AxiomatixReconciliationEngine:
    def __init__(self):
        self.init_reconciliation_tables()

    def init_reconciliation_tables(self):
        """Ensures the validation grid matrix is tracked inside the database."""
        conn = sqlite3.connect(DB_PATHS["registry"])
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS axiomatix_matrix (
                id TEXT PRIMARY KEY,
                framework_name TEXT,
                step_title TEXT,
                status TEXT DEFAULT 'Lapse',
                associated_file TEXT,
                last_verified TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def calculate_file_hash(self, filepath):
        """Generates SHA-256 signatures for the hash ledger pipeline."""
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def scan_for_text_duplicates(self, content_list):
        """Sliding-window comparison to detect overlapping documentation snapshots."""
        purged_content = []
        seen_signatures = set()

        for block in content_list:
            # Create a normalized structural signature for fuzzy matching
            normalized = re.sub(r'\s+', ' ', block).strip()
            
            # Simple hash check for exact matches
            block_hash = hashlib.md5(normalized.encode('utf-8')).hexdigest()
            if block_hash in seen_signatures:
                continue # Purge exact duplicate snapshot block
                
            # Fuzzy match verification against already processed blocks
            is_duplicate = False
            for seen_block in purged_content:
                ratio = difflib.SequenceMatcher(None, normalized, seen_block).ratio()
                if ratio >= FUZZY_THRESHOLD:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                seen_signatures.add(block_hash)
                purged_content.append(block)
                
        return purged_content

    def verify_step_implementation(self, step_id, structural_regex, search_file):
        """Validates framework steps against live physical source components."""
        full_path = os.path.join(RYUSH_DIR, search_file)
        if not os.path.exists(full_path):
            return "Lapse"

        with open(full_path, 'r', encoding='utf-8') as f:
            code_content = f.read()

        # Check for matching symbols or structures defined in blueprint step
        if re.search(structural_regex, code_content):
            self.check_off_step(step_id, search_file)
            return "Verified"
        
        return "Lapse"

    def check_off_step(self, step_id, filepath):
        """Updates the internal matrix status to verified."""
        conn = sqlite3.connect(DB_PATHS["registry"])
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE axiomatix_matrix 
            SET status = 'Verified', associated_file = ?, last_verified = ?
            WHERE id = ?
        """, (filepath, datetime.now().isoformat(), step_id))
        conn.commit()
        conn.close()

# --- INITIALIZATION EXECUTION LOOP ---
if __name__ == "__main__":
    print("[Ryush-ASRE] Initializing Axiomatix Structural Reconciliation Engine...")
    engine = AxiomatixReconciliationEngine()
    print("[Ryush-ASRE] System listening on database matrices. Ready for operational mutations.")
