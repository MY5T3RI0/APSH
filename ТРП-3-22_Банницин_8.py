# TRP-3-22, Банницин Дмитрий

# 1

import random
print("Дано целое число N ( > 0). Сформировать и вывести целочисленный"
      " список размера N, содержащий N первых положительных нечетных"
      " чисел: 1, 3, 5, … .")

N = int(input("N = "))
nums = []

for n in range(1, N * 2, 2):
    nums.append(n)

print(nums)

# 2

print("Дано целое число N (> 1), а также первый член A и разность D"
      " арифметической прогрессии. Сформировать и вывести список размера"
      " N, содержащий N первых членов данной прогрессии: A, A + D, A + 2·D,"
      " A + 3·D, … .")

N = int(input("N = "))
A = int(input("A = "))
D = int(input("D = "))
nums = []

for n in range(A, (N + 1) * D, D):
    nums.append(n)

print(nums)

# 3

print("Даны целые числа N ( > 2), A и B. Сформировать и вывести"
      " целочисленный список размера N, первый элемент которого равен A,"
      " второй равен B, а каждый последующий элемент равен сумме всех"
      " предыдущих.")

N = int(input("N = "))
A = int(input("A = "))
B = int(input("D = "))
nums = []

nums.append(A)
nums.append(B)

for n in range(2, N):
    nums.append(nums[n-2] + nums[n-1])

print(nums)

# 4

print("Дан целочисленный список размера N. Вывести все содержащиеся в"
      " данном списке четные числа в порядке убывания их индексов, а также"
      " их количество K.")

N = int(input("N = "))

nums = []

for n in range(0, N):
    nums.append(random.randint(0, 100))

print(nums)

for n in nums[::-1]:
    if n % 2 == 0:
        print(n)

# 5

print("Дан список A ненулевых целых чисел размера 10. Вывести значение"
      " первого из тех его элементов AK, которые удовлетворяют неравенству"
      " AK < A10. Если таких элементов нет, то вывести 0.")

nums = []

for n in range(0, 10):
    nums.append(random.randint(1, 100))

print(nums)

for n in nums:
    if n < nums[9]:
        print(n)
        exit(0)
print(0)

# 6

print("Дан список размера N и целые числа K и L(1 < K ≤ L ≤ N). Найти сумму"
      " всех элементов списка, кроме элементов с номерами от K до L"
      " включительно.")

N = int(input("N = "))
K = int(input("K = "))
L = int(input("L = "))

nums = []
s = 0

for n in range(0, N):
    nums.append(random.randint(1, 100))

print(nums)

s = sum(nums[:K]) + sum(nums[L+1:])

print(s)

# 7

print("Дан целочисленный список размера N. Проверить, чередуются ли в нем"
      " четные и нечетные числа. Если чередуются, то вывести 0, если нет, то"
      " вывести порядковый номер первого элемента, нарушающего"
      " закономерность.")

N = int(input("N = "))

nums = []

for n in range(0, N):
    nums.append(random.randint(1, 10))

print(nums)

for n in range(1, len(nums)):
    if nums[n] % 2 == nums[n-1] % 2:
        print(n)
        exit(0)

print(0)

# 8

print("Дан список A размера N. Найти минимальный элемент из его элементов"
      "с четными номерами: A2, A4, A6, … .")

N = int(input("N = "))

nums = []

for n in range(0, N):
    nums.append(random.randint(1, 100))

print(nums)

print(min(nums[::2]))

# 9

print("Дан список размера N. Найти номера тех элементов списка, которые"
      " больше своего правого соседа, и количество таких элементов."
      " Найденные номера выводить в порядке их возрастания.")

N = int(input("N = "))

nums = []
count = 0

for n in range(0, N):
    nums.append(random.randint(1, 100))

print(nums)

for n in range(0, N-1):
    if nums[n] > nums[n+1]:
        print(n)
        count += 1

print("count = ", count)

# 10

print("Даны два списка A и B одинакового размера N. Сформировать новый"
      " список C того же размера, каждый элемент которого равен"
      " максимальному из элементов списков A и B с тем же индексом.")

N = int(input("N = "))

nums1 = []
nums2 = []
nums3 = []

for n in range(0, N):
    nums1.append(random.randint(1, 100))
for n in range(0, N):
    nums2.append(random.randint(1, 100))

print(nums1)
print(nums2)

for n in range(0, N):
    nums3.append(max(nums1[n], nums2[n]))

print(nums3)

# 11

print("Дан целочисленный список A размера N. Переписать в новый"
      "целочисленный список B все четные числа из исходного списка(в том"
      "же порядке) и вывести размер полученного списка B и его содержимое.")

N = int(input("N = "))

A = []
B = []

