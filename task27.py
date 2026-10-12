numbers = [2, 5, 8, 11, 14, 17, 20]
num1 = list(filter(lambda x: x % 2 ==0 , numbers))
num2 = list(map(lambda x: x * 3, num1))
print(num2)