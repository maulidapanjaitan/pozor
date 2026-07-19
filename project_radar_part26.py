# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ProjectRadar
def run_demo():
    """Демо-команда: показывает первый проект и его следующий шаг."""
    print("=" * 60)
    print("DEMO: ProjectRadar Quick Test")
    print("=" * 60)
    if projects:
        p = projects[0]
        print(f"Проект: {p.name}")
        print(f"Риск: {p.risk_level} | Приоритет: {p.priority}")
        if p.next_action:
            print(f"Следующий шаг: {p.next_action}")
    else:
        print("Нет проектов для демо.")
