# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ProjectRadar
def print_project_table(projects):
    if not projects:
        print("Список проектов пуст.")
        return

    # Определяем ширину колонок
    col_widths = {}
    headers = ["ID", "Название", "Статус", "Риск", "Приоритет", "Этап"]
    for h in headers:
        col_widths[h] = max(len(h), max((len(str(p.get(k, ""))) for p in projects if k in p), default=len(h)))

    # Формируем строки таблицы
    rows = [f"{'─' * sum(col_widths.values()) + '┘'}"]
    row_header = "│".join(h.ljust(col_widths[h]) for h in headers)
    rows.append(row_header)
    rows.append("│".join('─' * col_widths[h] for h in headers))

    for p in projects:
        cells = []
        for k, w in zip(headers, col_widths):
            val = str(p.get(k, ""))
            cells.append(val.ljust(w))
        rows.append("│".join(cells))
    rows[-1] += "└"

    print("\n".join(rows))


if __name__ == "__main__":
    sample_projects = [
        {"id": 1, "title": "Мобильное приложение", "status": "В процессе", "risk": "Средний", "priority": 3, "stage": 4},
        {"id": 2, "title": "Веб-аналитика", "status": "Готово", "risk": "Низкий", "priority": 1, "stage": 5},
    ]
    print_project_table(sample_projects)
