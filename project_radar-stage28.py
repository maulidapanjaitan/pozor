# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ProjectRadar
def project_metrics(projects):
    """Calculate key metrics across all projects."""
    total = len(projects)
    if total == 0:
        return {"active": 0, "done": 0, "avg_priority": 0.0, "total_risks": 0}

    active = sum(p["status"] in ("planning", "in_progress") for p in projects)
    done = sum(1 for p in projects if p["status"] == "completed")
    priorities = [p.get("priority", 3) for p in projects]
    risks = [sum(p["risks"].values()) for p in projects]

    return {
        "active": active,
        "done": done,
        "avg_priority": sum(priorities) / total if priorities else 0.0,
        "total_risks": sum(risks),
    }
