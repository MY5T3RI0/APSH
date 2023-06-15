# TRP-3-22, Банницин Дмитрий

# 1

import os
print("""Дана строка S. Если S является допустимым именем файла, то
создать пустой файл с этим именем и вывести True. Если файл с
именем S создать нельзя, то вывести False.""")

S = input('S = ')

try:
    f = open(S, 'w+')
    result = True
except:
    result = False

print(result)

# 2

print("""Дано имя файла и целое число N (> 1). Создать файл целых чисел с
данным именем и записать в него N первых положительных четных
чисел (2,4, …).""")

S = input('S = ')
N = int(input('N = '))

try:
    f = open(S, 'w+')
except:
    print("file creation failure")

[f.write(str(i)+" ") for i in range(1, N+1)]
f.close()

# 3

print("""Дано имя файла целых чисел. Найти количество элементов,
содержащихся в данном файле. Если файла с таким именем не
существует, то вывести –1.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

print(len(f.read().split(' '))-1)
f.close()

# 4

print("""Дан файл целых чисел, содержащий не менее четырех элементов.
Вывести первый, второй, предпоследний и последний элементы
данного файла.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
print(fileContent[0], fileContent[1], fileContent[-3], fileContent[-2])
f.close()

# 5

print("""Дан файл целых чисел. Создать новый файл, содержащий те же
элементы, что и исходный файл, но в обратном порядке.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

fNew = open(S.replace('.', '(new).'), 'w+')
[fNew.write(i+" ") for i in fileContent[::-1]]
fNew.close()

# 6

print("""Дан файл вещественных чисел. Создать два новых файла, первый из
которых содержит элементы исходного файла с нечетными
номерами (1, 3,…), а второй — с четными (2, 4, …).""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

fNew = open(S.replace('.', '(new).'), 'w+')
[fNew.write(i+" ") for i in fileContent[::2]]
fNew.close()

fNew = open(S.replace('.', '(new2).'), 'w+')
[fNew.write(i+" ") for i in fileContent[1::2]]
fNew.close()

# 7

print("""Дан файл вещественных чисел. Заменить в нем все элементы на их
квадраты.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

f = open(S, 'w+')
[f.write(str(pow(float(i), 2)) + " ")
 for i in fileContent[:len(fileContent)-1]]
f.close()

# 8
print("""Дан файл вещественных чисел. Поменять в нем местами
минимальный и максимальный элементы.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
minInd = fileContent.index(min(fileContent))
maxInd = fileContent.index(max(fileContent))

fileContent[minInd], fileContent[maxInd] = fileContent[maxInd], fileContent[minInd]
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in fileContent]
f.close()

# 9

print("""Дан файл целых чисел, содержащий четное количество элементов.
Удалить из данного файла вторую половину элементов.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in fileContent[:len(fileContent) // 2 + 1]]
f.close()

# 10

print("""Дан файл целых чисел. Удалить из него все элементы с четными
номерами.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in fileContent[1::2]]
f.close()

# 11

print("""Дан файл целых чисел. Удалить из него все отрицательные числа.""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in filter(lambda i: int(i) >= 0, fileContent)]
f.close()

# 12

print("""Дан файл целых чисел. Удвоить его размер, записав в конец файла
все его исходные элементы (в том же порядке).""")

S = input('S = ')

try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in fileContent]
f.close()

f = open(S, 'a+')
[f.write(i + " ") for i in fileContent]
f.close()

# 13

print("""Дан файл целых чисел. Продублировать в нем все элементы с
нечетными номерами.""")

S = input('S = ')


def duplicate(i):
    fileContent[fileContent.index(i)] = i + " " + i


try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
[duplicate(i) for i in fileContent[1::2]]
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in fileContent]
f.close()

# 14

print("""Дан файл целых чисел. Заменить в нем каждый элемент с четным
номером на два нуля.""")

S = input('S = ')


def duplicate(i):
    fileContent[fileContent.index(i)] = "0 0"


try:
    f = open(S, 'r')
except:
    print("-1")
    exit(0)

fileContent = f.read().split(' ')
[duplicate(i) for i in fileContent[0::2]]
f.close()

f = open(S, 'w+')
[f.write(i + " ") for i in fileContent]
f.close()

# 15

print("""Даны два файла произвольного типа. Поменять местами их
содержимое.""")

S1 = input('S1 = ')
S2 = input('S2 = ')

f1 = open(S1, 'r')
f2 = open(S2, 'r')

fileContent1 = f1.read()
fileContent2 = f2.read()
f1.close()
f2.close()

f1 = open(S1, 'w+')
f2 = open(S2, 'w+')
f2.write(fileContent1)
f1.write(fileContent2)
f1.close()
f2.close()

# 16

print("""Дан файл произвольного типа. Создать его копию с новым именем.""")

S1 = input('S1 = ')

f1 = open(S1, 'r')

fileContent1 = f1.read()
f1.close()

f2 = open(S1.replace('.', '(copy).'), 'w+')
f2.write(fileContent1)
f2.close()

# 17

print("""Даны три файла одного и того же типа, но разного размера.
Заменить содержимое самого длинного файла на содержимое
самого короткого.""")

S = [input('S1 = '), input('S2 = '), input('S3 = ')]

f = [open(S[0], 'r'), open(S[1], 'r'), open(S[2], 'r')]

fileContent = [f[0].read(), f[1].read(), f[2].read()]

size = [len(fileContent[0]), len(fileContent[1]), len(fileContent[2])]

minInd = size.index(min(size[::]))
maxInd = size.index(max(size[::]))

f1 = open(S[minInd], 'w+')
f2 = open(S[maxInd], 'w+')
f1.write(fileContent[maxInd])
f2.write(fileContent[minInd])
f1.close()
f2.close()

# 18

print("""Даны два файла одного и того же типа. Добавить к первому файлу
содержимое второго файла, а ко второму файлу — содержимое
первого.""")

S1 = input('S1 = ')
S2 = input('S2 = ')

f1 = open(S1, 'r')
f2 = open(S2, 'r')

fileContent1 = f1.read()
fileContent2 = f2.read()
f1.close()
f2.close()

f1 = open(S1, 'w+')
f2 = open(S2, 'w+')
f2.write(fileContent1 + " " + fileContent2)
f1.write(fileContent2 + " " + fileContent1)
f1.close()
f2.close()

# 19

print("""Дан файл целых чисел. Создать два новых файла, первый из
которых содержит положительные числа из исходного файла (в
обратном порядке), а второй — отрицательные (также в обратном
порядке). Если положительные или отрицательные числа в
исходном файле отсутствуют, то соответствующий
результирующий файл оставить пустым.""")

S1 = input('S1 = ')

f1 = open(S1, 'r')

fileContent1 = f1.read().split()
f1.close()

f1 = open(S1.replace('.', '(positive).'), 'w+')
f2 = open(S1.replace('.', '(negative).'), 'w+')
[f1.write(i + " ") for i in filter(lambda i: int(i) >= 0, fileContent1)]
[f2.write(i + " ") for i in filter(lambda i: int(i) < 0, fileContent1)]
f1.close()
f2.close()

# 20

print("""Даны два файла вещественных чисел с именами S1 и S2, элементы
которых упорядочены по возрастанию. Объединить эти файлы в
новый файл с именем S3 так, чтобы его элементы также оказались
упорядоченными по возрастанию.""")

S1 = input('S1 = ')
S2 = input('S2 = ')

f1 = open(S1, 'r')
f2 = open(S2, 'r')

fileContent1 = f1.read().split()
fileContent2 = f2.read().split()
f1.close()
f2.close()

fileContent3 = [float(elem) for elem in fileContent2 + fileContent1]
fileContent3.sort()

f1 = open(S1.replace('.', '(union).'), 'w+')

[f1.write(str(i) + " ") for i in fileContent3]
f1.close()

# 21

print("""Дан символьный файл, содержащий по крайней мере один символ
пробела. Удалить все его элементы, расположенные после первого
символа пробела, включая и этот пробел.""")

S1 = input('S1 = ')

f1 = open(S1, 'r')

fileContent1 = f1.read()
f1.close()

fileContent1 = fileContent1[fileContent1.find(" ")+1:]

f1 = open(S1, 'w+')

f1.write(fileContent1)
f1.close()

# 22

print("""Даны имена четырех файлов. Найти количество файлов с
указанными именами, которые имеются в текущем каталоге.""")

S = [input('S1 = '), input('S2 = '), input('S3 = '), input('S4 = ')]

count = 0
files = [i.name for i in os.scandir(os.getcwd())]
for i in range(4):
    if S[i] in files:
        count += 1

print("Answer:", count)
