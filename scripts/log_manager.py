
import os
import hashlib
import ast
import difflib
from datetime import datetime

LOG_DIR = os.path.expanduser('~/Ryush/logs')
TRUNCATE_SIZE = 2048 

def log_event(event_data, code_context=""):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(LOG_DIR, f"{timestamp}_event.log")
    
    # Metadata: Hash, AST, Diff (genetic)
    code_hash = hashlib.sha256(code_context.encode()).hexdigest()
    ast_tree = str(ast.dump(ast.parse(code_context))) if code_context else ""
    
    with open(log_file, 'w') as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Hash: {code_hash}\n")
        f.write(f"AST: {ast_tree[:TRUNCATE_SIZE]}\n")
        f.write(f"Data: {str(event_data)[:TRUNCATE_SIZE]}\n")
    
    # Truncate if needed
    if os.path.getsize(log_file) > TRUNCATE_SIZE:
        with open(log_file, 'r+') as f:
            f.truncate(TRUNCATE_SIZE)

if __name__ == "__main__":
    log_event("Initialization Log", "def test(): pass")
