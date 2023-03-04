#TRP-3-22, Банницин Дмитрий

#1.2
print("Составить алгоритм вычисления периметра квадрата, если известна его сторона , сторона квадрата вводится пользователем ")
per = int(input("x = "))**2
print("Answer: ", per)

#1.3
import math
print("Составить алгоритм вычисления длины окружности, если известен ее радиус")
r = int(input("r = "))
print("Answer: ", r * 2 * math.pi)

#1.4
import math
print("Составить алгоритм вычисления периметра прямоугольного треугольника, если известны его катеты , катеты вводятся пользователем")
a = int(input("a = "))
b = int(input("b = "))
print("Answer: ", a + b + math.sqrt(a**2 + b**2))

#1.5
import math
print("Составить алгоритм вычисления площади кольца, если известны радиуса внешней и внутренней окружности , радиусы окружностей вводятся пользователем")
r_in = int(input("r внутренней = "))
r_out = int(input("r внешней = "))
print("Answer: ", r_out**2 * math.pi - r_in**2 * math.pi)

#1.6
import math
print("Составить алгоритм вычисления периметра равнобедренной трапеции, если известны ее основания и высота , пользователем.")
a = int(input("a = "))
b = int(input("b = "))
h = int(input("h = "))
print("Answer: ", a + b + 2 * math.sqrt(h ** 2 + (a-b)**2 / 4))

#1.7
print("Дано число n (вводится пользователем). С начала суток прошло n минут. " 
"Определите, сколько часов и минут будут показывать электронные часы в этот момент. "
"Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). "
"Учтите, что число n может быть больше, чем количество минут в сутках.")
n = int(input("n = "))
hours = int(n / 60)
days = int(hours / 24)
print("Answer: ", "days: ", days, " hours: ", hours % 24, " minutes: ", n % 60)

#2.2
print("Составить алгоритм решения задачи для определения меньшего из трех целых чисел (не используя функцию min или max).")
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
n3 = int(input("n3 = "))

if n1 < n2 :
    if n1 < n3 :
        print("Answer: ", n1)
    else:
        print("Answer: ", n3)
else:
    if n2 < n3 :
        print("Answer: ", n2)
    else:
        print("Answer: ", n3)

#2.3
print("Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого, не используя функцию min или max). ")
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
n3 = int(input("n3 = "))

if n1 < n2 :
    if n1 > n3 :
        print("Answer: ", n1)
    if n2 < n3:
        print("Answer: ", n2)
else:
    if n1 < n3 :
        print("Answer: ", n1)
    if n2 < n3 :
        print("Answer: ", n3)

#2.4
print("Из двух случайных чисел (вводит пользователь), одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число. ")
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

if n1 % 2 == 0 :
    print("Answer: ", n2)
else:
    print("Answer: ", n1)

#2.5
print("Дано трехзначное натуральное число n. Имеется ли в нем цифра 1? ")

if input().find("1") == -1 :
    print("Answer: ", False)
else:
    print("Answer: ", True)

    
#2.6
print("Дано трехзначное натуральное число. Вычислить произведение ненулевых цифр этого числа. ")

number = input("number = ")
multiply = 1
for n in number:
    if n != '0' :
        multiply = multiply * int(n)
print("Answer: ", multiply)

#2.7
import math
print("Составить алгоритм решения задачи для определения большей площади, если известны радиус круга и сторона квадрата.")

circle_square = int(input("radius = "))**2 * math.pi 
square = int(input("side = "))**2

if circle_square > square :
    print("Answer: ", circle_square)
else :
    print("Answer: ", square)

#2.8
print("Для данного x вычислить значение функции:")

x = int(input("x = "))

if x < -1 :
    print("Answer: ", 1/(x**2))
elif x < 2 :
    print("Answer: ", x**2)
else :
    print("Answer: ", 4)

#2.9
import math
print("Даны действительные числа x, y вычислите u = 3z^2 - 2z + 5")

x = int(input("x = "))
y = int(input("y = "))

if x + y < 2 :
    z = math.sqrt(x**2 + y**2)
elif x + y == 3 | x + y == 8:
    z = 2 * x * y
elif x + y >= 10 :
    z = x - y
else :
    z = 2 * x + 3 * y

print("Answer: u = ", 3 * z**2 - 2 * z + 5) 

#2.10
print("Составить алгоритм вывода названия дня недели по его порядковому номеру" 
"(1 – понедельник, 2 – вторник, 3 – среда, 4 – четверг, 5 – пятница, 6 – суббота"
", 7 – воскресенье, проверка вхождения числа в диапазон приветствуется).")

x = int(input("x = "))

if x == 1:
    print("Answer: понедельник") 
if x == 2:
    print("Answer: вторник") 
if x == 3:
    print("Answer: среда") 
if x == 4:
    print("Answer: четверг")
if x == 5:
    print("Answer: пятница") 
if x == 6:
    print("Answer: суббота") 
if x == 7:
    print("Answer: воскресенье") 

#2.11
print("Определить четверть координатной плоскости, которой принадлежит точка. Координаты точки ввести с клавиатуры.")

x = int(input("x = "))
y = int(input("y = "))

if x > 0:
    if y > 0:
        print("Answer: 1")
    else:
        print("Answer: 2")
elif y > 0:
    print("Answer: 3")
else:
    print("Answer: 4")

#2.12
print("Даны целые числа m, n. Если числа не равны," 
"то заменить каждое из них одним и тем же числом," 
"равным большему из исходных, а если равны, то заменить числа нулями. ")

m = int(input("m = "))
n = int(input("n = "))

if m == n:
    m = 0
    n = 0
elif m > n:
    n = m
else:
    m = n

print("Answer: m =", m, "n =", n)