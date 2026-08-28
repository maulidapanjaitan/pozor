# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ProjectRadar
import argparse, sys
from project_radar import Radar, Risk, Action

def main():
    parser = argparse.ArgumentParser(description="ProjectRadar CLI")
    parser.add_argument("--add", type=str, help="Add a project: name,risks,actions")
    parser.add_argument("--report", nargs="*", default=[], help="Report on project(s)")
    parser.add_argument("--risk", type=str, help="Add risk: name,impact,probability")
    parser.add_argument("--action", type=str, help="Add action: name,owner,deadline")
    parser.add_argument("--remove", type=str, help="Remove project by name")
    parser.add_argument("--export", type=str, help="Export to JSON file")
    args = parser.parse_args()
    if args.add:
        parts = args.add.split(",")
        name = parts[0]; risks = parts[1].split(";") if len(parts)>1 else []; actions = parts[2].split(";") if len(parts)>2 else []
        proj = Radar(name, risks, actions)
        proj.save("projects.json")
        print(f"Project '{name}' added.")
    elif args.report:
        for p in args.report:
            proj = Radar.load(p)
            proj.report()
    elif args.risk:
        parts = args.risk.split(",")
        risk = Risk(parts[0], parts[1], parts[2])
        print(f"Risk '{risk.name}' added.")
    elif args.action:
        parts = args.action.split(",")
        action = Action(parts[0], parts[1], parts[2])
        print(f"Action '{action.name}' added.")
    elif args.remove:
        proj = Radar.load(args.remove)
        proj.remove()
        print(f"Project '{args.remove}' removed.")
    elif args.export:
        proj = Radar.load("projects.json")
        with open(args.export, "w") as f:
            f.write(proj.export())
        print(f"Exported to {args.export}")
    else:
        print("Usage: project_radar.py --help")

if __name__ == "__main__":
    main()
