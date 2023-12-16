import y178
from array import array # Импортируем модуль для создания массива
# проверяет функцию проверяет функцию c на четырех разных массивах
def test():
    assert y178.count_odd_numbers(array('L', [1, 2, 3, 4, 5])) == 3
    assert y178.count_odd_numbers(array('L', [10, 20, 30])) == 0
    assert y178.count_odd_numbers(array('L', [5, 5, 5, 5, 5, 5])) == 6
    assert y178.count_odd_numbers(array('L', [1, 2, 3])) == 2
    
n = int(input('Введите n: ')) # Вводим длину массива
# Получаем массив натуральных чисел от 1 до 100
my_arr = y178.make_array(n) # Создаем массив из случайных натуральных чисел
count = y178.count_odd_numbers(my_arr)
#count = 0 # Количество нечётных чисел

#for i in range(n):
  #  k = my_arr[i] # Берем очередной элемент массива
 #   if y178.is_odd(k): # Если число нечётное
   #     count += 1 # Увеличиваем счетчик на 1
#print(k, y178.is_odd(k)) # Тестовый вывод 
print('Количество нечётных чисел в массиве: ', count) # Выводим текущий элемент и его нечётность104
