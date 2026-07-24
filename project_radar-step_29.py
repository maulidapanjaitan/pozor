# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: ProjectRadar
APP_CONFIG = {
    "app_name": "ProjectRadar",
    "version": "1.0.0",
    "max_projects": 25,
    "default_priority": "medium",
    "risk_levels": ["low", "medium", "high"],
    "status_colors": {"planned": "\033[94m", "in_progress": "\033[95m", "completed": "\033[92m"},
    "output_dir": "./output",
    "log_level": "INFO"
}

def get_config(key, default=None):
    """Retrieve config value with fallback."""
    return APP_CONFIG.get(key, default)

def set_config(key, value):
    """Set and persist a config value."""
    APP_CONFIG[key] = value
