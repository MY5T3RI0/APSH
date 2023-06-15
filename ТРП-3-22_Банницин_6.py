# TRP-3-22, Банницин Дмитрий

# 1

print(ord(input("Дан символ C. Вывести его код (то есть номер в кодовой таблице).\n"
                "n = ")))

# 2

print(chr(int(input("Дано целое число N (32 ≤ N ≤ 126). Вывести символ с кодом, "
                    "равнымN. \nn = "))))

# 3

print("Дано целое число N (1 ≤ N ≤ 26). Вывести N первых прописных (тоесть"
      " заглавных) букв латинского алфавита.")

for i in range(65, 65 + int(input("N = "))):
    print(chr(i))

# 4

print("Дан символ C, изображающий цифру или букву (латинскую или"
      " русскую). Если C изображает цифру, то вывести строку «digit», если"
      " латинскую букву — вывести строку «lat», если русскую — вывести"
      " строку «rus».")

N = ord(input("N = "))

if N > 49 and N < 58:
    print("digit")
elif N > 66 and N < 91 or N > 98 and N < 123:
    print('lat')
elif N > 193 and N < 256:
    print('rus')

# 5

print("Дана непустая строка. Вывести коды ее первого и последнего символа.")

str = input("str = ")

print("Answer: ", ord(str[0]), ord(str[len(str) - 1]))

# 6

print("Дано целое число N (> 0) и символ C. Вывести строку длины N, которая"
      " состоит из символов C.")

C = input("C = ")
N = int(input("N = "))

for i in range(1, N+1):
    print(C, end="")

# 7

print("Дана строка. Вывести строку, содержащую те же символы, но"
      " расположенные в обратном порядке.")

str = input("str = ")

for i in range(len(str), 0, -1):
    print(str[i-1], end="")

# 8

print("Дана непустая строка S. Вывести строку, содержащую символы строки"
      " S, между которыми вставлено по одному пробелу.")

S = input("S = ")

for char in S:
    print(char, end=" ")

# 9

print("Дана непустая строка S и целое число N ( > 0). Вывести строку,"
      " содержащую символы строки S, между которыми вставлено по N"
      " символов «*» (звездочка).")

S = input("S = ")
N = int(input("N = "))

for char in S:
    print(char, end="")
    for n in range(0, N):
        print("*", end="")

# 10

print("Дана строка. Подсчитать количество содержащихся в ней цифр.")

S = input("S = ")
count = 0

for char in S:
    try:
        int(char)
        count += 1
    except:
        count

print("Answer: ", int(count))

# 11

print("Дана строка. Подсчитать количество содержащихся в ней прописных"
      " латинских букв.")

S = input("S = ")
count = 0

for char in S:
    if 65 <= ord(char) <= 90:
        count += 1

print("Answer: ", count)

# 12

print("Дана строка. Преобразовать в ней все строчные буквы(как латинские,"
      " так и русские) в прописные, а прописные — в строчные. ")

S = input("S = ")
count = 0

print("Answer: ", end=" ")

for char in S:
    if 65 <= ord(char) <= 90:
        print(chr(ord(char) + 32), end="")
    elif 97 <= ord(char) <= 122:
        print(chr(ord(char) - 32), end="")

# 13

print("Дана строка. Если она представляет собой запись целого числа, то"
      " вывести 1, если вещественного(с дробной частью) — вывести 2"
      " если строку нельзя преобразовать в число, то вывести 0. Считать, что"
      " дробная часть вещественного числа отделяется от его целой части"
      " десятичной точкой «.».")

S = input("S = ")

print("Answer: ", end=" ")

try:
    int(S)
    print(1)
except:
    try:
        float(S)
        print(2)
    except:
        print(0)

# 14

print("Дана строка, изображающая арифметическое выражение вида"
      " «< цифра >±<цифра >±…±<цифра >», где на месте знака операции «±»"
      " находится символ «+» или «–» (например, «4+7–2–8»). Вывести"
      " значение данного выражения(целое число).")

S = input("S = ")
sum = 0

S = S.replace('-', ' -').replace('+', ' ')
print(S)

for num in S.split():
    sum += int(num)

print("Answer: ", sum)

# 15

print("Дано целое число N ( > 0) и строка S. Преобразовать строку S в строку"
      " длины N следующим образом: если длина строки S больше N, то"
      " отбросить первые символы, если длина строки S меньше N, то в ее"
      " начало добавить символы «.» (точка).")

S = input("S = ")
N = int(input("N = "))

print("Answer: ", end='')

if len(S) >= N:
    for n in range(len(S) - N, len(S)):
        print(S[n], end='')
else:
    for n in range(0, N - len(S)):
        print('.', end="")
    print(S)

# 16

print("Даны целые положительные числа N1 и N2 и строки S1 и S2. Получить"
      " из этих строк новую строку, содержащую первые N1 символов строки"
      " S1 и последние N2 символов строки S2")

S1 = input("S1 = ")
S2 = input("S2 = ")
N1 = int(input("N1 = "))
N2 = int(input("N2 = "))

print("Answer: ", end='')

for n in range(0, N1):
    print(S1[n], end='')
for n in range(len(S2) - N2, len(S2)):
    print(S2[n], end='')

# 17

print("Дан символ C и строка S. Удвоить каждое вхождение символа C в"
      " строку S.")

S = input("S = ")
C = input("C = ")

print("Answer: ", end='')

for char in S:
    print(char, end='')
    if char == C:
        print(char, end='')

# 18

print("Дан символ C и строки S, S0. Перед каждым вхождением символа C в"
      " строку S вставить строку S0.")

S = input("S = ")
S0 = input("S0 = ")
C = input("C = ")

print("Answer: ", end='')

for char in S:
    if char == C:
        print(S0, end='')
    print(char, end='')

# 19

print("Даны строки S и S0. Проверить, содержится ли строка S0 в строке S."
      " Если содержится, то вывести True, если не содержится, то вывести"
      " False.")

S = input("S = ")
S0 = input("S0 = ")

print("Answer: ", S0 in S)

# homework

# 1

print("Дан символ C. Вывести два символа, первый из которых предшествует"
      " символу C в кодовой таблице, а второй следует за символом C.")

C = ord(input("C = "))

print("Answer: ", chr(C - 1), chr(C + 1))

# 2

print("Дано целое число N(1 ≤ N ≤ 26). Вывести N последних строчных(то"
      " есть маленьких) букв латинского алфавита в обратном порядке"
      " (начиная с буквы «z»).")

N = int(input("N = "))

print("Answer: ")

for n in range(0, N):
    print(chr(122 - n), end="")

# 3

print("Дана строка. Подсчитать общее количество содержащихся в ней"
      " строчных латинских и русских букв.")

str = input("str = ")
count = 0

for char in str:
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 1040 <= ord(char) <= 1103 or ord(char) == 1025 or ord(char) == 1105:
        count += 1
    print(ord(char))

print("Answer: ", count)

# 4

print("Дана строка. Преобразовать в ней все прописные латинские буквы в"
      " строчные.")

str = input("str = ")

print("Answer: ", str.lower())

# 5

print("Дан символ C и строки S, S0. Перед каждым вхождением символа C в"
      " строку S вставить строку S0.")

S = input("S = ")
S0 = input("S0 = ")
C = input("C = ")

print("Answer: ", end='')

for char in S:
    print(char, end='')
    if char == C:
        print(S0, end='')
