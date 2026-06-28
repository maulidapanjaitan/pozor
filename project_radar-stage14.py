# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ProjectRadar
def generate_summary():
    if not projects: return print("Нет данных для сводки.")
    total_risk = sum(p['risk'] for p in projects)
    high_priority = [p for p in projects if p.get('priority', 0) >= 8]
    blocked = [p for p in projects if 'blockers' in p and p['blockers']]
    print(f"\n=== СВОДКА ПРОЕКТОВ ===")
    print(f"Всего проектов: {len(projects)}")
    print(f"Суммарный риск (0-10): {total_risk:.1f}")
    if high_priority:
        print("Высокий приоритет:")
        for p in high_priority[:3]:
            print(f"  - {p['name']}: {p.get('priority', 'N/A')}")
    if blocked:
        print("Блокированные задачи:")
        for b in blocked:
            print(f"  - {b['name']}: {'; '.join(b['blockers'])}")
    actions = [f"{p['next_action']} ({p.get('due', 'N/A')})" for p in projects if p.get('next_action')]
    if actions:
        print("Следующие действия:")
        for a in actions[:5]:
            print(f"  - {a}")
