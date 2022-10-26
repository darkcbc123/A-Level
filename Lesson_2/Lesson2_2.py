# Второй уровень ("if-elif-else"):
# Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры.

print('Привет, сегодня идем в поход. Давай убедимся, что ты ничего не забыл. ')

sleep_tool = input('Напиши, где ты будешь спать - ').lower()
sleep_result = ''
if sleep_tool == 'палатка':
    sleep_result = 'Да'
    print('Отлично')
elif sleep_tool == 'мешок':
    print('Отлично')
    sleep_result = 'No'
else:
  print('Мда, какой-то ты неподготовленный')

fire = str.lower(input('А есть чем разжигать костер? - '))

list_of_fire_equip = ['спички', 'дрова', 'угли', 'жидкость для розжига', 'ветки']
fire_eq_check = ''
if fire in list_of_fire_equip:
    fire_eq_check = 'Yes'
    print('Молодец!')
elif fire not in list_of_fire_equip:
    fire_eq_check = 'No'
    print('ОЙ-ой')

food = str.lower(input('Еду не забыл? '))
food_check = ''
if food == 'нет':
    food_check = 'Yes'
    print('Ништяк')
elif food == 'не':
    food_check = 'Yes'
    print('Ништяк')
elif food == 'забыл':
    food_check = 'No'
    print('Идиот!')
elif food == 'да':
    food_check = 'No'
    print('Идиот!')

print('Подведем итог')
print(f'Место для сна {sleep_result}')
print(f'Костер {fire_eq_check}')
print(f'Костер {food_check}')



