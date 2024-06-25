import time


def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


"""Selection sort"""


def selection_sort(l):
    print("Running Selection Sort...")
    for i in range(len(l)):   #itera su ogni elemento della lista 
        min_index = i  # index of the 1-st element of the unordered sublist
        for j in range(i + 1, len(l)):   #itera sugli elementi della sottolista non ordinata , partendo dall'elemento succesivo ad a.
            if l[min_index] > l[j]:     #ora si cerca un indice di valore minore di min index 
                min_index = j           #quando si trova si imposta uguale a min index ...
        swap(l, i, min_index)          ##
        print("Step", i + 1, "- Partially ordered list: ", l)


####  modifica selection sort per ordinare primariamente in base alla parità e secondariamente in base all'ordinamento naturale 


def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def is_smaller(a, b):
    if a % 2 == b % 2:  # Se entrambi sono pari o dispari
        return a < b    # Confronta i valori
    return a % 2 == 0   # Se uno è pari e l'altro dispari, il pari viene prima

def modified_selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if is_smaller(l[j], l[min_index]):
                min_index = j
        swap(l, i, min_index)

# Test del codice modificato con una lista di esempio
test_list = [5, 3, 2, 8, 1, 4]
modified_selection_sort(test_list)
test_list



"""Insertion sort"""


def insertion_sort(l):
    print("Running Insertion Sort...")
    for i in range(1, len(l)):
        value = l[i]  # value of the current element to be ordered
        j = i - 1  # index of the predecessor of the i-th element
        while j >= 0 and value < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = value
        print("Step", i, "- Partially ordered list: ", l)


"""Bubble sort"""


def bubble_sort(l):
    print("Running Bubble Sort...")
    for i in reversed(range(len(l))):
        for j in range(0, i):
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)
        print("Step", len(l) - i, "- Partially ordered list: ", l)


"""Improved bubble sort"""


def bubble_sort_with_check(l):
    print("Running Improved Bubble Sort Sort...")
    for i in reversed(range(len(l))):
        swap_done = False
        for j in range(0, i):
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)
                swap_done = True
        if swap_done == False:
            break
        print("Step", len(l) - i, "- Partially ordered list: ", l)


"""Merge sort"""


def merge_lists(l, start, middle, high):
    print("Partially ordered list between", start, "and", high, ":", end='')

    start2 = middle + 1

    while start < start2 <= high:

        if l[start] <= l[start2]:
            start += 1
        else:
            value = l[start2]
            index = start2

            # Shift all the elements
            while index != start:
                l[index] = l[index - 1]
                index -= 1

            l[start] = value

            # Update indexes
            start += 1
            start2 += 1

    print(l)


def recursive_merge_sort(l, low, high):
    if low < high:
        middle = (low + high) // 2

        recursive_merge_sort(l, low, middle)
        recursive_merge_sort(l, middle + 1, high)
        merge_lists(l, low, middle, high)


def merge_sort(l):
    print("Running Merge Sort...")
    recursive_merge_sort(l, 0, len(l) - 1)


"""Quick sort"""


def partition(l, low, high):
    pivot = l[high]
    p = low

    for j in range(low, high):
        if l[j] <= pivot:
            l[p], l[j] = l[j], l[p]
            p = p + 1

    l[p], l[high] = l[high], l[p]
    print("Partially ordered list: ", l)
    return p


def recursive_quick_sort(l, low, high):
    pi = partition(l, low, high)
    if low < pi - 1:
        recursive_quick_sort(l, low, pi - 1)
    if pi + 1 < high:
        recursive_quick_sort(l, pi + 1, high)


def quick_sort(l):
    print("Running Quick Sort...")
    recursive_quick_sort(l, 0, len(l) - 1)


my_list=[10, 8, 13, 4, 1, 12, 7, 2]
print("Input list: ", my_list)

start_time = time.time()

#please, select the algorithm to be used by removing # in the following lines

# selection_sort(my_list)
# insertion_sort(my_list)
bubble_sort(my_list)
# bubble_sort_with_check(my_list)
# merge_sort(my_list)
# quick_sort(my_list)


end_time = time.time()

print("Ordered list: ", my_list)
print("Elapsed time:", round(1000* (end_time - start_time), 6), "milliseconds")
