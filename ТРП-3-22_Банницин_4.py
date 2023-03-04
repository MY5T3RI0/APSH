# TRP-3-22, Банницин Дмитрий

# 1

import random
print("Дано целое число N (> 0). Найти квадрат данного числа, используя для"
      " его вычисления следующую формулу: N2 = 1 + 3 + 5 + … + (2*N - 1)."
      " После добавления к сумме каждого слагаемого выводить текущее"
      " значение суммы (в результате будут выведены квадраты всех целых"
      " чисел от 1 до N).")

N = int(input("N = "))
sum = 0

for n in range(1, N * 2, 2):
    sum += n
    print(sum)

# 2

print("Дано целое число N (> 0). Найти значение выражения 1.1 – 1.2 + 1.3"
      " – … (N слагаемых, знаки чередуются). Условный оператор не"
      " использовать.")

N = int(input("N = "))
sum = 0
k = -1
for n in range(1, N + 1, 1):
    k *= -1
    sum += k * (1 + n/10)
print(round(sum, 1))

# 3

print("Дано целое число N (> 2). Последовательность целых чисел AK"
      "определяется следующим образом: A1 = 1, A2 = 2, A3 = 3, AK = AK–1 +"
      "AK–2 – 2·AK–3, K = 4, 5, … . Вывести элементы A1, A2, …, AN")


def getAk(k):
    if k <= 3:
        return k
    else:
        return getAk(k-1) + getAk(k-2) - 2 * getAk(k-3)


N = int(input("N = "))
print("Answer: ")
for n in range(1, N + 1, 1):
    print(getAk(n))

# 4

print("Даны целые положительные числа A и B (A < B). Вывести все целые числа"
      " от A до B включительно; при этом каждое число должно выводиться"
      " столько раз, каково его значение (например, число 3 выводится 3 раза).")

A = int(input("A = "))
B = int(input("B = "))
print("Answer: ")

for n in range(A, B + 1, 1):
    for m in range(1, n+1, 1):
        print(n, end="")
    print()

# 5

print("Дано целое число N (> 0). Найти двойной факториал N: N!! = N·(N–"
      "2)·(N–4)·… (последний сомножитель равен 2, если N — четное, и 1,если"
      "N — нечетное).")

N = int(input("N = "))

print("Answer: ")

if N % 2 == 1:
    n = 1
else:
    n = 2
ans = 1
while n <= N:
    ans *= n
    n += 2
print(ans)

# 6

print("Дано число A (> 1). Вывести наибольшее из целых чисел K, для"
      " которых сумма 1 + 1/2 + … + 1/K будет меньше A, и саму эту сумму.")

A = int(input("A = "))

print("Answer: ")
sum = 0
k = 1
while sum < A:
    sum += 1/k
    k += 1
print(k-1, sum)

# 7

print("Дано целое число N ( > 1). Последовательность чисел Фибоначчи FK"
      " определяется следующим образом: F1=1, F2=1, FK=FK–2 + FK–1, K=3,"
      " 4, … . Проверить, является ли число N числом Фибоначчи. Если"
      " является, то вывести True, если нет — вывести False.")

N = int(input("N = "))

f1 = 1
f2 = 1
f3 = 2

print("Answer: ")

while f1 <= N:
    if f1 == N or f2 == N or f3 == N:
        print(True)
        quit()
    f1 = f2 + f3
    f2 = f3 + f1
    f3 = f1 + f2
print(False)

# 13

print("Дано целое число N и набор из N вещественных чисел. Вывести в том"
      " же порядке округленные значения всех чисел из данного набора(как целые"
      " числа), а также сумму всех округленных значений.")

N = int(input("N = "))
k = 0
sum = 0
numbers = []
print("Answer: ")

while k < N:
    numbers.append(random.uniform(1, 100))
    k += 1

k = 0

while k < N:
    temp = int(numbers[k])
    print(temp)
    sum += temp
    k += 1
print("sum = ", sum)

# 14

print("Дано целое число N и набор из N целых чисел. Вывести в том же"
      " порядке номера всех нечетных чисел из данного набора и количество K"
      " таких чисел.")

N = int(input("N = "))
k = 0
count = 0
numbers = []
print("Answer: ")

while k < N:
    numbers.append(random.randint(1, 100))
    k += 1

k = 0

while k < N:
    if numbers[k] % 2 == 1:
        print(numbers[k])
        count += 1
    k += 1
print("count = ", count)

# 15

print("Дано целое число N и набор из N целых чисел, упорядоченный по"
      " возрастанию. Данный набор может содержать одинаковыеэлементы."
      " Вывести в том же порядке все различные элементы данного набора.")

N = int(input("N = "))
k = 0
numbers = []
print("Answer: ")

while k < N:
    numbers.append(random.randint(1, 100))
    k += 1

k = 0

while k < N:
    if numbers.count(numbers[k]) == 1:
        print(numbers[k])
    k += 1

