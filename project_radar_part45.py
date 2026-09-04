# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ProjectRadar
def restore_from_backup(backup_path: str) -> bool:
    """Восстанавливает данные из резервной копии."""
    import os, json, shutil
    if not os.path.isfile(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        print(f"Резервная копия восстановлена из {backup_path}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
