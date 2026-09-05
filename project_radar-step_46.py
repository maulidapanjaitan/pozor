# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ProjectRadar
def migrate_data_structure(old_data):
    """Upgrade data schema from v1 to v2.
    
    v1: {name, description, risk, priority, stages, next_actions}
    v2: {name, description, risk, priority, stages, next_actions, tags, created_at, updated_at, status}
    """
    import datetime
    v2 = {}
    for key, val in old_data.items():
        if key in ('name', 'description', 'risk', 'priority', 'stages', 'next_actions'):
            v2[key] = val
        else:
            v2[key] = ''
    v2['tags'] = []
    v2['created_at'] = v2.get('created_at', datetime.datetime.now().isoformat())
    v2['updated_at'] = datetime.datetime.now().isoformat()
    v2['status'] = 'active'
    return v2
