#Банкомат выдает сумму максимально возможными купюрами

summa = int(input('Введите сумму для снятия '))
list_of_banknotes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for banknotes in list_of_banknotes:
    count = 0
    while summa >= banknotes:
        summa = summa - banknotes
        count += 1
    if count >= 1:
        print(f'{count} по {banknotes} грн')
