
def invert_array(array):
    """ Алгоритм перестановки элементов массива.
    :param array: входящий массив
    :return: возврат массива в обратном порядке
    """
    for i in range(len(array)//2):
        array[i], array[len(array)-1-i] = array[len(array)-1-i], array[i]

    return array

#test
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6]
print(invert_array(a))
print(invert_array(b))