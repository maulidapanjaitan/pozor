# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ProjectRadar
def export_state_to_json():
    import json
    from datetime import datetime
    
    # Формируем словарь состояния проекта
    state = {
        "project_name": project_config.get("name", "ProjectRadar"),
        "timestamp": datetime.utcnow().isoformat(),
        "projects": []
    }
    
    for proj in projects:
        proj_state = {
            "id": proj["id"],
            "title": proj["title"],
            "risk_level": proj.get("risk", "medium"),
            "priority": proj.get("priority", 5),
            "stages": [s["name"] for s in proj.get("stages", [])],
            "next_actions": proj.get("actions", []),
            "status": proj.get("status", "active")
        }
        state["projects"].append(proj_state)
    
    # Преобразуем в строку JSON с отступами для читаемости
    json_string = json.dumps(state, indent=2, ensure_ascii=False)
    return json_string
