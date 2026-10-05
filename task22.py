try:
	num1 = float(input('Введите первое число: '))
	num2 = float(input('Введите второе число: '))
	operation = input('Введите операцию: ')
	
	if operation == '+':
		result = num1 + num2
	elif operation == '-':
		result = num1 - num2
	elif operation == '*':
		result = num1 * num2
	elif operation == '/':
		result = num1 / num2
	else:
		raise ValueError('Неизвестная операция')
	
	print('Результат: ', result)
	
except ValueError as e:
	print(e)
except ZeroDivisionError:
	print('Делить на ноль нельза')
finally:
	print('Программа завершенна')