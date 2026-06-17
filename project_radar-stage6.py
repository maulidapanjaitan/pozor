# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ProjectRadar
def filter_projects(status=None, category=None, tags=None):
    filtered = []
    for p in projects:
        if status and p['status'] != status: continue
        if category and p.get('category') != category: continue
        if tags:
            project_tags = set(p.get('tags', []))
            if not all(tag in project_tags for tag in tags): continue
        filtered.append(p)
    return filtered

def get_next_actions(projects, status=None, priority='high'):
    actions = []
    for p in projects:
        if status and p['status'] != status: continue
        if p.get('priority') != priority: continue
        next_action = p.get('next_step', 'Нет следующих действий')
        actions.append(f"{p['name']} ({p['id']}): {next_action}")
    return actions

if __name__ == "__main__":
    print("Фильтр по статусу 'active':")
    for proj in filter_projects(status='active'):
        print(f"  - {proj['name']}: {proj['status']}")
    
    print("\nСледующие действия для задач высокого приоритета:")
    for act in get_next_actions(projects, priority='high'):
        print(f"  * {act}")
