import re
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    pattern = r' +\d+\.?\d+ +'       # Шаблон для пошуку співпадінь
    matches = re.findall(pattern, text)  # Знаходимо всі числа відповідно до шаблону
    for match in matches:
        yield float(match)               # Повертаємо кожне число

def sum_profit(text: str, generator):
    total_salary = 0
    for number in generator(text):       # Отримуємо значення з генератора
        total_salary += number           # Сумуєм між собою
    return total_salary                  # Повертаєм значення суми

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
