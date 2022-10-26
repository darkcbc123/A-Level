# Задание 3
# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
f = open(r'C:\Users\vlmed\PycharmProjects\pythonProject3\text.txt', 'r')
for line in f:
    list_string = line.split()
    count = {}

    def lower_reg(i):
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        return count

    list(map(lower_reg, list_string))
    print(count)