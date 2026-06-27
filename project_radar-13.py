# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ProjectRadar
def search_projects(query, fields=None):
    if not query: return []
    if fields is None: fields = ['name', 'description']
    query_lower = query.lower()
    results = [p for p in projects if any(
        q in str(getattr(p, f, '')).lower() 
        for f in fields 
        for q in [query_lower]
    )]
    return sorted(results, key=lambda x: sum(q in str(getattr(x, f, '')) for f in fields), reverse=True)
