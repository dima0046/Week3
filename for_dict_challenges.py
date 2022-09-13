from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???

lst = Counter(map(lambda student: student['first_name'], students))

for name in lst:
    print(f'{name}: {lst[name]}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???

lst = Counter(map(lambda student: student['first_name'], students))
max_val = max(lst.values())

for k in lst.items():
    if k[1] == max_val:
        print(f'Most popular name is {k[0]} ({max_val} times).')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
i = 1
for students in school_students:

    lst = Counter(map(lambda student: student['first_name'], students))
    max_val = max(lst.values())

    for k in lst.items():
        if k[1] == max_val:
            print(f'Most popular name in class {i} is {k[0]} ({max_val} times).')
            i += 1

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
girls = 0
boys = 0

keyslist = [key for key in is_male]
for classes in school:
    class_name = classes['class']
    for students in classes['students']:
        for key in keyslist:
            if students['first_name'] == key and is_male[students['first_name']] == False:
                girls += 1
            if students['first_name'] == key and is_male[students['first_name']] == True:
                boys += 1
    print(f'Class {class_name}: girls - {girls}, boys - {boys}')
    girls = 0
    boys = 0

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

classlist = []
classes_genders = {}

keyslist = [key for key in is_male]

#Собираем словарь учеников
for classes in school:
    
    girls = 0
    boys = 0
    
    #Смотрим сколько мальчиков и девочек в классе
    for students in classes['students']:
        for key in keyslist:
            if students['first_name'] == key and is_male[students['first_name']] == False:
                girls += 1
            if students['first_name'] == key and is_male[students['first_name']] == True:
                boys += 1
    
    #добавляем количество девочек и мальчиков в классе
    class_name = classes['class']

    classes_genders['class'] = class_name
    classes_genders['girls'] = girls
    classes_genders['boys'] = boys
    
    girls = 0
    boys = 0
    classlist.append(classes_genders)
    classes_genders={}

i=0
x=0
for items in classlist:
    if items['girls'] > i:
        i = items['girls']
        cls =  items['class']
        print(f'Most girls in the class {cls}')
    if items['boys'] > x:
        x = items['boys']
        cls =  items['class']
        print(f'Most boys in the class {cls}')
