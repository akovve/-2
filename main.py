class PostfixCalculator:
    """Калькулятор для постфиксных выражений (без импортов)."""

    def __init__(self):
        """Инициализация пустого стека."""
        self.stack = []

    def evaluate(self, expression: str) -> float:
        """
        Вычисляет значение выражения в постфиксной записи.

        :param expression: Строка с выражением, разделённым пробелами
        :return: Результат вычисления
        :raises ValueError: В случае ошибки синтаксиса или арифметики
        """
        self.stack.clear()
        tokens = expression.strip().split()

        for token in tokens:
            if self._is_number(token):
                self.stack.append(float(token))
            elif token in ('+', '-', '*', '/'):
                self._apply_operator(token)
            else:
                raise ValueError(f"Неизвестный символ: '{token}'")

        if len(self.stack) != 1:
            raise ValueError("Некорректное выражение: стек не пуст")

        return self.stack.pop()

    def _apply_operator(self, operator: str) -> None:
        """Выполняет операцию над двумя верхними элементами стека."""
        if len(self.stack) < 2:
            raise ValueError("Недостаточно операндов для операции")

        b = self.stack.pop()
        a = self.stack.pop()

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                raise ValueError("Деление на ноль недопустимо")
            result = a / b
        else:
            raise ValueError(f"Неизвестный оператор: '{operator}'")

        self.stack.append(result)

    def _is_number(self, token: str) -> bool:
        """Проверка, можно ли привести токен к числу."""
        try:
            float(token)
            return True
        except:
            return False


def run_tests():
    """Тестирование калькулятора с несколькими выражениями."""
    calc = PostfixCalculator()

    tests = {
        "3 5 +": 8.0,
        "10 4 -": 6.0,
        "2 3 * 4 +": 10.0,
        "20 5 /": 4.0,
        "5 1 2 + 4 * + 3 -": 14.0
    }

    for expr, expected in tests.items():
        result = calc.evaluate(expr)
        assert abs(result - expected) < 0.000001, f"Тест не пройден: {expr}"
        print(f"{expr} = {result}")

    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()
