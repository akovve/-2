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


def main():
    """Основная функция с дружественным интерфейсом."""
    calc = PostfixCalculator()
    print("Добро пожаловать в калькулятор постфиксных выражений!")
    print("Введите выражение в постфиксной форме (например: '3 5 + 2 *').")
    print("Для выхода введите 'exit' или 'quit'.")
    
    while True:
        user_input = input("\nВведите выражение: ").strip()
        
        if user_input.lower() in ('exit', 'quit'):
            print("До свидания!")
            break
            
        if not user_input:
            print("Ошибка: Вы не ввели выражение. Попробуйте снова.")
            continue
            
        try:
            result = calc.evaluate(user_input)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
