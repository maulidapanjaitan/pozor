# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ProjectRadar
class ProjectModel:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.risks = []
        self.priority = 0
        self.stages = []
        self.next_actions = []

    def add_risk(self, risk):
        if not isinstance(risk, str) or len(risk.strip()) == 0:
            raise ValueError("Риск должен быть непустой строкой")
        self.risks.append(risk)

    def set_priority(self, priority):
        if not isinstance(priority, int) or priority < 1 or priority > 10:
            raise ValueError("Приоритет должен быть целым числом от 1 до 10")
        self.priority = priority

    def add_stage(self, stage_name, status="planned"):
        if not isinstance(stage_name, str) or len(stage_name.strip()) == 0:
            raise ValueError("Название этапа должно быть непустой строкой")
        self.stages.append({"name": stage_name, "status": status})

    def add_action(self, action):
        if not isinstance(action, str) or len(action.strip()) == 0:
            raise ValueError("Действие должно быть непустой строкой")
        self.next_actions.append(action)

def validate_input(name, description, priority_str, risks_list, stages_list, actions_list):
    try:
        model = ProjectModel(name=name, description=description)
        model.set_priority(int(priority_str))
        for risk in risks_list:
            model.add_risk(risk)
        for stage in stages_list:
            if isinstance(stage, dict):
                model.add_stage(stage.get("name", ""), stage.get("status", "planned"))
            else:
                model.add_stage(stage)
        for action in actions_list:
            model.add_action(action)
        return model
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
        return None
