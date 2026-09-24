book = {
         'title' : 'Harry Potter' ,
         'author' : 'J.K. Rowling' ,
         'year' : 1997 ,
         'genre' : 'fantasy'    
}

#вывести весь список
print(book)

#вывести название книги
print(book['title']) 

#вывести автор
print(book['author'])

 #измени год 
book['year'] =  1998
print(book)

#добавь новый ключ 'pages'
book['pages'] = 223
print(book)

#удали 'genre'
del book['genre']
print(book)