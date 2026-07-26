# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ProjectRadar
class ProfileSwitcher:
    def __init__(self, profiles):
        self.profiles = profiles
        self.active_profile = None

    def set_active(self, profile_name):
        if profile_name in self.profiles:
            self.active_profile = profile_name
            return True
        print(f"Профиль '{profile_name}' не найден.")
        return False

    def get_active_profile(self):
        return self.active_profile

    def list_profiles(self):
        return list(self.profiles.keys())
