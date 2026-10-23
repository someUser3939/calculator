import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class Calculator:
    def __init__(self, number_1: int, number_2: int) -> None:
        self.number_1 = number_1
        self.number_2 = number_2
        logging.info(f"Создан калькулятор для чисел: {self.number_1} и {self.number_2}")

    def __str__(self) -> str:
        return f"Калькулятор [{self.number_1}, {self.number_2}]"

    def calculate(self, operation: str) -> float:
        """Выполняет указанную математическую операцию"""
        logging.info(f"Начало операции '{operation}'")
        
        try:
            if operation in ('+', 'plus'):
                result = self.number_1 + self.number_2
            elif operation == '-':
                result = self.number_1 - self.number_2
            elif operation == '*':
                result = self.number_1 * self.number_2
            elif operation == '/':
                result = self.number_1 / self.number_2  # Ошибка ZeroDivisionError поймается ниже
            else:
                raise ValueError(f"Неизвестная операция: {operation}")
            
            logging.info(f"Операция завершена. Результат: {result}")
            return float(result)

        except ZeroDivisionError:
            logging.error("Критическая ошибка: Попытка деления на ноль!")
            raise
        except ValueError as ve:
            logging.error(f"Ошибка валидации: {ve}")
            raise
        finally:
            logging.info("Блок вычислений отработал")


# --- ПРАВИЛЬНАЯ ТОЧКА ВХОДА В ПРОГРАММУ ---
if __name__ == "__main__":
    print("--- Старт программы (прямой запуск файла) ---")
    
    # 1. Тест с правильными данными
    try:
        calc1 = Calculator(10, 5)
        print(calc1)
        
        res_add = calc1.calculate('plus')
        print(f"Результат сложения: {res_add}\n")
        
    except Exception as e:
        print(f"Произошла ошибка в основном потоке: {e}")

    # 2. Тест на ошибку (деление на ноль)
    print("--- Тестируем деление на ноль ---")
    try:
        calc2 = Calculator(10, 0)
        res_div = calc2.calculate('/')
    except ZeroDivisionError:
        print("Перехватили деление на ноль в блоке проверки. Программа не упала!\n")

    # 3. Тест на неверный знак
    print("--- Тестируем неверный знак операции ---")
    try:
        calc1.calculate('неизвестный_знак')
    except ValueError:
        print("Перехватили ошибку неверного знака. Всё под контролем.")
