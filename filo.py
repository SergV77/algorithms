
A = [0] * 1000
top = 0
x = int(input("Введите элементы мвссива: "))
while x != 0:
    A[top] = x
    top += 1
    x = int(input("Введите элементы мвссива: "))


for k in range(4, -1, -1):
    print(A[k])



# Копирывание массивов
N = int(input("Введите размер мвссива: "))
A = [0] * N
B = [0] * N

for k in range(N):
    A[k] = int(input("Введите элемент мвссива: "))

for k in range(N):
    B[k] = A[k]


