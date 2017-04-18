motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Изменение элемента списка
motorcycles[0] = 'ducati'
print(motorcycles)
#Добавление элемента
motorcycles.append('honda')
print(motorcycles)
#Вставка элемента в нужную позицию
motorcycles.insert(0, 'ural')
print(motorcycles)
#Удаление элементов
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)
