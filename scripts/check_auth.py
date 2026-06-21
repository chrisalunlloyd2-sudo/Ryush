import subprocess
import sys

def verify_auth():
    """Verifies GitHub CLI authentication status."""
    try:
        # Check auth status for github.com
        result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("[Ryush-Auth] Verified: Authenticated with GitHub.")
            return True
        else:
            print("[Ryush-Auth] ALERT: Authentication missing or expired.")
            print("[Ryush-Auth] ACTION REQUIRED: Please run 'gh auth login' in your local terminal.")
            return False
    except FileNotFoundError:
        print("[Ryush-Auth] ERROR: GitHub CLI (gh) not found.")
        return False

if __name__ == "__main__":
    if not verify_auth():
        sys.exit(1)
