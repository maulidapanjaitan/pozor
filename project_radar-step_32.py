# === Stage 32: Добавь журнал действий пользователя ===
# Project: ProjectRadar
import datetime, json, os, sys

class ActionLog:
    def __init__(self):
        self.log_path = 'action_log.json'
        self.entries = []
        if os.path.exists(self.log_path):
            with open(self.log_path, 'r') as f:
                self.entries = json.load(f)

    def add_entry(self, user, action, timestamp=None):
        ts = datetime.datetime.now().isoformat() if timestamp is None else str(timestamp)
        entry = {
            "user": user,
            "action": action,
            "timestamp": ts
        }
        self.entries.append(entry)
        with open(self.log_path, 'w') as f:
            json.dump(self.entries, f, indent=2)

    def get_log(self):
        return self.entries

def main():
    log = ActionLog()
    print("=== User Action Log ===")
    print(f"Total entries: {len(log.get_log())}")
    for entry in log.get_log():
        print(f"[{entry['timestamp']}] {entry['user']}: {entry['action']}")

if __name__ == '__main__':
    main()
