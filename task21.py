file = open('Note.txt', 'r')
text = file.read()
print(text)
file.close()

file = open('Note.txt', 'w')
file.write('\nNew line!')
file.close()

print('Hello Python')