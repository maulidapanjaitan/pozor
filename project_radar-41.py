# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: ProjectRadar
def dry_run_mode():
    """Toggle dry-run mode: changes are logged instead of applied."""
    global dry_run
    dry_run = not dry_run
    status = "DRY RUN" if dry_run else "LIVE"
    print(f"[{status}] Mode active: {'WRITE' if dry_run else 'READ'} operations will be logged instead of executed.")
    return dry_run
