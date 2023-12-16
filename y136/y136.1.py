import y136
# проверяет функцию computeF на четырех разных списках 
def test():
 assert y136.computeF([1, 2, 3, 4, 5]) == 450
 assert y136.computeF([10, 20, 30]) == 54000 
 assert y136.computeF([5, 5, 5, 5, 5, 5]) == 1080
 assert y136.computeF([1, 2, 3]) == 72
       
#n = int(input("Введите N = ").strip())
#arr = y136.fillArray(n)
#print("Ответ", y136.computeF(arr)) # Выводим результат вычислений на экран    формат вывод
n = int(input("Введите N = ").strip())
arr = y136.fillArray(n)
result = y136.computeF(arr)
print(f"Ответ: {result:.2f}") # Выводим результат вычислений на экран с двумя знаками после запятой