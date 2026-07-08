# === Stage 20: Добавь восстановление записей из архива ===
# Project: ProjectRadar
def load_archive(path):
    """Загрузка записей из текстового архива в формате: name|risk|priority|phase|next_action"""
    records = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = [p.strip() for p in line.split('|')]
                if len(parts) == 5:
                    records.append({
                        'name': parts[0],
                        'risk': int(parts[1]),
                        'priority': int(parts[2]),
                        'phase': int(parts[3]),
                        'next_action': parts[4]
                    })
    except FileNotFoundError:
        return []
    return records
