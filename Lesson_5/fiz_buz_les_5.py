#Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.
import sys

f = open(r'C:\Users\vlmed\PycharmProjects\pythonProject3\txt.txt', 'r')
final_res = []
for line in f:
    string_list = line.split()
    integer_list = list(map(int, string_list))

    result = []
    number = (list(range(1, int(integer_list[2] + 1))))

    def count_fb(number):
        if number % integer_list[0] == 0 and number % integer_list[1] == 0:
            result.append('FB')
        elif number % integer_list[0] == 0:
            result.append('F')
        elif number % integer_list[1] == 0:
            result.append('B')
        else:
            result.append(str(number))
        return result
    final_res.append(result)
    list(map(count_fb, number))

with open(r'C:\Users\vlmed\PycharmProjects\pythonProject3\write.txt', "w") as file:
    for listik in final_res:
        file.write(str(listik) + '\n')
