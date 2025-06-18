class Node:
    """Узел для реализации стека на связном списке"""
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Реализация стека на связном списке"""
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        """Добавление элемента в стек"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Извлечение элемента из стека"""
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        """Просмотр верхнего элемента без извлечения"""
        if self.is_empty():
            raise IndexError("Попытка просмотра пустого стека")
        return self.top.value

    def is_empty(self):
        """Проверка на пустоту"""
        return self.top is None

    def clear(self):
        """Очистка стека"""
        self.top = None
        self.size = 0


class PostfixCalculator:
    """Калькулятор постфиксных выражений"""
    def __init__(self):
        self.stack = Stack()

    def evaluate(self, expression):
        """Вычисление постфиксного выражения"""
        self.stack.clear()
        tokens = expression.strip().split()

        for token in tokens:
            if self._is_number(token):
                self.stack.push(float(token))
            elif token in '+-*/':
                self._apply_operator(token)
            else:
                raise ValueError(f"Недопустимый токен: '{token}'")

        if self.stack.size != 1:
            raise ValueError("Некорректное выражение")

        return self.stack.pop()

    def _apply_operator(self, operator):
        """Применение оператора"""
        if self.stack.size < 2:
            raise ValueError("Недостаточно операндов")

        b = self.stack.pop()
        a = self.stack.pop()

        if operator == '+':
            self.stack.push(a + b)
        elif operator == '-':
            self.stack.push(a - b)
        elif operator == '*':
            self.stack.push(a * b)
        elif operator == '/':
            if b == 0:
                raise ValueError("Деление на ноль")
            self.stack.push(a / b)

    def _is_number(self, token):
        """Проверка, является ли токен числом"""
        try:
            float(token)
            return True
        except ValueError:
            return False


def main():
    """Интерактивный интерфейс калькулятора"""
    calc = PostfixCalculator()
    print("\n//====================================================//")
    print("||         КАЛЬКУЛЯТОР ПОСТФИКСНЫХ ВЫРАЖЕНИЙ          ||")
    print("||====================================================||")
    print("|| Пример: 3 5 + 2 * → 16                             ||")
    print("|| Доступные операции: + - * /                        ||")
    print("|| Для выхода: 'exit', 'quit', 'выйти'                ||")
    print("//====================================================//")

    while True:
        try:
            user_input = input("\nВведите выражение: ").strip()
            
            if user_input.lower() in {'exit', 'quit', 'выйти'}:
                print("\nРабота завершена. До свидания!")
                break
                
            if not user_input:
                print("Ошибка: Пустой ввод")
                continue
                
            result = calc.evaluate(user_input)
            print(f"Результат: {result:.2f}" if result % 1 else f"Результат: {int(result)}")
            
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
