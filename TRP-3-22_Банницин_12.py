# TRP-3-22, Банницин Дмитрий

# 1

# union 1.1.1

import random
import math
import re
print("""Есть 2 коробки с множеством фруктов, определить 
какие фрукты встречаются в двух коробках""")

box1 = {"apple", "orange"}
box2 = {"orange", "banana", "pear"}

print(box1.union(box2))

# union 1.1.2

print("""В городе М 3 фермы с животными, определить 
колличество видов животных на фермах""")

farm1 = {"cow", "horse"}
farm2 = {"horse", "chicken", "bool"}
farm3 = {"duck", "cat", "chicken"}

print("Answer: ", len(farm1.union(farm2).union(farm3)))

# intersection 1.2.1

print("""В городе М 3 фермы с животными, определить 
колличество видов животных которые есть на всех фермах""")

farm1 = {"cow", "horse", "chicken"}
farm2 = {"horse", "chicken", "bool"}
farm3 = {"horse", "duck", "cat", "chicken"}

print("Answer: ", len(farm1.intersection(farm2).intersection(farm3)))

# intersection 1.2.2

print("""Дано 3 множества чисел, определить какие встераются в каждом из множеств""")

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}
set3 = {5, 6, 7, 8, 9, 0}

print("Answer: ", set1.intersection(set2).intersection(set3))

# difference 1.3.1

print("""Дано 3 множества чисел, определить какие встераются только в первом множетсве""")

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}
set3 = {5, 6, 7, 8, 9, 0}

print("Answer: ", set1.difference(set2).difference(set3))

# difference 1.3.2

print("""Дано 3 множества чисел, определить какие встераются только в первом и втором множетсвах""")

set1 = {1.1, 2.1, 3.1, 4.1, 5.1, 6.1}
set2 = {3.1, 4.1, 5.2, 6.2, 7.2, 8.3}
set3 = {5.3, 6.1, 7.2, 8.1, 9.3, 0.0}

print("Answer: ", set1.union(set2).difference(set3))

# subset 1.4.1

print("""Дано 3 множества чисел, определить входит ли первое в два других""")

set1 = {3.1, 4.1, 5.2}
set2 = {3.1, 4.1, 5.2, 6.2, 7.2, 8.3}
set3 = {5.3, 6.1, 7.2, 3.1, 9.3, 5.2, 4.1}

print("Answer: ", set1.issubset(set2) and set1.issubset(set3))

# subset 1.4.2

print("""Дано 3 множества чисел, вевести множество, 
являющееся подмножеством для одного из 2х других""")

set1 = {3.1, 4.1, 5.2}
set2 = {3.1, 4.1, 5.2, 6.2, 7.2, 8.3}
set3 = {5.3, 6.1, 7.2, 3.1, 9.3, 5.2, 4.1}

if set1.issubset(set2) or set1.issubset(set3):
    print(set1)
elif set2.issubset(set1) or set2.issubset(set3):
    print(set2)
elif set3.issubset(set1) or set3.issubset(set2):
    print(set3)

# 2

print("""Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает
хотя бы один из школьников""")

schoolboy1 = {"russian", "english", "japan"}
schoolboy2 = {"turkish", "japan", "russian"}
schoolboy3 = {"russian", "english"}
schoolboy4 = {"russian", "japan", "korean"}

print("Answer: ",
      schoolboy1.intersection(schoolboy2).intersection(
          schoolboy3).intersection(schoolboy4),
      "\n", schoolboy1.union(schoolboy2).union(schoolboy3).union(schoolboy4))

# 3

print("""Во входном файле (вы можете читать данные из файла (input.txt)
записан текст. Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько
различных слов содержится в этом тексте.""")

file = open('input.txt', 'r')
words = file.read()
words = re.split(" |\n", words)
wordsSet = set(words)
wordsSet.remove('')
print(len(wordsSet))

# 4

print("""Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c':
500, 'd': 600}. Объедините их в один при помощи встроенных функций
языка Python.""")

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_3 = dictionary_1 | dictionary_2
print("Answer: ", dictionary_3)

# 5

print("""Найдите три ключа с самыми высокими значениями в словаре my_dict
= {'a':500, 'b':5874, 'c': 560, 'd':400, 'e':5874, 'f': 20}.""")

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print([i for i in list(sorted_dict.keys())[:-4:-1]])

# 6

print("""Создайте словарь, в котором ключами будут числа от 1 до 10, а
значениями эти же числа, возведенные в куб.""")

my_dict = {i: i ** 3 for i in range(1, 11)}

print(my_dict)

# 7

print("""Даны два списка одинаковой длины. Необходимо создать из них
словарь таким образом, чтобы элементы первого списка были
ключами, а элементы второго — соответственно значениями нашего
словаря.""")

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

