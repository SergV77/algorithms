array = [0, 1, 0, 3, 12]
for el in array:
    if el == 0:
        array.append(array.pop(array.index(el)))

print(array)


# import os
# import shutil
# import threading
#
# dirname1 = r'D:\algorithms\dir1'
# dirname2 = r'D:\algorithms\dir2'
#
# def copy_file(dirname1, dirname2):
#     for file in os.listdir(dirname1):
#         shutil.copy(dirname1 + '/' + file, dirname2)
#         print('%s => %s' % (dirname1 + '/' + file, dirname2 + '/' + file))
#
# for i in range(len(os.listdir(dirname1))):
#     threading.Thread(target=copy_file, args=(dirname1, dirname2)).start()
#


# import time
# from threading import Thread
#
# def sleepMe(i):
#     print("Поток %i засыпает на 5 секунд.\n" % i)
#     time.sleep(5)
#     print("Поток %i сейчас проснулся.\n" % i)
# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()





# print(['aaa', 'bbb', 'ccc'][::-1])
# print('abc'[::-1])

# pow = lambda x: x*x
# data = 1
#
# for i in range(1, 3):
#     data += pow(i)
#
# print(pow(data))

# dict_c = {'1': 3, '2': 2, '3': 1}
# for key in dict_c.keys():
#     if key == '2':
#         del dict_c[key]
#
# print(dict_c)
#