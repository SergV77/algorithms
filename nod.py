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



arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 1, 1, 2, 5, 6, 7]

def compare_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(compare_array(arr1, arr2))

