class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Деление на ноль!")
            return None
        return a / b

class Main:
    @staticmethod
    def main():
        calculator = Calculator()
        pairs_count = int(input("Введите количество пар чисел: "))
        results = []

        for i in range(pairs_count):
            print(f"\nВведите пару чисел {i + 1}:")
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))

            sum_ = calculator.add(a, b)
            difference = calculator.subtract(a, b)
            product = calculator.multiply(a, b)
            quotient = calculator.divide(a, b)

            results.append((sum_, difference, product, quotient))

        print("\nРезультаты:")
        for i, (sum_, difference, product, quotient) in enumerate(results, start=1):
            print(f"\nРезультаты для пары чисел {i}:")
            print("Сумма чисел:", sum_)
            print("Разность чисел:", difference)
            print("Произведение чисел:", product)
            print("Частное чисел:", quotient)

if __name__ == "__main__":
    Main.main()
