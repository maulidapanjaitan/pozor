# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: ProjectRadar
def list_use_cases(projects, use_cases_db):
    """Показывает сценарии использования для каждого проекта.
    use_cases_db — словарь: проект_id -> список кортежей (название, описание).
    """
    print("\n📋 Сценарии использования:")
    print("-" * 60)
    for pid, cases in use_cases_db.items():
        print(f"\n🔹 Проект: {pid}")
        for name, desc in cases:
            print(f"   • {name}: {desc}")
    print("-" * 60)
