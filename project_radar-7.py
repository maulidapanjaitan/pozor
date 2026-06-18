# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ProjectRadar
def sort_projects(projects, key='date'):
    if not projects: return []
    reverse = {'priority': True, 'name': False}.get(key, False)
    def get_val(p):
        v = p.get(key)
        if isinstance(v, str): return (0, v.lower())
        return (1, 0.0) if v is None else (0, float(v))
    return sorted(projects, key=get_val, reverse=reverse)
