students = {'Vanya Ivanov', 'Sveta Svetova', 'Vadim Vadimov', 'Kolya Nikolaev', 'Tanya Tanenko', 'Igor Igorev', 'Dima Dimov', 'Polyna Borysenko'}

Python = {'Kolya Nikolaev', 'Sveta Svetova', 'Vanya Ivanov', 'Igor Igorev'}
FrontEnd = {'Polyna Borysenko', 'Dima Dimov'}
FullStack = {'Tanya Tanenko', 'Dima Dimov', 'Sveta Svetova'}
Java = {'Vanya Ivanov', 'Sveta Svetova', 'Vadim Vadimov', 'Tanya Tanenko', 'Igor Igorev'}

result = []
for i in students:
    count = 0
    if i in Python:
        count += 1
    if i in FrontEnd:
        count += 1
    if i in FullStack:
        count += 1
    if i in Java: 
        count += 1
    if count >= 2:
        result.append(f'{i} >>> {count}')

print(result)

print(students - FrontEnd)

print(Python & Java)
