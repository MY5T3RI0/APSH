# TRP-3-22, Банницин Дмитрий

# 1

import math
import random

print("Даны целые положительные числа M и N. Сформировать"
      " целочисленную матрицу размера M × N, у которой все элементы I - й"
      " строки имеют значение 10*I(I=1, …, M).")

M = int(input("M ="))
N = int(input("N ="))
A = [[(i+1)*10]*N for i in range(M)]

for m in range(M):
    print(A[m])

# 2

print("Даны целые положительные числа M и N. Сформировать"
      " целочисленную матрицу размера M × N, у которой все элементы J - го"
      " столбца имеют значение 5*J(J=1, …, N).")

M = int(input("M ="))
N = int(input("N ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = (n+1)*5
    print(A[m])

# 3

print("Даны целые положительные числа M, N, число D и набор из M чисел."
      " Сформировать матрицу размера M × N, у которой первый столбец"
      " совпадает с исходным набором чисел, а элементы каждого следующего"
      " столбца равны сумме соответствующего элемента предыдущего столбца"
      " и числа D(в результате каждая строка матрицы будет содержать"
      " элементы арифметической прогрессии).")

M = int(input("M ="))
N = int(input("N ="))
D = int(input("D ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        if n == 0:
            A[m][n] = random.randint(0, 100)
        else:
            A[m][n] = A[m][n-1] + D
    print(A[m])

# 4

print("Дана матрица размера M × N и целое число K(1 ≤ K ≤ M). Вывести"
      " элементы K-й строки данной матрицы.")

M = int(input("M ="))
N = int(input("N ="))
K = int(input("K ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------")
print("Answer: ", A[K-1])

# 5

print("Дана матрица размера M × N и целое число K(1 ≤ K ≤ N). Вывести"
      " элементы K-го столбца данной матрицы.")

M = int(input("M ="))
N = int(input("N ="))
K = int(input("K ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------")
print("Answer: ", [x[K-1] for x in A])

# 6

print("Дана матрица размера M × N. Вывести ее элементы, расположенные в"
      " строках с четными номерами(2, 4, …). Вывод элементов производить по"
      " строкам, условный оператор не использовать.")

M = int(input("M ="))
N = int(input("N ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------")
for m in range(2, M, 2):
    print(A[m])

# 7

print("Дана матрица размера M × N. Вывести ее элементы, расположенныев"
      " столбцах с нечетными номерами(1, 3, …). Вывод элементов"
      " производить по столбцам, условный оператор не использовать.")

M = int(input("M ="))
N = int(input("N ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------")
for m in range(1, N, 2):
    print([x[m] for x in A])

# 8

print("Дана матрица размера M × N и целое число K(1 ≤ K ≤ M). Найти сумму"
      " и произведение элементов K-й строки данной матрицы.")

M = int(input("M ="))
N = int(input("N ="))
K = int(input("K ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------")
print("Answer: sum = ", sum(A[K-1]), " multiply = ", math.prod(A[K-1]))

# 9

print("Дана матрица размера M × N и целое число K(1 ≤ K ≤ N). Найти сумму"
      " и произведение элементов K-го столбца данной матрицы.")

M = int(input("M ="))
N = int(input("N ="))
K = int(input("K ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------")
print("Answer: sum = ", sum([x[K-1] for x in A]),
      " multiply = ", math.prod([x[K-1] for x in A]))

# 10

print("Дана матрица размера M × N. В каждой строке матрицы найти"
      " минимальный элемент.")

M = int(input("M ="))
N = int(input("N ="))
A = [[0]*N for i in range(M)]

for m in range(M):
    for n in range(N):
        A[m][n] = random.randint(0, 100)
    print(A[m])

print("------------------------------\nAnswer:")

for m in range(M):
    print(min(A[m]))
