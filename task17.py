text = "Python is a very interesting programming language"

# 1. Первый символ
print(text[0])

# 2. Последний символ
print(text[-1])

# 3. Первые 6 символов
print(text[0:7:1])

# 4. Слово interesting
print(text[17:28])

# 5. Верхний регистр
print(text.upper())

# 6. Нижний регистр
print(text.lower())

# 7. Сколько раз встречается i
print(text.count("i"))

# 8. Позиция слова programming
print(text.find("programming"))

# 9. Позиция последней буквы i
print(text.rfind("i"))

# 10. Замена Python на Java
print(text.replace("Python", "Java"))

# 11. Длина строки
print(len(text))

# 12. Повторение Python 3 раза
print("Python " * 3)