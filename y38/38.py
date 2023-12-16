print("Введите x ")
x = float(input())
print("Введите y ")
y = float(input())
if x > y:
    z = x - y
else:
    z = y - x + 1
# Проверяем, что функция правильно вычисляет значение z, если x > y
x = 10
y = 5
assert (x - y) == 5
# Проверяем, что функция правильно вычисляет значение z, если x <= y
x = 5
y = 10
assert (y - x + 1) == 6
print("Ответ  ")
print(z)
