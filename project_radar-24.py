# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ProjectRadar
def print_record(record):
    status = {"R": "Риск", "P": "Проблема", "T": "Задача"}[record["status"]]
    print(f"\n{'─'*50}")
    print(f"  Запись #{record['id']}")
    print(f"  Статус: {status} | Приоритет: {'Крит.' if record['priority'] == 'critical' else 'Выс.' if record['priority'] == 'high' else 'Средн.' if record['priority'] == 'medium' else 'Низк.'}")
    print(f"  Описание: {record.get('description', '(нет)')}")
    print(f"  Этап: {record.get('current_stage', 'Не назначен')}")
    action = record.get("next_action", "Нет следующего действия.")
    if isinstance(action, dict):
        action = f"{action.get('what', '')} → {action.get('who', '')}: {action.get('by_when', '')}"
    print(f"  Следующее действие: {action}")
