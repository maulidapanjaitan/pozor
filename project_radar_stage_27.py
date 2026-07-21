# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ProjectRadar
def reset_demo_data():
    """Возвращает все состояния к демо-значениям для тестирования."""
    global _projects, _user, _search_query, _selected_project_id
    
    demo_projects = [
        {
            "id": 1, "name": "Радар", "status": "active",
            "priority": "high", "risk_level": "medium",
            "stage": ["planning", "design"], "next_action": "Согласовать дизайн"
        },
        {
            "id": 2, "name": "Локатор", "status": "active",
            "priority": "medium", "risk_level": "low",
            "stage": ["development"], "next_action": "Протестировать API"
        },
        {
            "id": 3, "name": "Компас", "status": "on_hold",
            "priority": "low", "risk_level": "high",
            "stage": ["planning"], "next_action": "Пересмотреть требования"
        }
    ]
    
    _projects = demo_projects
    _user = {"name": "Администратор", "role": "admin", "active_tasks": 0}
    _search_query = ""
    _selected_project_id = None
    
    print("✅ Демо-данные сброшены. Состояние очищено.")

def clear_all_state():
    """Полностью сбрасывает все переменные состояния."""
    global _projects, _user, _search_query, _selected_project_id
    
    _projects = []
    _user = {"name": "", "role": "guest", "active_tasks": 0}
    _search_query = ""
    _selected_project_id = None
    
    print("🧹 Все данные полностью очищены.")
