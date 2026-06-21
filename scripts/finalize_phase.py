import os
import tarfile
import hashlib
import datetime
import shutil

PROJECT_DIR = os.path.expanduser('~/Ryush')
SNAPSHOT_DIR = os.path.join(PROJECT_DIR, 'snapshots')

def create_snapshot():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    snapshot_name = f"snapshot_{timestamp}.tar.gz"
    snapshot_path = os.path.join(SNAPSHOT_DIR, snapshot_name)
    
    with tarfile.open(snapshot_path, "w:gz") as tar:
        for root, dirs, files in os.walk(PROJECT_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                if '.git' in file_path or 'snapshots' in file_path:
                    continue
                tar.add(file_path, arcname=os.path.relpath(file_path, PROJECT_DIR))
    print(f"Snapshot created: {snapshot_name}")

def update_readme():
    readme_path = os.path.join(PROJECT_DIR, 'README.md')
    blueprint_path = os.path.join(PROJECT_DIR, 'blueprint.md')
    
    with open(blueprint_path, 'r') as b:
        blueprint_content = b.read()
        
    with open(readme_path, 'a') as r:
        r.write(f"\n\n## Phase Snapshot - {datetime.datetime.now().isoformat()}\n")
        r.write(blueprint_content)
    print("README updated.")

if __name__ == "__main__":
    create_snapshot()
    update_readme()
