#--------------------------------------------------------------------#
# Алгоритм КМП (Кнут-Морриса-Пратта)                                 #
#--------------------------------------------------------------------#

#Построение массива пи
t = "лилила"


p = [0] * len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

#Поиск образца в строке

a = "лилилось лилилась"

m = len(t)
n = len(a)

i = 0
j = 0

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Образец найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n:
    print("Образец не найден")


#--------------------------------------------------------------------#
# Алгоритм Бойера-Мура-Хорспула                                 #
#--------------------------------------------------------------------#

#Формирование таблицы смещения
t = "данные"

S = set()   # Уникадбные символы в образцу
M = len(t)  # Число символов в образце
d ={}       # Словарь смещений

for i in range(M - 2, -1, -1):  # Итерации с предпоследнего символа
    if t[i] not in S:           # если символ еще не добавлен в таблицу
        d[t[i]] = M - i - 1
        S.add(t[i])

if t[M - 1] not in S:          # Отдельно формируем последний символ
    d[t[M-1]] = M

d['*'] = M                     # смещение для прочих символов

print(d)


#Поиск образца в строке

a = "большие метеоданные"

N = len(a)

if N >= M:
    i = M - 1

    while i < N:
        k = 0
        for j in range(M - 1, -1, -1):
            if a[i-k] != t[j]:
                if j == M - 1:
                    off = d[a[i]] if d.get(a[i], False) else d['*']
                else:
                    off = d[t[j]]

                i += off
                break

            k += 1

        if j == 0:
            print(f"Образец найден по индексу {i - k + 1}")
            break

else:
    print("Образец не найден.")