for n in range(0, N):
    A.append(random.randint(1, 100))

print(A)

for n in range(0, N):
    if A[n] % 2 == 0:
        B.append(A[n])

print("B(size = ", len(B), ") : ", B)

# 12

print("Дан список A размера N. Сформировать два новых списка B и C: в"
      "список B записать все положительные элементы списка A, в список C —"
      "все отрицательные(сохраняя исходный порядок следования"
      "элементов). Вывести вначале размер и содержимое списка B, а затем"
      "— размер и содержимое списка C.")

N = int(input("N = "))

A = []
B = []
C = []

for n in range(0, N):
    A.append(random.randint(-100, 100))

print(A)

for n in range(0, N):
    if A[n] >= 0:
        B.append(A[n])
    else:
        C.append(A[n])

print("B(size = ", len(B), ") : ", B)
print("C(size = ", len(C), ") : ", C)

# 13

print("Дан список A размера N и целое число K(1 ≤ K ≤ N). Преобразовать"
      " список, увеличив каждый его элемент на исходное значение элемента"
      " AK.")

N = int(input("N = "))
K = int(input("K = "))

A = []

for n in range(0, N):
    A.append(random.randint(0, 100))

print(A)
AK = A[K]
for n in range(0, N):
    A[n] += AK

print("A(size = ", len(A), ") : ", A)

# 14

print("Дан список размера N. Поменять местами его минимальный и"
      "максимальный элементы.")

N = int(input("N = "))

A = []

for n in range(0, N):
    A.append(random.randint(0, 100))

print(A)

print(A.index(min(A)))
print(A.index(max(A)))

A[A.index(min(A))], A[A.index(max(A))] = A[A.index(max(A))], A[A.index(min(A))]

print("A(size = ", len(A), ") : ", A)

# 15

print("Дана матрица размера M × N. Преобразовать матрицу, поменяв"
      " местами минимальный и максимальный элемент в каждой строке.")

M = int(input("M ="))
N = int(input("N ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

for m in range(M):
    min_ind = A[m].index(min(A[m]))
    max_ind = A[m].index(max(A[m]))
    A[m][min_ind], A[m][max_ind] = A[m][max_ind], A[m][min_ind]
    print("A[", m, "](size = ", len(A[m]), ") : ", A[m])

# 16

print("Дана матрица размера M × N. Преобразовать матрицу, поменяв"
      "местами минимальный и максимальный элемент в каждом столбце.")

M = int(input("M ="))
N = int(input("N ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

for m in range(N):
    min_ind = ([x[m] for x in A]).index(min([x[m] for x in A]))
    max_ind = ([x[m] for x in A]).index(max([x[m] for x in A]))
    A[min_ind][m], A[max_ind][m] = A[max_ind][m], A[min_ind][m]

for m in range(M):
    print(A[m])

# 17

print("Дана квадратная матрица A порядка M. Найти сумму элементов ее"
      " главной диагонали, то есть диагонали, содержащей следующие"
      " элементы: A1, 1, A2, 2, A3, 3, …, AM, M.")

M = int(input("M ="))
A = [[0]*M for i in range(M)]

for m in range(M):
    for n in range(M):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("-----------------")

print("Answer: ", sum([A[x][x] for x in range(M)]))

# 18

print("Дана квадратная матрица A порядка M. Найти среднее арифметическое"
      " элементов ее побочной диагонали, то есть диагонали, содержащей"
      " следующие элементы: A1, M, A2, M–1, A3, M–2, …, AM, 1")

M = int(input("M ="))
A = [[0]*M for i in range(M)]

for m in range(M):
    for n in range(M):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("-----------------")

print("Answer: ", sum([A[x][-x-1] for x in range(M)])/M)

# 19

print("Дана квадратная матрица A порядка M. Найти сумму элементов каждой"
      "ее диагонали, параллельной главной(начиная с одноэлементной диагонали A1, M).")

M = int(input("M ="))
A = [[0]*M for i in range(M)]

for m in range(M):
    for n in range(M):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("-----------------")

for n in range(M-1, 0, -1):
    print(sum([A[x][x+n] for x in range(M-n)]))

for n in range(M):
    print(sum([A[x+n][x] for x in range(M-n)]))

# 20

print("Дана квадратная матрица A порядка M. Найти минимальный элемент для"
      " каждой ее диагонали, параллельной главной(начиная содноэлементной диагонали A1, M).")

M = int(input("M ="))
A = [[0]*M for i in range(M)]

for m in range(M):
    for n in range(M):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("-----------------")

for n in range(M-1, 0, -1):
    print(min([A[x][x+n] for x in range(M-n)]))

for n in range(M):
    print(min([A[x+n][x] for x in range(M-n)]))