my_dict = {list1[i]: list2[i] for i in range(len(list1))}

print(my_dict)

# 8

print("""Инвертировать словарь, т.е. поменять ключи со значениями.""")

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

my_dict = {i[1]: i[0] for i in my_dict.items()}

print(my_dict)

# 9

print("""Создайте словарь, где ключами являются числа, а значениями –
строки. Примените к нему метод items(), полученный объект
dict_items передайте в написанную вами функцию, которая создает и
возвращает новый словарь, "обратный" исходному, т. е. ключами
являются строки, а значениями – числа.""")


def invertDict(dict):
    return {i[1]: i[0] for i in dict.items()}


my_dict = {500: 'a', 5874: 'e', 560: 'c', 400: 'd', 20: 'f'}

new_dict = invertDict(my_dict)

print("Original dictionary: ", my_dict, "\nInvert dictionary: ", new_dict)

# 11

print("""Банковские счета. Некоторый банк хочет внедрить систему
управления счетами клиентов, поддерживающую следующие
операции: пополнение счета клиента; снятие денег со счета; запрос
остатка средств на счете; перевод денег между счетами клиентов;
начисление процентов всем клиентам. Необходимо реализовать
такую систему. Клиенты банка идентифицируются именами
(уникальная строка, не содержащая пробелов). Первоначально у банка
нет ни одного клиента. Как только для клиента проводится операция
пололнения, снятия или перевода денег, ему заводится счет с нулевым
балансом. Все дальнейшие операции проводятся только с этим
счетом. Сумма на счету может быть как положительной, так и
отрицательной, при этом всегда является целым числом.1""")


def deposit(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) + int(money)


def withdraw(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) - int(money)


def balance(arg):
    name = arg[0]
    if name in bank:
        print(bank[name])
    else:
        print('ERROR')


def transfer(arg):
    name_1, name_2, money = arg
    withdraw((name_1, money))
    deposit((name_2, money))


def income(arg):
    percent = int(arg[0])
    for name, balanse in bank.items():
        if balanse > 0:
            bank[name] = bank.get(name) + balanse * percent//100


bank = {}
bank_fun = {
    'DEPOSIT': deposit, 'WITHDRAW': withdraw,
    'BALANCE': balance, 'TRANSFER': transfer,
                        'INCOME': income
}

for _ in range(int(input('operations count: '))):
    data = input("Enter 'OPERATION name money'").split()
    fun_name = data[0]
    arg = data[1:]
    bank_fun[fun_name](arg)

# 12

print("""Создать базу данных на основе словаря, в котором хранится
информация по студентам 2-х групп (ФИО, адрес, телефон), а также
их оценки по 3-м предметам (Алгоритмизация и программирование,
Информатика, Физкультура, всего по 4 оценки в каждом предмете,
для каждого студента). Вывести на печать в виде таблицы оценки
студентов групп, среднюю успеваемость студентов в группе,
среднюю успеваемость по группе в целом. Оформить данные в виде
отчета.
""")

group_number1 = "g1"
group_number2 = "g2"

names = [
    "Мухин Савелий Ильяович",
    "Костин Эдуард Мэлорович",
    "Потапов Василий Мартынович",
    "Елисеев Лукьян Тарасович",
    "Панфилов Аверьян Гордеевич",
    "Егоров Даниил Ильяович",
    "Лаврентьев Мартын Протасьевич",
    "Шашков Карл Оскарович",
    "Владимиров Ким Улебович",
    "Гурьев Макар Наумович",
    "Пестов Альфред Эдуардович",
    "Стрелков Гурий Гордеевич",
    "Орлов Азарий Иосифович",
    "Субботин Бенедикт Вениаминович",
    "Романов Артем Кириллович",
    "Сысоев Панкратий Олегович",
    "Кузнецов Гарри Онисимович",
    "Соколов Осип Аркадьевич",
    "Гурьев Корней Яковович",
    "Белоусов Филипп Антонович"
]

