#Находим наибольший общий делитель a и b
def nod(a, b):
    while b != 0:
        # Вычисляем остаток
        remainder = a % b
        a, b = b, remainder
    return a

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
NOD = nod(a, b)
print("НОД: ")
print(NOD)
