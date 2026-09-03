# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ProjectRadar
def backup_data_file(source_path, backup_dir="backups"):
    """Создать резервную копию файла данных.
    
    Args:
        source_path: Путь к исходному файлу данных.
        backup_dir: Путь к директории для бэкапов.
    
    Returns:
        Путь к созданной копии или None если ошибка.
    """
    import os
    import shutil
    from datetime import datetime
    
    if not os.path.exists(source_path):
        print(f"Ошибка: файл {source_path} не найден")
        return None
    
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(source_path)}")
    
    try:
        shutil.copy2(source_path, backup_path)
        print(f"Резервная копия создана: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Ошибка при создании бэкапа: {e}")
        return None
