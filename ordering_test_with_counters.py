# This file contains example of sorting algorithms in python
import math
import time
import random
from collections import defaultdict
from matplotlib import pyplot as plt

comparisons = 0

def random_lists(list_per_size, max_size, max_value):
    lists =[]
    for size in range(2,max_size+1):
        for _ in range(list_per_size):
            lists.append(random.sample(range(max_value), size))

    return lists


# this function returns all permutations of the input list
def permutations(input_list):
    # If lst is empty then there are no permutations
    if len(input_list) == 0:
        return []
    # If there is only one element in list then only one permutation is possible
    if len(input_list) == 1:
        return [input_list]
    # Find all permutations of the list
    l = []  # empty list that will store current permutation
    # iterate the list and calculate the permutation
    for i in range(len(input_list)):
        m = input_list[i]
        # extract list[i] or m from the list
        remaining_list = input_list[:i] + input_list[i + 1:]
        # generating all permutations where m is first element
        for p in permutations(remaining_list):
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

samples_selection_sort = defaultdict(int)
samples_insertion_sort = defaultdict(int)
samples_bubble_sort = defaultdict(int)
samples_bubble_sort_with_check = defaultdict(int)
samples_merge_sort = defaultdict(int)
samples_quick_sort = defaultdict(int)

max_list_size = 20
lists_per_list_size = 50
print("Generating lists ...")
permutations_list = random_lists(lists_per_list_size, max_list_size, max_list_size*10)
print("Lists generation completed")
print("Running algorithms and collecting data ...")

for permutation in permutations_list:
    comparisons = 0
    selection_sort(permutation.copy())
    samples_selection_sort[len(permutation)]+=comparisons
    comparisons = 0
    insertion_sort(permutation.copy())
    samples_insertion_sort[len(permutation)]+=comparisons
    comparisons = 0
    bubble_sort(permutation.copy())
    samples_bubble_sort[len(permutation)]+=comparisons
    comparisons = 0
    bubble_sort_with_check(permutation.copy())
    samples_bubble_sort_with_check[len(permutation)]+=comparisons
    comparisons = 0
    merge_sort(permutation.copy())
    samples_merge_sort[len(permutation)]+=comparisons
    comparisons = 0
    quick_sort(permutation.copy())
    samples_quick_sort[len(permutation)]+=comparisons

#calculate average values
for k in samples_selection_sort.keys():
    samples_selection_sort[k] = samples_selection_sort.get(k) / lists_per_list_size
for k in samples_insertion_sort.keys():
    samples_insertion_sort[k] = samples_insertion_sort.get(k) / lists_per_list_size
for k in samples_bubble_sort.keys():
    samples_bubble_sort[k] = samples_bubble_sort.get(k) / lists_per_list_size
for k in samples_bubble_sort_with_check.keys():
    samples_bubble_sort_with_check[k] = samples_bubble_sort_with_check.get(k) / lists_per_list_size
for k in samples_merge_sort.keys():
    samples_merge_sort[k] = samples_merge_sort.get(k) / lists_per_list_size
for k in samples_quick_sort.keys():
    samples_quick_sort[k] = samples_quick_sort.get(k) / lists_per_list_size

print("Data collection terminated")
print("Plotting data ...")

plt.figure(figsize=(8,6))
bin_width= 1
plt.plot(samples_insertion_sort.keys(), samples_insertion_sort.values(), label="Insertion Sort")
plt.plot(samples_bubble_sort_with_check.keys(), samples_bubble_sort.values(), label="Bubble Sort with Check")
plt.plot(samples_merge_sort.keys(), samples_merge_sort.values(), label="Merge Sort")
plt.plot(samples_quick_sort.keys(), samples_quick_sort.values(), label="Quick Sort")
plt.xlabel("List length", size=14)
plt.ylabel("Comparisons", size=14)
plt.title("Comparisons v. List length")
plt.legend()

plt.show()

print("Program terminated")
