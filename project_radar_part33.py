# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ProjectRadar
def undo_last_action(action_log):
    """Откат последнего действия в логе действий проекта."""
    if not action_log:
        return "Нет действий для отката."
    
    last_action = action_log[-1]
    action_type = last_action.get("type")
    
    if action_type == "add_project":
        project_id = last_action.get("project_id")
        undone_projects.remove(project_id)
        undone_risks[project_id] = last_action.get("risks", [])
        undone_priorities[project_id] = last_action.get("priorities", [])
        undone_phases[project_id] = last_action.get("phases", [])
        undone_next_steps[project_id] = last_action.get("next_steps", [])
        
    elif action_type == "add_risk":
        project_id = last_action.get("project_id")
        risk_id = last_action.get("risk_id")
        if risk_id in undone_risks:
            undone_risks.pop(risk_id)
            
    elif action_type == "update_priority":
        project_id = last_action.get("project_id")
        priority_name = last_action.get("priority_name")
        priority_value = last_action.get("priority_value")
        if priority_name in undone_priorities:
            undone_priorities[priority_name] = priority_value
            
    elif action_type == "add_phase":
        project_id = last_action.get("project_id")
        phase_name = last_action.get("phase_name")
        phase_description = last_action.get("phase_description")
        if phase_name in undone_phases:
            undone_phases[phase_name] = phase_description
            
    elif action_type == "add_next_step":
        project_id = last_action.get("project_id")
        step_text = last_action.get("step_text")
        due_date = last_action.get("due_date")
        if step_text in undone_next_steps:
            undone_next_steps[step_text] = due_date
            
    return f"Отменено действие: {action_type} для проекта {project_id}"
