# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ProjectRadar
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_id: {"name": str, "projects": set}}
    
    def add_tag(self, name: str) -> int:
        if not name.strip(): return None
        tag_id = hash(name) % 100000
        while tag_id in self.tags and len(self.tags[tag_id]["name"]) > 20:
            tag_id += 1
        self.tags[tag_id] = {"name": name, "projects": set()}
        return tag_id
    
    def remove_tag(self, tag_id: int) -> bool:
        if tag_id not in self.tags: return False
        del self.tags[tag_id]
        return True
    
    def add_project_to_tag(self, tag_id: int, project_key: str):
        if tag_id in self.tags and project_key:
            self.tags[tag_id]["projects"].add(project_key)
    
    def remove_project_from_tag(self, tag_id: int, project_key: str):
        if tag_id in self.tags and project_key in self.tags[tag_id]["projects"]:
            self.tags[tag_id]["projects"].remove(project_key)
            return True
        return False
    
    def get_tags_for_project(self, project_key: str) -> list:
        result = []
        for tid, data in self.tags.items():
            if project_key in data["projects"]:
                result.append({"id": tid, "name": data["name"]})
        return result
