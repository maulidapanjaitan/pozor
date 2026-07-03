# === Stage 17: Добавь группировку записей по категориям ===
# Project: ProjectRadar
from collections import defaultdict, Counter
def group_by_category(records):
    grouped = defaultdict(list)
    for r in records:
        cat = r.get('category', 'Uncategorized')
        grouped[cat].append(r)
    summary = {k: {'count': len(v), 'items': v} for k, v in sorted(grouped.items())}
    return summary

def calculate_risk_score(record):
    base = record.get('priority', 3) * 10 + (5 if not record.get('stage') else 2)
    risk_factors = sum(1 for f in ['high_budget', 'new_vendor'] if f in record and record[f])
    return min(base + risk_factors * 15, 100)

def generate_next_actions(record):
    actions = []
    if not record.get('stage'):
        actions.append("Start project")
    elif record.get('status') == 'in_progress' and record.get('risk_score', 0) > 70:
        actions.append("Mitigate risks immediately")
    else:
        actions.append("Continue current stage")
    return actions

def enrich_and_group_projects(projects_data):
    enriched = []
    for p in projects_data:
        p['risk_score'] = calculate_risk_score(p)
        p['next_actions'] = generate_next_actions(p)
        enriched.append(p)
    grouped = group_by_category(enriched)
    return grouped
