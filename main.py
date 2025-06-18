class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self._items = []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self._items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._items.pop()

    def peek(self):
        """Возвращает элемент с вершины стека без удаления."""
        if self.is_empty():
            raise IndexError("Попытка просмотра вершины пустого стека")
        return self._items[-1]

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self._items) == 0

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self._items)

    def clear(self):
        """Очищает стек."""
        self._items.clear()


class PostfixCalculator:
    """Калькулятор для вычисления постфиксных выражений."""

    def __init__(self):
        """Инициализация калькулятора с пустым стеком."""
        self._stack = Stack()

    def evaluate(self, expression):
        """
        Вычисляет значение постфиксного выражения.
        """
        self._stack.clear()
        tokens = expression.strip().split()
            
        if not tokens:
            raise ValueError("Пустое выражение")

        for token in tokens:
            try:
                if self._is_number(token):
                    self._stack.push(float(token))
                elif token in {'+', '-', '*', '/'}:
                    self._apply_operator(token)
                else:
                    raise ValueError(f"Недопустимый знак: '{token}'")
            except ValueError as e:
                raise ValueError(f"Ошибка обработки знака '{token}': {e}")

        if self._stack.size() != 1:
            raise ValueError("Некорректное выражение: в стеке осталось несколько значений")
        
        if token.lstrip('-').replace('.', '', 1).isdigit():
            self._stack.push(float(token))

        return self._stack.pop()

    def _apply_operator(self, operator):
        """
        Применяет оператор к двум верхним элементам стека.
        """
        try:
            if self._stack.size() < 2:
                raise ValueError("Недостаточно операндов для операции")

            right_operand = self._stack.pop()
            left_operand = self._stack.pop()

            if operator == '+':
                result = left_operand + right_operand
            elif operator == '-':
                result = left_operand - right_operand
            elif operator == '*':
                result = left_operand * right_operand
            elif operator == '/':
                if right_operand == 0:
                    raise ValueError("Деление на ноль невозможно")
                result = left_operand / right_operand
            else:
                raise ValueError(f"Неизвестный оператор: '{operator}'")

            self._stack.push(result)
        except ValueError as e:
            raise ValueError(f"Ошибка выполнения операции: {e}")

    def _is_number(self, token):
        """Проверяет, является ли токен числом."""
        try:
            float(token)
            return True
        except ValueError:
            return False


class CalculatorUI:
    """Класс для взаимодействия с пользователем."""

    def __init__(self):
        self.calculator = PostfixCalculator()

    def run(self):
        """Запускает интерактивный интерфейс калькулятора."""
        print("//==================================================//")
        print("||        КАЛЬКУЛЯТОР ПОСТФИКСНЫХ ВЫРАЖЕНИЙ         ||")
        print("||==================================================||")
        print("|| Пример ввода: 3 5 + 2 *                          ||")
        print("|| Доступные операции: + - * /                      ||")
        print("|| Для выхода введите 'exit' или 'quit' или 'выйти' ||")
        print("//==================================================//")

        while True:
            try:
                user_input = input("\nВведите выражение: ").strip()

                if user_input.lower() in {'exit', 'quit', 'выйти'}:
                    print("\nРабота программы завершена. До свидания!")
                    break

                if not user_input:
                    print("Ошибка: Пустой ввод. Пожалуйста, введите выражение.")
                    continue

                result = self.calculator.evaluate(user_input)
                print(f"Результат: {result:.2f}" if result % 1 else f"Результат: {int(result)}")

            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    ui = CalculatorUI()
    ui.run()
