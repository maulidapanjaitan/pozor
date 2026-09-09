# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: ProjectRadar
def self_check():
    """Финальная самопроверка: проверяет, что все ключевые сущности и функции определены."""
    required = [
        "ProjectRadar", "Risk", "Priority", "Stage", "Action",
        "add_risk", "add_priority", "add_stage", "add_action",
        "get_risks", "get_priorities", "get_stages", "get_actions",
        "display_dashboard", "generate_report",
    ]
    missing = [name for name in required if not hasattr(ProjectRadar, name)]
    if missing:
        print(f"⚠️  Финальная проверка: найдено {len(missing)} недостающих элементов: {missing}")
        return False
    print("✅ Финальная самопроверка пройдена: все ключевые сущности и функции определены.")
    return True

if __name__ == "__main__":
    ok = self_check()
    if ok:
        print("🎉 Проект ProjectRadar готов к использованию.")
    else:
        print("❌ Проект ProjectRadar требует доработки.")
