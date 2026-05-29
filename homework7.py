def calculator_decorator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except ZeroDivisionError:
            print("Помилка: Не можна ділити на нуль!")
            return None
        except Exception as e:
            print(f"Помилка обчислення прикладу '{expression}': {e}")
            return None
    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


print("Результат 2 + 2 * 2:", calculate("2 + 2 * 2"))
print("Результат 10 / 0:", calculate("10 / 0"))
print("Результат неправильного прикладу:", calculate("2 + abc"))