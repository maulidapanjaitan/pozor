# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ProjectRadar
import re
from collections import defaultdict

def split_large_functions(source):
    """
    Разбивает крупные функции (>40 строк) на под-функции, сохраняя публичный API.
    """
    lines = source.split('\n')
    functions = []
    current_func = []
    func_name = None
    func_start = 0

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('def ') and func_name is None:
            func_name = stripped.split('(')[0].split('def ')[-1]
            current_func = [line]
            func_start = i
        elif stripped.startswith('def ') and func_name is not None and i - func_start > 40:
            functions.append((func_name, '\n'.join(current_func), func_start))
            current_func = [line]
            func_name = stripped.split('(')[0].split('def ')[-1]
            func_start = i
        else:
            current_func.append(line)

    if current_func:
        functions.append((func_name, '\n'.join(current_func), func_start))

    return functions
