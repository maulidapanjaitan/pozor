# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ProjectRadar
def demo():
    print("=== ProjectRadar Demo ===")
    print()

    projects = [
        {"name": "Project Alpha", "risk": "medium", "priority": 8, "phase": "planning", "next_action": "Review budget"},
        {"name": "Project Beta", "risk": "high", "priority": 10, "phase": "execution", "next_action": "Mitigate risk"},
        {"name": "Project Gamma", "risk": "low", "priority": 5, "phase": "review", "next_action": "Archive"},
    ]

    for p in projects:
        print(f"Project: {p['name']}")
        print(f"  Risk: {p['risk']}")
        print(f"  Priority: {p['priority']}")
        print(f"  Phase: {p['phase']}")
        print(f"  Next Action: {p['next_action']}")
        print()

    print("Demo complete.")
