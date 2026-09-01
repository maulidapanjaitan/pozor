# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ProjectRadar
def paginate_data(data, page_size=10):
    """Compact paginated view for long lists."""
    pages = []
    for start in range(0, len(data), page_size):
        pages.append(data[start:start + page_size])
    return len(pages), pages