addresses = [
    "383404, Кировская область, город Орехово-Зуево, наб. Ладыгина, 38",
    "025744, Калининградская область, город Шатура, въезд Балканская, 40",
    "688894, Новосибирская область, город Красногорск, бульвар Ладыгина, 72",
    "294463, Томская область, город Красногорск, проезд Балканская, 76",
    "618380, Калужская область, город Лотошино, пл. Будапештсткая, 05",
    "456465, Псковская область, город Егорьевск, спуск Космонавтов, 57",
    "277250, Ленинградская область, город Раменское, пл. Домодедовская, 50",
    "250565, Архангельская область, город Ступино, спуск Балканская, 54",
    "729325, Калужская область, город Волоколамск, наб. Чехова, 06",
    "778124, Ивановская область, город Орехово-Зуево, въезд Домодедовская, 90",
    "271911, Кемеровская область, город Дорохово, въезд Гагарина, 99",
    "930265, Томская область, город Чехов, наб. Чехова, 23",
    "849695, Мурманская область, город Егорьевск, ул. Славы, 76",
    "055391, Воронежская область, город Одинцово, проезд Гоголя, 52",
    "013421, Новосибирская область, город Дорохово, наб. Славы, 04",
    "424702, Оренбургская область, город Лотошино, пер. Бухарестская, 16",
    "843688, Ярославская область, город Павловский Посад, пр. Чехова, 23",
    "533725, Пензенская область, город Лотошино, ул. Ломоносова, 77",
    "246125, Новгородская область, город Павловский Посад, шоссе Сталина, 54",
    "181899, Ярославская область, город Клин, пр. Бухарестская, 09"
]


def getRandMarks():
    return [random.randrange(2, 5) for _ in range(4)]


def getAvgMarks(group):

    avgAIP = 0
    avgINF = 0
    avgPE = 0

    for student in group:
        for mark in student['marks']['AIP']:
            avgAIP += mark
        for mark in student['marks']['INF']:
            avgINF += mark
        for mark in student['marks']['PE']:
            avgPE += mark

    return {'AIP': avgAIP/40, 'INF': avgINF/40, 'PE': avgPE/40}


group = {}
students1 = [{'name': names[i], 'address':addresses[i], 'phone':random.randrange(
    89000000000, 89999999999), 'marks':{'AIP': getRandMarks(),
                                        "INF": getRandMarks(),
                                        "PE": getRandMarks()}}
    for i in range(10)]

students2 = [{'name': names[10+i], 'address':addresses[10+i], 'phone':random.randrange(
    89000000000, 89999999999), 'marks':{'AIP': getRandMarks(),
                                        "INF": getRandMarks(),
                                        "PE": getRandMarks()}}
    for i in range(10)]

group[group_number1] = students1
group[group_number2] = students2

for key in group.keys():
    print(key, getAvgMarks(group[key]))
    for student in group[key]:
        print('\t', student['name'], 'AIP ', end="")
        for mark in student['marks']['AIP']:
            print(mark, end="")
        print(' INF ', end="")
        for mark in student['marks']['INF']:
            print(mark, end="")
        print(' PE ', end="")
        for mark in student['marks']['PE']:
            print(mark, end="")
        print()

# 13
print("""Описать процедуру ShiftRight(N), выполняющую правый циклический
сдвиг числа N: значение N1 переходит в N2, значение N2 — в N3,
значение Nk — в N1 (N —целое, являющиеся одновременно входным
и выходным). С помощью этой процедуры выполнить правый
циклический сдвиг для трех наборов 3, 5, 10 значных чисел.
""")

N = int(input('N = '))


def ShiftRight(num):
    num = int(str(num)[-1]+str(num)[:-1])
    return num


print(ShiftRight(N))

# 14

print("""Описать процедуру ShiftLeft3(A, B, C), выполняющую левый
циклический сдвиг: Описать процедуру ShiftLeft3(N), выполняющую
левый циклический сдвиг: значение N1 переходит в Nk, значение N3 —
в N2, значение Nk — в Nk-1 (N —целое, являющиеся одновременно
входным и выходным). С помощью этой процедуры выполнить
правый циклический сдвиг для трех наборов 4, 6, 11 значных чисел.
""")

N = int(input('N = '))


def ShiftRight(num):
    num = int(str(num)[1:]+str(num)[0])
    return num


print(ShiftRight(N))

# 15

print("""Описать функцию IsSquare(K) логического типа, возвращающую
True, если целый параметр K (> 0) является квадратом некоторого
целого числа, и False в противном случае. С ее помощью найти
количество квадратов в наборе из 5 целых положительных чисел.
""")

numbers = [4, 8, 3, 8, 9]


def IsSquare(num):
    if math.sqrt(num)**2 == num:
        return True
    return False


for num in numbers:
    print(IsSquare(num))

# 16

print("""Описать функцию где Робот может перемещаться в четырех
направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток)
и принимать три цифровые команды: 0 — продолжать движение, 1 —
поворот налево, –1 — поворот направо. Дан символ C — исходное
направление робота и целое число N — посланная ему команда
(вводится в основной программе). Вывести направление робота после
выполнения k-полученных команд
""")


def CompleteCommand(C, command):
    turn = (4 + (int(C) + int(command))) % 4
    return turn


turns = {0: "С", 1: "З", 2: "Ю", 3: "В"}

k = input("k = ")
C = list(turns.keys())[list(turns.values()).index(input('C = '))]
for i in range(int(k)):
    N = input('N: ')
    C = CompleteCommand(C, N)

print(turns[C])
