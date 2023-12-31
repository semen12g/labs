# Вычисляем значение факториала для введенного числа
def product(n):
    factorial = 1  # Переменная для хранения значения факториала
    
    # Вычисление факториала числа n
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

# Получить конечный результат произведения для этого факториала
def calculate(n):
    product_result = 1  # Переменная для хранения произведения в знаменателе
    
    # Вычисление произведения в знаменателе
    for i in range(2, n + 1):
        product_result *= (1 - 1 / (i * i))
    
    return product_result

n = int(input("Введите число n: "))

assert n >= 2, "n должно быть больше или равно 2"  # Проверка, что n >= 2