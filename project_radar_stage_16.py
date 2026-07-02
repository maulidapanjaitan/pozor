# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ProjectRadar
def calculate_monthly_stats(data, start_date="2024-01-01", end_date=None):
    from datetime import datetime, timedelta
    if not data: return {}
    now = datetime.now()
    if end_date is None: end_date = now.strftime("%Y-%m-%d")
    months = []
    current = start_date
    while current <= end_date:
        year_month = f"{current[:4]}-{current[5:7]}"
        first_day = datetime.strptime(current, "%Y-%m-%d").replace(day=1)
        last_day = (first_day.replace(day=28) + timedelta(days=3)).strftime("%Y-%m-%d")
        if current > end_date: break
        month_data = [item for item in data if start_date <= item['date'] <= end_date and item['month'] == year_month]
        months.append({
            "period": f"{year_month}",
            "total_items": len(month_data),
            "high_risk_count": sum(1 for i in month_data if i.get('risk_level') == 'HIGH'),
            "avg_priority": sum(i.get('priority', 0) for i in month_data) / max(len(month_data), 1),
            "next_actions": [i['action'] for i in month_data if i.get('status') == 'TODO'][:5]
        })
        current = (datetime.strptime(current, "%Y-%m-%d") + timedelta(days=30)).strftime("%Y-%m-%d")
    return months
