# This file contains example of sorting algorithms in python
import math
import time
import random

from matplotlib import pyplot as plt

comparisons = 0

def random_lists(n, size, max_value):
    lists =[]
    for _ in range(n):
        lists.append(random.sample(range(max_value), list_size))

    return lists


# Python function to print permutations of a given list
def permutations(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutations(remLst):
            l.append([m] + p)
    return l

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


"""Selection sort"""

def selection_sort(l):
    global comparisons
    for i in range(len(l)):
        min_index = i   # index of the 1-st element of the unordered sublist
        for j in range(i + 1, len(l)):
            comparisons+=1
            if l[min_index] > l[j]:
                min_index = j
        swap(l, i, min_index)


"""Insertion sort"""

def insertion_sort(l):
    global comparisons
    for i in range(1, len(l)):
        value = l[i]    # value of the current element to be ordered
        j = i - 1       # index of the predecessor of the i-th element
        while j >= 0:
            comparisons+=1
            if value < l[j]:
                l[j + 1] = l[j]
            else:
                break
            j = j - 1
        l[j + 1] = value



"""Bubble sort"""

def bubble_sort(l):
    global comparisons
    for i in reversed(range(len(l))):
        for j in range(0, i):
            comparisons+=1
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)



"""Improved bubble sort"""

def bubble_sort_with_check(l):
    global comparisons
    for i in reversed(range(len(l))):
        swap_done = False
        for j in range(0, i):
            comparisons+=1
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)
                swap_done = True
        if swap_done == False:
            break

    return comparisons

"""Merge sort"""

def merge_lists(l, start, middle, high):
    global comparisons
    start2=middle+1

    while start < start2 <= high:

        comparisons+=1
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

    return comparisons

def recursive_merge_sort(l, low, high):
    if low < high:
        middle = (low + high) // 2

        recursive_merge_sort(l, low, middle)
        recursive_merge_sort(l, middle + 1, high)
        merge_lists(l, low, middle, high)

    return comparisons

def merge_sort(l):
    return recursive_merge_sort(l, 0, len(l) - 1)




"""Quick sort"""

def partition(l, low, high):
    global comparisons
    pivot = l[high]
    p = low

    for j in range(low, high):
        comparisons += 1
        if l[j] <= pivot:
            l[p], l[j] = l[j], l[p]
            p = p + 1

        l[p], l[high] = l[high], l[p]
    return p

def recursive_quick_sort(l, low, high):
    pi = partition(l, low, high)
    if low < pi - 1:
        recursive_quick_sort(l, low, pi - 1)
    if pi + 1 < high:
        recursive_quick_sort(l, pi + 1, high)


def quick_sort(l):
    return recursive_quick_sort(l, 0, len(l) - 1)





"""-------Entry point-------"""

samples_selection_sort = []
samples_insertion_sort = []
samples_bubble_sort = []
samples_bubble_sort_with_check = []
samples_merge_sort = []
samples_quick_sort = []

list_size = 20
number_of_lists = 10000
print("Generating lists ...")
#lists = permutations(list(range(list_size)))
permutations_list = random_lists(number_of_lists, list_size, number_of_lists*1000)
print("Lists generation completed")
print("Running algorithms and collecting data ...")

for permutation in permutations_list:
    comparisons = 0
    selection_sort(permutation.copy())
    samples_selection_sort.append(comparisons)
    comparisons = 0
    insertion_sort(permutation.copy())
    samples_insertion_sort.append(comparisons)
    comparisons = 0
    bubble_sort(permutation.copy())
    samples_bubble_sort.append(comparisons)
    comparisons = 0
    bubble_sort_with_check(permutation.copy())
    samples_bubble_sort_with_check.append(comparisons)
    comparisons = 0
    merge_sort(permutation.copy())
    samples_merge_sort.append(comparisons)
    comparisons = 0
    quick_sort(permutation.copy())
    samples_quick_sort.append(comparisons)

print("Data collection terminated")
print("Plotting data ...")

plt.figure(figsize=(8,6))
bin_width= 1
#plt.hist(samples_selection_sort, bins=1, alpha=0.5, label="Selection Sort")
plt.hist(samples_insertion_sort, bins=range(min(samples_insertion_sort), max(samples_insertion_sort) + bin_width, bin_width), alpha=0.5, label="Insertion Sort")
#plt.hist(samples_bubble_sort, bins=1, alpha=0.5, label="Bubble Sort")
plt.hist(samples_bubble_sort_with_check, bins=range(min(samples_bubble_sort_with_check), max(samples_bubble_sort_with_check) + bin_width, bin_width), alpha=0.5, label="Bubble Sort with Check")
plt.hist(samples_merge_sort, bins=range(min(samples_merge_sort), max(samples_merge_sort) + bin_width, bin_width), alpha=0.5, label="Merge Sort")
plt.hist(samples_quick_sort, bins=range(min(samples_quick_sort), max(samples_quick_sort) + bin_width, bin_width), alpha=0.5, label="Quick Sort", range=[0, list_size * (list_size - 1) / 2])
plt.xlabel("Comparisons", size=14)
plt.ylabel("Count", size=14)
plt.title("Comparisons Histograms")
plt.legend(loc='upper left')

plt.show()

print("Program terminated")
