import math

from Iris import Iris
from Centroid import Centroid

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


def sortline(v_line):
    v_type = "default"
    info = v_line.split(",")
    wector = list()
    for i in range(len(info)):
        try:
            wector.append(float(info[i]))
        except ValueError:
            v_type = info[i]
    iris1 = Iris(wector, v_type, 0, 0)
    return iris1


def readfile(path):
    arr = list()
    ffile = open(path, 'r')
    for line in ffile:
        arr.append(sortline(line.replace("\n", "")))
    return arr


def createcentroids(groups):
    tmp = list()
    elnumber = int(len(groups)/k)
    g = 0
    for i in range(k):
        tmp.append(groups[g])
        g += elnumber
    arr = list()
    for i in range(len(tmp)):
        centroid = Centroid(tmp[i].vector, i+1)
        arr.append(centroid)
    return arr


def calculate(iris, centroid):
    length = 0
    if len(iris.vector) != len(centroid.vector):
        quit("Given vectors are not the same length")
    for i in range(len(iris.vector)):
        length = math.sqrt(math.pow(iris.vector[i] - centroid.vector[i], 2))
    return length


def group(centroids, groups):
    print("")
    for iris in groups:
        howfar = list()
        currentid = 0
        for centroid in centroids:
            howfar.append(calculate(iris, centroid))
            print(f'C{centroid.v_id} distance: {calculate(iris, centroid)}')
            if calculate(iris, centroid) == min(howfar):
                currentid = centroid.v_id
        print(f'{iris.vector} has been assigned to C{currentid}')
        iris.setbelongsto(currentid)
    print("")


def changecentroidsvalue(centroids, groups):
    for centroid in centroids:
        counter = 0
        newvector = list()
        for i in range(len(centroid.vector)):
            newvector.append(0)
        for iris in groups:
            if centroid.v_id == iris.belongsto:
                counter += 1
        for iris in groups:
            if centroid.v_id == iris.belongsto:
                for i in range(len(iris.vector)):
                    newvector[i] += iris.vector[i]
        for i in range(len(newvector)):
            newvector[i] = newvector[i] / counter
        centroid.setvector(newvector)


def kmeans(centroids, groups):
    onceagain = True
    session = 1
    while onceagain:
        print(f"\n{session} session")
        session += 1
        oldvalues = list()
        newvalues = list()
        for iris in groups:
            oldvalues.append(iris.belongsto)
        group(centroids, groups)
        for iris in groups:
            newvalues.append(iris.belongsto)
        if oldvalues == newvalues:
            print("\nGrouping has ended\n")
            return
        else:
            answer = input("Would you like to group again? (y/n)")
            if answer == "n":
                onceagain = False
            else:
                changecentroidsvalue(centroids, groups)

# main


groupset = readfile(pathCSV)
centroidset = createcentroids(groupset)
kmeans(centroidset, groupset)

for iris in groupset:
    print(iris.__str__())
