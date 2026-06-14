# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ProjectRadar
def edit_record(record_id, new_data):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return
    for key, value in new_data.items():
        if key in record_fields and key != 'id':
            records[record_id][key] = value
    else:
        print("Неизвестное поле для редактирования.")

def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        print(f"Запись с ID {record_id} удалена.")
    else:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
