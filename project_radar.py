# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ProjectRadar
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

# --- Базовая структура проекта ProjectRadar ---

class MiniProject:
    def __init__(self, name: str, risk_level: int, priority: int, stages: List[str]):
        self.name = name
        self.risk_level = risk_level  # 1-5
        self.priority = priority       # 1-5 (1 - высокий)
        self.stages = stages           # Список этапов
        self.next_action = None
        self.status = "planning"

    def get_next_action(self) -> str:
        if not self.stages:
            return "Нет запланированных действий."
        current_idx = 0
        for i, stage in enumerate(self.stages):
            if stage == "completed":
                current_idx += 1
        if current_idx < len(self.stages) - 1:
            return f"Выполнить этап: {self.stages[current_idx + 1]}"
        return "Проект завершен."

class ProjectRadarApp:
    def __init__(self):
        self.projects: List[MiniProject] = []
        self.load_demo_data()

    def load_demo_data(self):
        demo_projects = [
            MiniProject("Редизайн сайта", 3, 2, ["Анализ ТЗ", "Прототип", "Верстка", "Тесты"]),
            MiniProject("Настройка CI/CD", 2, 1, ["Выбор инструментов", "Скрипты сборки", "Интеграция"]),
            MiniProject("Исследование рынка", 4, 3, ["Сбор данных", "Анализ конкурентов", "Отчет"]),
        ]
        self.projects = demo_projects

    def print_dashboard(self):
        print(f"\n=== ProjectRadar: {datetime.now().strftime('%d.%m.%Y %H:%M')} ===")
        if not self.projects:
            print("Нет активных проектов.")
            return
        
        for p in sorted(self.projects, key=lambda x: (x.priority, -x.risk_level)):
            print(f"\n[Приоритет {p.priority}] Риск: {p.risk_level}/5 | {p.name}")
            print(f"  Статус: {p.status}")
            print(f"  Следующее действие: {p.get_next_action()}")

    def add_project(self, name: str, risk: int, priority: int, stages: List[str]):
        p = MiniProject(name, risk, priority, stages)
        self.projects.append(p)
        return p

# --- Точка входа и демонстрация ---

if __name__ == "__main__":
    app = ProjectRadarApp()
    app.print_dashboard()
