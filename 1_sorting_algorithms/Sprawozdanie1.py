import math
from random import randint
from timeit import default_timer as timer



def mergeSort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list1[:mid]
        right = list1[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1


def heapify(list1, n, i):
    global compare_counter
    global swap_counter
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    compare_counter += 1
    if l < n and list1[i] < list1[l]:
        largest = l
    if r < n and list1[largest] < list1[r]:
        largest = r
    if largest != i:
        swap_counter += 1
        list1[i], list1[largest] = list1[largest], list1[i]
        heapify(list1, n, largest)

def heapSort(list1):
    global compare_counter
    global swap_counter
    n = len(list1)
    for i in range(n // 2, -1, -1):
        heapify(list1, n, i)
    for i in range(n - 1, 0, -1):
        swap_counter += 1
        list1[i], list1[0] = list1[0], list1[i]
        heapify(list1, i, 0)


def insertion_sort(list1):
    global  compare_counter
    global  swap_counter
    for i in range(1, len(list1)):
        x = list1[i]
        for j in range(i-1, -1, -1):
            compare_counter += 1
            swap_counter += 1
            if x > list1[j]:
                list1[j+1] = list1[j]
            else:
                list1[j+1] = x
                break
        else:
            list1[0] = x
            swap_counter += 1



def knuth_przyrosty(lista):
    granica = math.ceil(len(lista) / 3)
    przyrosty = []
    k = 1
    while True:
        a = (3**k - 1) // 2
        if a <= granica:
            przyrosty.append(a)
            k += 1
        else: return przyrosty

def ins_sort(lista, zbior_ind):
    swap_num = compare_num = 0
    for i in range(1, len(zbior_ind)):
        x = lista[zbior_ind[i]]
        for j in range(i-1, -1, -1):
            compare_num += 1
            swap_num += 1
            if x > lista[zbior_ind[j]]:
                lista[zbior_ind[j+1]] = lista[zbior_ind[j]]
            else:
                lista[zbior_ind[j+1]] = x
                break
        else:
            lista[zbior_ind[0]] = x
            swap_num += 1
    return swap_num, compare_num

def shell_sort(lista):
    global compare_counter
    global swap_counter
    przyrosty = knuth_przyrosty(lista)
    print("Przyrosty: ", przyrosty)
    n = len(lista)
    for p in przyrosty[::-1]:
        for i in range(p):
            zbior_ind = list(range(i, n, p))
            counters = ins_sort(lista, zbior_ind)
            swap_counter += counters[0]
            compare_counter += counters[1]
    return przyrosty


def quick_sort(lista, i_pocz, j_kon):
    global compare_counter
    global swap_counter
    if i_pocz >= j_kon:
        return 0, 0
    pivot = lista[j_kon]
    print(pivot, end = ", ")
    lista[j_kon] = lista[i_pocz]
    lista[i_pocz] = pivot
    swap_counter += 1
    i = i_pocz + 1
    j = j_kon
    while True:
        while i <= j and lista[j] <= pivot:
            j -= 1
            compare_counter += 1
        if i <= j and not lista[j] <= pivot: compare_counter += 1
        while i <= j and lista[i] >= pivot:
            i += 1
            compare_counter += 1
        if i <= j and not lista[i] >= pivot: compare_counter += 1
        if i > j:
            counters = quick_sort(lista, i_pocz, j)
            swap_counter += counters[0]
            compare_counter += counters[1]
            if i <= j_kon:
                counters = quick_sort(lista, i, j_kon)
                swap_counter += counters[0]
                compare_counter += counters[1]
            return swap_counter, compare_counter
        x = lista[i]
        lista[i] = lista[j]
        lista[j] = x
        swap_counter += 1
        i += 1
        j -= 1


def bubbleSort(lista):
    n = len(lista)
    global compare_counter
    global swap_counter
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            compare_counter+=1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swap_counter +=1


def selection_sort(lista):
    global compare_counter
    global swap_counter
    for i in range(len(lista)-1):
        min = i
        for j in range(i+1, len(lista)-1):
            compare_counter += 1
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
        swap_counter += 1





print("Podaj ciąg liczb:")
l=list(map(int, input().split()))
l_rand = []
for i in range(10):
    l_rand.append(randint(0, 10))


start_time = timer()
mergeSort(l)
stop_time = timer()
print(l)
print("--- Czas sortowania wczynanego ciągu merge sortem: %s ms ---" % ((stop_time - start_time)*(1000)))

start_time = timer()
mergeSort(l_rand)
stop_time = timer()
print("--- Czas sortowania dowolnego ciągu merge sortem: %s ms ---\n" % ((stop_time - start_time)*(1000)))



compare_counter = swap_counter = 0
start_time = timer()
heapSort(l)
stop_time = timer()
print(l)
print("--- Czas sortowania wczynanego ciągu heap sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter)


compare_counter = swap_counter = 0
start_time = timer()
heapSort(l_rand)
stop_time = timer()
print("--- Czas sortowania dowolnego ciągu heap sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter, "\n")



compare_counter = swap_counter = 0
start_time = timer()
insertion_sort(l)
stop_time = timer()
print(l)
print("--- Czas sortowania wczynanego ciągu insert sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter)


compare_counter = swap_counter = 0
start_time = timer()
insertion_sort(l_rand)
stop_time = timer()
print("--- Czas sortowania dowolnego ciągu insert sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter, "\n")



compare_counter = swap_counter = 0
start_time = timer()
shell_sort(l)
stop_time = timer()
print(l)
print("--- Czas sortowania wczynanego ciągu shell sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter)


compare_counter = swap_counter = 0
start_time = timer()
shell_sort(l_rand)
stop_time = timer()
print("--- Czas sortowania dowolnego ciągu shell sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter, "\n")



compare_counter = swap_counter = 0
start_time = timer()
bubbleSort(l)
stop_time = timer()
print(l)
print("--- Czas sortowania wczynanego ciągu bubble sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter)


compare_counter = swap_counter = 0
start_time = timer()
bubbleSort(l_rand)
stop_time = timer()
print("--- Czas sortowania dowolnego ciągu bubble sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter, "\n")



compare_counter = swap_counter = 0
start_time = timer()
selection_sort(l)
stop_time = timer()
print(l)
print("--- Czas sortowania wczynanego ciągu selection sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter)


compare_counter = swap_counter = 0
start_time = timer()
selection_sort(l_rand)
stop_time = timer()
print("--- Czas sortowania dowolnego ciągu selection sortem: %s ms ---" % ((stop_time - start_time)*(1000)))
print("Liczba porównań: ",compare_counter, "\nLiczba swapów: ", swap_counter, "\n")
