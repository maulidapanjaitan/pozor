# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ProjectRadar
def suggest_next_actions(project):
    """Generates recommended next actions based on project state."""
    if not project.get("risks", []):
        return ["Review existing risks and update mitigation plans"]
    
    high_risk_count = sum(1 for r in project["risks"] if r.get("severity") == "high")
    if high_risk_count > 2:
        return ["Escalate critical risks to stakeholders immediately", "Reassess project timeline with risk buffer"]
    
    unfinished_tasks = [t for t in project.get("tasks", []) if not t.get("completed")]
    if unfinished_tasks and len(unfinished_tasks) > 3:
        priorities = sorted([t["name"] for t in unfinished_tasks], key=lambda x: (0 if "critical" in x.lower() else 1, -x.count(".")))
        return [f"Focus on high-priority incomplete tasks first", f"Break down complex tasks into smaller milestones"]
    
    stages = project.get("stages", [])
    current_stage = project.get("current_stage", "")
    if not current_stage or current_stage == "planning":
        return ["Define detailed task breakdown for each stage", "Assign owners to all identified tasks"]
    elif current_stage in ("execution", "monitoring"):
        actions = []
        if unfinished_tasks:
            actions.append("Complete pending tasks before proceeding")
        if project.get("risks"):
            actions.append("Update risk response plans based on latest assessments")
        return actions
    
    completed_pct = len([t for t in project.get("tasks", []) if t.get("completed")]) / max(len(project["tasks"]), 1) * 100
    if completed_pct >= 80:
        return ["Prepare final deliverables and documentation", "Conduct post-project review and lessons learned"]
    
    return ["Continue current phase activities", "Monitor progress against milestones"]
