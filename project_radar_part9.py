# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ProjectRadar
import json, sys, os
from datetime import datetime

def load_initial_data(json_string):
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Инициализация глобальных переменных проекта
        global projects, risks, priorities
        
        projects = {p['id']: p.copy() for p in data.get('projects', [])}
        risks = {r['project_id']: r for r in data.get('risks', [])}
        
        # Преобразование дат в объекты datetime для удобства работы
        def parse_date(date_str):
            if not date_str: return None
            formats = ['%Y-%m-%d', '%d.%m.%Y']
            for fmt in formats:
                try: return datetime.strptime(date_str, fmt)
                except ValueError: pass
            return None
        
        # Обновляем даты в проектах и рисках
        for pid, proj in projects.items():
            if 'start_date' in proj: proj['start_date'] = parse_date(proj['start_date'])
            if 'end_date' in proj: proj['end_date'] = parse_date(proj['end_date'])
            
            # Обновляем даты в рисках этого проекта
            for risk_id, risk in risks.items():
                if risk.get('project_id') == pid:
                    if 'due_date' in risk: risk['due_date'] = parse_date(risk['due_date'])

        priorities = {p['id']: p.get('priority', 3) for p in projects.values()}
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)
    
    return data
