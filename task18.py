fruits = ['apple' , 'banana' , 'orange' , 'apple' , 'kiwi']

# вывести весь список
print(fruits)

# вывести первый элемент
print(fruits[0])

# вывести последний элемент
print(fruits[-1])

# вывести первые 3 элемента
print(fruits[:3])

# изменить слова 'banana' на 'mango'
fruits[1] = 'mango'
print(fruits)

#добавить 'grape' в конце списка
fruits.append('grape')
print(fruits)

# удалить слова 'orange'
fruits.remove('orange')
print(fruits)

#вставить 'watermelon' на втoрую позицию
fruits.insert(2,  "watermelon")
print(fruits)

#удалить последний элемент
print(fruits.pop(-1))
print(fruits)

#посчитать, сколько раз встречаеться 'apple' в списке
print(fruits.count('apple'))

# отсортирует список
fruits.sort()
print(fruits)

#вывести каждый фрукт отдельно
for fruit in fruits:
	print(fruits)