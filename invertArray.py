
def invert_array(array, N):
    """ Алгоритм перестановки элементов массива.
    :param array: входящий массив
    :return: возврат массива в обратном порядке
    """
    for i in range(N//2):
        array[i], array[N-1-i] = array[N-1-i], array[i]

    return array

#test
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6]
print(invert_array(a, len(a)))
print(invert_array(b, len(b)))