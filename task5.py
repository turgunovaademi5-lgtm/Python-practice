age = int(input('Введите ваш возраст: '))
has_ticket = input('У вас есть билет? (да/нет): ')
if age>=18 and has_ticket == 'да':
	print('Добра пожаловать!')
elif age>=18 and has_ticket == 'нет':
	print('У вас нет билета')
elif age<18:
	print('Вход только для совершеннолетних')
else:
	print('Некорректный ответ')