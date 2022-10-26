
#Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.
import sys
f = open(r'C:\Users\vlmed\PycharmProjects\pythonProject3\txt.txt', 'r')
for line in f:
    string_list = line.split()
    integer_list = list(map(int, string_list))
    print()
    fizz, buzz, number = integer_list[:]

    i = 1
    while i <= number:
        if i % fizz == 0 and i % buzz == 0:
            print('FB', end=' ')
        elif i % fizz == 0:
            print('F', end=' ')
        elif i % buzz == 0:
            print('B', end=' ')
        else:
            print(i, end=' ')
        i += 1


f.close() # закрытие файла


