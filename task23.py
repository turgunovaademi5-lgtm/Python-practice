from random import randint
number = randint(1, 20)

for attempt in range(3):
	user_number = int(input('Угадай число от 1 до 20: '))
	if user_number == number:
		print('Ты угадала!')
		break
	else:
		print('Не угадала! Попробуй еще раз!')
else:
	print('Не угадала! Мое число:' , number)