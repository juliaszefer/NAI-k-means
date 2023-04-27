import math

from Iris import Iris
# Wprowadzanie danych przy odpaleniu programu z terminala

# import sys
#
# if len(sys.argv) != 3:
#     print('nieprawidlowa ilosc argumentow')
#     raise TypeError(f"nieprawidlowa ilosc argumentow\nwymagane: 3\notrzymane: {len(sys.argv)}")
#
# pathCSV = sys.argv[1]
# k = int(sys.argv[2])

pathCSV = 'Data/groupset.txt'
k = 3


def calculate(iris1, iris2):
    length = 0
    if len(iris1.vector) != len(iris2.vector):
        quit("Given vectors are not the same length")
    for i in range(len(iris1.vector)):
        length = math.sqrt(math.pow(iris1.vector[i] - iris2.vector[i], 2))
    return length


def sortline(v_line):
    v_type = "default"
    info = v_line.split(",")
    wector = list()
    for i in range(len(info)):
        try:
            wector.append(float(info[i]))
        except ValueError:
            v_type = info[i]
    iris1 = Iris(wector, v_type, 0)
    return iris1


def readfile(path):
    arr = list()
    ffile = open(path, 'r')
    for line in ffile:
        arr.append(sortline(line.replace("\n", "")))
    return arr
