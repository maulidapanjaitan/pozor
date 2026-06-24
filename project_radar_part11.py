# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ProjectRadar
import json, os

def save_project_data(data):
    try:
        with open('project_radar.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Данные успешно сохранены в project_radar.json")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def load_project_data():
    if os.path.exists('project_radar.json'):
        try:
            with open('project_radar.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
    return {}

if __name__ == "__main__":
    # Пример использования для проверки работы сохранения и загрузки
    sample_data = {"status": "active", "version": 1}
    save_project_data(sample_data)
    loaded_data = load_project_data()
    print(f"Загруженные данные: {loaded_data}")
