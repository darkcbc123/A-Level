#Написать программу, которая выводит саму себя задом наперед

import sys
filename = sys.argv[0]
# далее открываем файл на чтение (опция 'r')
f = open(filename, 'r') # в файле теперь file descriptor
for line in f: # для каждой строки в файле
	print(line[::-1])
f.close() # закрытие файла