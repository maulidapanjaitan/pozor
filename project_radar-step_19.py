# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ProjectRadar
def archive_records(records, cutoff_days=365):
    """Archive records older than cutoff_days and return archived list."""
    import datetime
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=cutoff_days)
    archived = []
    for r in records:
        if hasattr(r, 'created') or hasattr(r, 'updated'):
            ts = getattr(r, 'created', getattr(r, 'updated', None))
            if not ts:
                continue
            try:
                dt = datetime.datetime.fromtimestamp(ts) if isinstance(ts, (int, float)) else ts
                if dt < cutoff:
                    archived.append({'status': 'archived', 'record': r})
            except Exception:
                pass
    return archived
