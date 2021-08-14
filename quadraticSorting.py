#O(N**2)

def insert_sort(array):
    """Сортировка списка вставками."""
    N = len(array)
    for top in range(1, N):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1

def choise_sort(array):
    """Сортировка списка выбором."""
    N = len(array)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]


def bubble_sort(array):
    """Сортировка списка методом пузырька."""
    N = len(array)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]


def test_sort(sort_algorithm):
    print("Тестируем:", sort_algorithm.__doc__)
    print("test case #1: ", end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("test case #2: ", end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("test case #3: ", end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
