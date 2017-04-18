for value in range(0,2):
    print(value)
#Числовой список
numbers = list(range(1,6))
print(numbers)
#Числовой список с заданным приращением
even_numbers = list(range(2,11,2))
print(even_numbers)
#Квадраты всех чисел в диаппазоне(1,10)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
