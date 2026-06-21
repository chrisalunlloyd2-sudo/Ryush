# Ryush

Self-organizing, self-documenting AI project.

## Status
Phase 1: Foundation.

## Topology
[ASCII Topology Placeholder]

## Phase Snapshot - 2026-06-20T23:42:08.041995
# Ryush Blueprint
# Ryush Blueprint

Methodical approach to stability.

## Registry Schemas
- `project_registry.db`:\n  `file_registry(id, filepath, language, project, sector, area, use_case)`

## Intent Vocabulary (run() mappings)
| Intent | Command |
| :--- | :--- |
| update aliens butt | cd ~/Ryush && git push -u origin master |
| register | python3 ~/project_registry.py |
| git add all | cd ~/Ryush && git add . |
| git commit | cd ~/Ryush && git commit -m 'Auto-commit' |
| status | cd ~/Ryush && git status |
| log event | python3 ~/Ryush/scripts/log_manager.py |
| archive old | python3 ~/sustain_and_init.py |
| sync | cd ~/Ryush && git pull && git push |

## Phase Snapshot - 2026-06-21T00:01:42.481664
# Ryush Blueprint
# Ryush Blueprint

Methodical approach to stability.
## Registry Schemas

### code_knowledge.db
```sql
CREATE TABLE code_knowledge(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    code TEXT NOT NULL,
    performatives TEXT NOT NULL,
    weight INTEGER DEFAULT 1,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### downloads.db
```sql
CREATE TABLE downloads(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_name TEXT UNIQUE,
    status TEXT,
    last_attempt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### hash_ledger.db
```sql
CREATE TABLE ledger(
    hash TEXT PRIMARY KEY,
    filename TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### project_registry.db
```sql
CREATE TABLE file_registry(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filepath TEXT UNIQUE,
    language TEXT,
    project TEXT,
    sector TEXT,
    area TEXT,
    use_case TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


## Intent Vocabulary (run() mappings)
| Intent | Command |
| :--- | :--- |
| update aliens butt | cd ~/Ryush && git push -u origin master |
| register | python3 ~/project_registry.py |
| git add all | cd ~/Ryush && git add . |
| git commit | cd ~/Ryush && git commit -m 'Auto-commit' |
| status | cd ~/Ryush && git status |
| log event | python3 ~/Ryush/scripts/log_manager.py |
| archive old | python3 ~/sustain_and_init.py |
| sync | cd ~/Ryush && git pull && git push |

## Phase Snapshot - 2026-06-21T00:24:10.278155
# Ryush Blueprint
# Ryush Blueprint

Methodical approach to stability.
## Registry Schemas

### code_knowledge.db
```sql
CREATE TABLE code_knowledge(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    code TEXT NOT NULL,
    performatives TEXT NOT NULL,
    weight INTEGER DEFAULT 1,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### downloads.db
```sql
CREATE TABLE downloads(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_name TEXT UNIQUE,
    status TEXT,
    last_attempt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### hash_ledger.db
```sql
CREATE TABLE ledger(
    hash TEXT PRIMARY KEY,
    filename TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### project_registry.db
```sql
CREATE TABLE file_registry(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filepath TEXT UNIQUE,
    language TEXT,
    project TEXT,
    sector TEXT,
    area TEXT,
    use_case TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


## Intent Vocabulary (run() mappings)
| Intent | Command |
| :--- | :--- |
| update aliens butt | cd ~/Ryush && git push -u origin master |
| register | python3 ~/project_registry.py |
| git add all | cd ~/Ryush && git add . |
| git commit | cd ~/Ryush && git commit -m 'Auto-commit' |
| status | cd ~/Ryush && git status |
| log event | python3 ~/Ryush/scripts/log_manager.py |
| archive old | python3 ~/sustain_and_init.py |
| sync | cd ~/Ryush && git pull && git push |