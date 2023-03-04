# TRP-3-22, Банницин Дмитрий

# 3.3
print("Составить алгоритм вывода таблицы перевода перевода 1, 2, ... 20"
      "долларов США в рубли по текущему курсу(значение курса вводится"
      "пользователем, ответ выдается столбцом, например, 1 $=65 руб.). ")
print("Answer:")
for n in range(1, 21, 1):
    print(n, "$ =", n * 73)

# 3.4
print("Составить таблицу(для разделения строк таблицы использовать знак"
      "подчеркивания ‘_‘, а для разделения столбцов таблицы знак"
      "вертикальной полоски ‘|‘) вывода стоимости 2, 3, …, 10 кг конфет(цена"
      "1 кг конфет вводится пользователем).")
price = int(input("price = "))
print("Answer:")

for n in range(2, 11, 1):
    print(n, "кг\t|", n * price, "руб\t|", "\n-------------------------")

# 3.5
print(" Найти произведение ста первых целых чисел.")
print("Answer:")
multiply = 1

for n in range(2, 101, 1):
    multiply = multiply * n
print(multiply)

# 3.6
print("Составить алгоритм нахождения среднего арифметического всех целых"
      "чисел от 1 до 100.")
print("Answer:")
sum = 0

for n in range(1, 101, 1):
    sum = sum + n
print(sum / 100)

# 3.7
print("Определить сумму всех нечетных чисел от 1 до 99")
print("Answer:")
sum = 0

for n in range(1, 100, 1):
    if n % 2 == 1:
        sum = sum + n
print(sum)

# 3.8
print("Дано натуральное число n и k. Вычислите сумму")
n = int(input("n = "))
sum = 0
for k in range(1, n+1, 1):
    sum = sum + 1/k**5
print("Answer:")
print(sum)

# 3.9
print("Дано натуральное число n и k. Составьте алгоритм для вычисления"
      "суммы")
n = int(input("n = "))
sum = 0
for k in range(1, n+1, 1):
    sum = sum + (2 * k - 1) / (k + 1)
print("Answer:")
print(sum)

# 3.10
print("Дано натуральное число n и k."
      "Вычислите произведение n множителей")
n = int(input("n = "))
multiply = 1
for k in range(1, n + 1, 1):
    multiply = multiply * (1 / k + 1)
print("Answer:")
print(multiply)

# 4.2
print("Даны два целых числа A и B(A < B). Составить алгоритм вывода всех"
      "целых чисел, расположенных между данными числами(не включая"
      "сами эти числа), в порядке их убывания.")
A = int(input("A = "))
B = int(input("B = "))
print("Answer:")
while A < B-1:
    print(A+1)
    A += 1

# 4.4
print("Дано натуральное число N. Составить алгоритм получения всех чисел,"
      "меньше N.")
N = int(input("N = "))
k = 0
print("Answer:")
while k < N:
    print(k)
    k += 1

# 4.5
print("Дано число n. Составить алгоритм поиска первого натурального числа,"
      "квадрат которого больше n.")
N = int(input("N = "))
n = 0
print("Answer:")
while n < N:
    if n**2 > N:
        print(k)
        break
    n += 1

# 4.6
print("Дано натуральное число n. Вычислить произведение и количество"
      "нечетных цифр числа.")

count = 0
multiply = 1
n = 0
print("Answer:")

N = input("N = ")
while n < len(N):
    if int(N[n]) % 2 == 1:
        count += 1
        multiply *= int(k)
    n += 1
print("count: ", count, "multiply: ", multiply)

# 4.7
print("Определить сумму всех нечетных чисел от 1 до 99")
print("Answer:")
sum = 0
n = 0
while n < 100:
    if n % 2 == 1:
        sum = sum + n
    n += 1
print(sum)

# 4.8
print("Дано целое число n. Сколько цифр в числе n?")
count = 0
print("Answer:")
number = input("N = ")
while count < len(number):
    count += 1
print(count)

# 4.9
print("Найти все целые числа до 200, сумма чисел которых равна 13")
i = 0
while n < 200:
    sum = 0
    for n in str(k):
        sum += int(n)
    if sum == 13:
        print(k)
    n += 1
