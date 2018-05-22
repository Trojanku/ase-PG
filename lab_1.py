import random
import time

start = 0
stop = 9
step = 1
size = 1000

sortowanie = []

for i in range(size):
    sortowanie.append(random.randrange(start, stop, step))


#            sortowanie babelkowe

def sortowanie_babelkowe(losowe):
    czy = 0
    sortowanie_b = losowe[:]

    def babelkowo():
        z = 0
        while (z < size - 1):
            if (sortowanie_b[z] < sortowanie_b[z + 1]):
                zmienna = sortowanie_b[z]
                sortowanie_b[z] = sortowanie_b[z + 1]
                sortowanie_b[z + 1] = zmienna
                z = 0
            z = z + 1

    def spr():
        for i in range(size - 1):
            if (sortowanie_b[i] < sortowanie_b[i + 1]):
                return czy == 0

    while (czy == 0):
        czy = 1
        babelkowo()
        czy = spr()

    return sortowanie_b


#          selection sort

def sortowanie_selection(losowo):

    sortowanie_s = losowo[:]
    list = []

    while ( len(list) < size ):
        mini = min(sortowanie_s)
        list.append(mini)
        sortowanie_s.pop(sortowanie_s.index(mini))

    return list

#         quick sort

def quicksort(list, pierwszy, ostatni):

    lewy = pierwszy
    prawy = ostatni
    pivot = list[int((pierwszy + ostatni) / 2)]

    while True:

        while(list[lewy] < pivot):
            lewy = lewy + 1
        while(list[prawy] > pivot):
            prawy = prawy - 1

        if lewy > prawy:
            break
        else:
            zmienna = list[lewy]
            list[lewy] = list[prawy]
            list[prawy] = zmienna
            lewy = lewy + 1
            prawy = prawy - 1

    if(prawy > pierwszy):
        quicksort(list,pierwszy, prawy)
    if(lewy < ostatni):
        quicksort(list, lewy, ostatni)


# drukowanie

print('Nieposortowane: ')
print(sortowanie)

czas_start = time.clock()
sortowanie_b = sortowanie_babelkowe(sortowanie)
sortowanie_b.reverse()
czas_stop = time.clock()

czas = czas_stop - czas_start
print("czas babelkowy: ", czas)
print(sortowanie_b)

czas_start = time.clock()
sortowanie_s = sortowanie_selection(sortowanie)
czas_stop = time.clock()

czas = czas_stop - czas_start
print("czas selection sort: ", czas)
print(sortowanie_s)

sortowanie_q = sortowanie[:]

czas_start = time.clock()
quicksort(sortowanie_q, 0, size - 1)
czas_stop = time.clock()

czas = czas_stop - czas_start
print("czas quick sort: ", czas)
print(sortowanie_q)


