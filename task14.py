num = int(input('Введите число: '))
def check_number(num):
		if num > 0:
			print('Положительное')
		elif num < 0:
			print('Отрицательное')
		else:
			print('Ноль')
check_number(num)