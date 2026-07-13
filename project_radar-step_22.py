# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ProjectRadar
import datetime

def check_overdue_reminders(reminders, today):
    overdue = []
    for reminder in reminders:
        if isinstance(reminder['date'], str):
            due_date = datetime.datetime.fromisoformat(reminder['date'])
        else:
            due_date = reminder['date']
        if due_date < today and reminder.get('done', False) is False:
            overdue.append({'id': reminder['id'], 'name': reminder['title'], 'due': due_date, 'days_over': (today - due_date).days})
    return overdue
