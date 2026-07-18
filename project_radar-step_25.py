# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ProjectRadar
def parse_date(date_str):
    """Парсинг дат с понятными сообщениями об ошибках."""
    formats = ["%Y-%m-%d", "%d.%m.%yyyy", "%d %B %Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except (ValueError, TypeError):
            continue
    raise ValueError(f"Некорректная дата: '{date_str}'. Используйте формат YYYY-MM-DD или DD.MM.YYYY")

def validate_date_range(start_str, end_str):
    """Проверка диапазона дат с понятными сообщениями об ошибках."""
    try:
        start = parse_date(start_str)
        end = parse_date(end_str)
        if start > end:
            raise ValueError(f"Дата начала ({start_str}) должна быть раньше даты конца ({end_str})")
        return (start, end)
    except ValueError as e:
        print(f"[Ошибка] {e}")
        return None

def format_date(date_obj):
    """Форматирование даты в читаемый вид."""
    if date_obj is None:
        return "Не указана"
    return date_obj.strftime("%d.%m.%Y")

# Пример использования
try:
    start_date, end_date = validate_date_range("2024-01-15", "2024-06-30")
    if start_date and end_date:
        print(f"Диапазон дат: {format_date(start_date)} - {format_date(end_date)}")
except Exception as e:
    print(f"[Критическая ошибка] Не удалось обработать даты: {e}")
