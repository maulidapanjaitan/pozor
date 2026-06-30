# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ProjectRadar
def calculate_weekly_stats(stats_list):
    from datetime import datetime, timedelta
    if not stats_list: return {}
    grouped = {}
    for entry in stats_list:
        date_str = entry.get('date') or entry.get('timestamp', '')
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            week_start = (dt - timedelta(days=dt.weekday())).strftime('%Y-%m-%d')
            key = f"{week_start}W{dt.isocalendar()[1]}"
        except Exception: continue
        if key not in grouped: grouped[key] = {'count': 0, 'total_risk': 0.0, 'avg_priority': 0.0}
        grouped[key]['count'] += 1
        risk_val = entry.get('risk', 0) or 0
        priority_val = entry.get('priority', 0) or 0
        grouped[key]['total_risk'] += risk_val
        grouped[key]['avg_priority'] += priority_val / max(1, len([e for e in stats_list if (datetime.fromisoformat(e.get('date') or '').replace('Z', '+00:00')) and abs((datetime.fromisoformat(e.get('date') or '').replace('Z', '+00:00').timestamp() - dt.timestamp()) / 86400) < 7]))
    return {k: {'count': v['count'], 'total_risk': round(v['total_risk'], 2), 'avg_priority': round(v['avg_priority'], 1)} for k, v in grouped.items()}
