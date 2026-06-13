# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ProjectRadar
class ProjectRadar:
    def __init__(self):
        self.projects = {}
    
    def add_project(self, name, risks, priorities, stages, next_actions):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя проекта должно быть непустой строкой")
        
        project_data = {
            'risks': risks if isinstance(risks, list) else [risks],
            'priorities': priorities if isinstance(priorities, dict) else {},
            'stages': stages if isinstance(stages, list) else [],
            'next_actions': next_actions if isinstance(next_actions, list) else []
        }
        
        self.projects[name] = project_data
        
    def get_project(self, name):
        return self.projects.get(name)
