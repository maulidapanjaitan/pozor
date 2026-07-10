# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ProjectRadar
import datetime as dt


def add_reminders(projects):
    """Добавляет поле reminder_date в каждый проект, если его нет."""
    for p in projects:
        if 'reminder_date' not in p:
            p['reminder_date'] = None


def get_due_today(projects):
    """Возвращает проекты, у которых напоминание на сегодня."""
    today = dt.date.today()
    return [p for p in projects if p.get('reminder_date') == today]


def set_reminder(project_id, reminder_dt_str):
    """Устанавливает дату напоминания для проекта по ID. Возвращает проект или None."""
    try:
        d = dt.datetime.strptime(reminder_dt_str, '%Y-%m-%d').date()
    except ValueError:
        return None
    for p in projects:
        if p['id'] == project_id:
            p['reminder_date'] = d
            return p


def remove_reminder(project_id):
    """Сбрасывает дату напоминания для проекта по ID."""
    for p in projects:
        if p['id'] == project_id:
            p['reminder_date'] = None
            return p
    return None


projects = [
    {'id': 1, 'name': 'Мини-проект А', 'status': 'active'},
    {'id': 2, 'name': 'Мини-проект Б', 'status': 'active'},
]

add_reminders(projects)

print(get_due_today(projects))          # [] — сегодня ничего нет

p = set_reminder(1, '2025-12-31')      # ← установим напоминание на 31 декабря
if p:
    print(f"Напоминание для {p['name']}: {p['reminder_date']}")
