# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ProjectRadar
import json


class UserProfileManager:
    def __init__(self, storage_file="profiles.json"):
        self.storage_file = storage_file
        self.profiles = {}
        if os.path.exists(storage_file):
            with open(storage_file) as f:
                self.profiles = json.load(f)

    def add_profile(self, name, role, email="", phone=""):
        if name in self.profiles:
            print(f"Профиль '{name}' уже существует.")
            return False
        self.profiles[name] = {"role": role, "email": email, "phone": phone}
        with open(self.storage_file, "w") as f:
            json.dump(self.profiles, f)
        print(f"Профиль '{name}' добавлен.")
        return True

    def get_profile(self, name):
        if not self.profiles.get(name):
            print(f"Профиль '{name}' не найден.")
            return None
        return self.profiles[name]

    def delete_profile(self, name):
        if not self.profiles.pop(name, None):
            print(f"Профиль '{name}' удалён (не существовал).")
            return False
        with open(self.storage_file, "w") as f:
            json.dump(self.profiles, f)
        print(f"Профиль '{name}' удалён.")
        return True

    def list_profiles(self):
        if not self.profiles:
            print("Нет сохранённых профилей.")
            return []
        return [{"имя": k, "роль": v["role"]} for k, v in self.profiles.items()]
