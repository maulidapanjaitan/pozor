# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ProjectRadar
import json, os, sys

def load_projects_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            projects = [p for p in data if isinstance(p, dict)]
        else:
            print("Ошибка: JSON должен содержать массив объектов.")
            return []
        print(f"Загружено {len(projects)} проектов из '{file_path}'.")
        return projects
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла: {e}")
        return []

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "projects.json"
    projects = load_projects_from_file(file_path)
