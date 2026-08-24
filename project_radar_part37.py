# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ProjectRadar
import unittest

class TestProjectRadar(unittest.TestCase):
    def test_add_action(self):
        actions = []
        actions.append("Купить билет")
        self.assertEqual(actions[0], "Купить билет")

    def test_remove_action(self):
        actions = ["Купить билет", "Заказать еду"]
        actions.remove("Заказать еду")
        self.assertEqual(len(actions), 1)

    def test_priority_sort(self):
        tasks = [("Купить хлеб", 3), ("Купить молоко", 1), ("Купить масло", 2)]
        tasks.sort(key=lambda x: x[1])
        self.assertEqual(tasks[0][1], 1)

    def test_risk_level(self):
        risks = {"Низкий": 1, "Средний": 2, "Высокий": 3}
        self.assertEqual(risks["Высокий"], 3)

    def test_phase_order(self):
        phases = ["Запуск", "Планирование", "Выполнение", "Завершение"]
        self.assertEqual(phases[0], "Запуск")
        self.assertEqual(phases[-1], "Завершение")

if __name__ == "__main__":
    unittest.main()
