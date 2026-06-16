# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ProjectRadar
def delete_project(project_id: int) -> dict | None:
    if project_id not in projects_db:
        return {"success": False, "error": f"Проект с ID {project_id} не найден."}
    
    del projects_db[project_id]
    return {"success": True, "message": f"Проект {project_id} успешно удалён."}

def delete_task(project_id: int, task_id: str) -> dict | None:
    if project_id not in projects_db:
        return {"success": False, "error": f"Проект с ID {project_id} не найден."}
    
    tasks = projects_db[project_id].get("tasks", [])
    for i, task in enumerate(tasks):
        if task.get("id") == task_id:
            del tasks[i]
            return {"success": True, "message": f"Задача {task_id} в проекте {project_id} удалена."}
    
    return {"success": False, "error": f"Задача с ID {task_id} не найдена в проекте {project_id}."}

def delete_risk(project_id: int, risk_id: str) -> dict | None:
    if project_id not in projects_db:
        return {"success": False, "error": f"Проект с ID {project_id} не найден."}
    
    risks = projects_db[project_id].get("risks", [])
    for i, risk in enumerate(risks):
        if risk.get("id") == risk_id:
            del risks[i]
            return {"success": True, "message": f"Риск {risk_id} в проекте {project_id} удалён."}
    
    return {"success": False, "error": f"Риск с ID {risk_id} не найден в проекте {project_id}."}
