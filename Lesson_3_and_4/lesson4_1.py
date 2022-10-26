#Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.
import sys
final_res = []


f = open(r'C:\Users\vlmed\PycharmProjects\pythonProject3\txt.txt', 'r')
for line in f:

    string_list = line.split()
    integer_list = list(map(int, string_list))

    fizz, buzz, number = integer_list[:]
    result = []

    for i in range(1, number + 1):
        if i % fizz == 0 and i % buzz == 0:
            result.append('FB')
        elif i % fizz == 0:
            result.append('F')
        elif i % buzz == 0:
            result.append('B')
        else:
            result.append(str(i))
    final_res.append(' '.join(result))


with open(r'C:\Users\vlmed\PycharmProjects\pythonProject3\write.txt', "w") as file:
    for list in final_res:
        file.write(list + '\n')