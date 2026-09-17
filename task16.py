class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade
	def info(self):
		print('Меня зовут' , self.name)
		print('Мне' , self.age, 'лет')
		print('Я учусь в' , self.grade, 'классе')
	def study(self):
		print(self.name, 'сейчас учится')
student1 = Student('Аня' , 17, 10)
student2 = Student('Джек' , 15, 8)
student1.info()
student1.study()
student2.info()
student2.study()