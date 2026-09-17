class Book:
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
	def info(self):
		print('Название: ' , self.title)
		print('Автор: ' , self.author)
		print('Страниц: ' , self.pages)
	def read(self):
		print('Я читаю книгу: ' , self.title)
book1 = Book('Дракон' , 'Александра' , 80)
book2 = Book('Рыцарь' , 'Джейн' , 93)
book1.info()
book1.read()
book2.info()
book2.read()