# 16

print("Дано целое число N и набор из N целых чисел, содержащий по крайней"
      " мере два нуля. Вывести сумму чисел из данного набора,"
      " расположенных между последними двумя нулями(если последние"
      " нули идут подряд, то вывести 0).")

N = int(input("N = "))
k = 0
sum = 0
flag = False
numbers = []
print("Answer: ")

while k < N:
    numbers.append(random.randint(0, 100))
    k += 1

numbers[random.randint(0, k-1)] = 0
numbers[random.randint(0, k-1)] = 0

k = 0

while k < N:
    if numbers[k] == 0:
        flag = not (flag)
    if flag == True:
        sum += numbers[k]
    k += 1

print("sum = ", sum)

# 17

print("Даны целые числа K, N, а также K наборов целых чисел по N элементов"
      " в каждом наборе. Для каждого набора вывести номер его первого"
      " элемента, равного 2, или число 0, если в данном наборе нет двоек.")

N = int(input("N = "))
K = int(input("K = "))
i = 0
j = 0
numbers = [[0] * K for i in range(N)]
print("Answer: ")

while i < K:
    while j < N:
        numbers[i][j] = random.randint(1, 10)
        j += 1
    i += 1

i = 0
j = 0

while i < K:
    while j < N:
        if numbers[i][j] == 2:
            print(j)
        elif j == N-1:
            print(0)
        j += 1
    i += 1
    j = 0

# 18

print("Дано целое число N, а также K наборов ненулевых целых чисел."
      " Признаком завершения каждого набора является число 0. Для каждого"
      " набора вывести количество его элементов. Вывести также общее"
      " количество элементов во всех наборах.")

K = int(input("K = "))
i = 0
j = 0
sum = 0
numbers = []

A = []
while i < K:
    row = input('numbers[{}] = '.format(i)).split()
    while j < len(row):
        row[j] = int(row[j])
        j += 1
    numbers.append(row)
    i += 1
    j = 0

i = 0
j = 0

print("Answer: ")

while i < K:
    print('[{}] {}'.format(i, len(numbers[i]) - 1))
    sum += len(numbers[i]) - 1
    i += 1
print('total count = {}'.format(sum))

# 19

print("Дано целое число K, а также K наборов ненулевых целых чисел."
      " Каждый набор содержит не менее двух элементов, признаком его"
      " завершения является число 0. Найти количество наборов, элементы"
      " которых возрастают.")

K = int(input("K = "))
i = 0
j = 0
flag = False
sum = 0
numbers = []

A = []
while i < K:
    row = input('numbers[{}] = '.format(i)).split()
    while j < len(row):
        row[j] = int(row[j])
        if int(row[j-1]) > row[j] and row[j] != 0:
            flag = True
        j += 1
    if flag == False:
        sum += 1
    flag = False
    numbers.append(row)
    i += 1
    j = 0
print("Answer: ", sum)

# 20

print("Дано целое число K, а также K наборов ненулевых целых чисел."
      " Каждый набор содержит не менее двух элементов, признаком его"
      " завершения является число 0. Для каждого набора выполнить"
      " следующее действие: если элементы набора возрастают, то вывести 1"
      " если элементы набора убывают, то вывести –1"
      " если элементы набора"
      "не возрастают и не убывают, то вывести 0.")

K = int(input("K = "))
i = 0
j = 0
increase = False
decrease = False
numbers = []

A = []
while i < K:
    row = input('numbers[{}] = '.format(i)).split()
    while j < len(row):
        row[j] = int(row[j])
        if int(row[j-1]) > row[j] and row[j] != 0:
            increase = True
        elif int(row[j-1]) < row[j] and row[j] != 0 and j != 0:
            decrease = True
        j += 1
    if increase == False:
        print('[{}] {}'.format(i, 1))
    elif decrease == False:
        print('[{}] {}'.format(i, -1))
    else:
        print('[{}] {}'.format(i, 0))
    increase = False
    decrease = False
    numbers.append(row)
    i += 1
    j = 0
print("Answer: ", sum)

# 21

print("Дано целое число N ( > 2) и набор из N вещественных чисел. Набор"
      " называется пилообразным, если каждый его внутренний элемент либо"
      " больше, либо меньше обоих своих соседей(то есть является"
      " «зубцом»). Если данный набор является пилообразным, то вывести 0"
      "в противном случае вывести номер первого элемента, не являющегося"
      " зубцом.")

numbers = input("N = ").split()
i = 0

while i < len(numbers):
    numbers[i] = float(numbers[i])
    if i > 1:
        if not (numbers[i-1] < numbers[i-2] and numbers[i-1] < numbers[i] or numbers[i-1] > numbers[i-2] and numbers[i-1] > numbers[i]):
            print("Answer: ", i)
            quit()
    i += 1

print("Answer: ", 0)