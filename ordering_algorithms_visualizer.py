import random

from matplotlib import container
import numpy as np
from numpy.core.fromnumeric import partition
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# plt.style.use('dark_background')
# dark background breaks the whole program use safely

class TrackedArray():
    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def track(self, key, access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    # to keep track of the activities
    # like which index was acessed or
    # what operation was performed
    # return type is either a list of tuples or a tuple
    def GetActivity(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indices, self.access_type)]
        else:
            return (self.indices[idx], self.access_type[idx])

    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __delitem__(self, key):
        self.track(key, "del")
        self.arr.__delitem__(key)

    def __len__(self):
        return self.arr.__len__()

    def __str__(self):
        return self.arr.__str__()

    def __repr__(self):
        return self.arr.__repr__()

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


"""Selection sort"""


def selection_sort(l):
    print("Running Selection Sort...")
    for i in range(len(l)):
        min_index = i  # index of the 1-st element of the unordered sublist
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        swap(l, i, min_index)
        print("Step", i + 1, "- Partially ordered list: ", l)


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


"""-------Entry point-------"""
images_per_second = 6.0
list_size = 10
max_value = list_size*10

# creating an array and rounding it off
my_list = random.sample(range(max_value), list_size)
# if a pseudorandom number generator is reinitialized with the same seed,
# it will produce the same sequence of numbers.
# np.random.seed(0)

# shuffling the array
my_list = TrackedArray(my_list)

print(my_list)

fig, ax = plt.subplots(figsize=(16, 8))

fig.suptitle('Sorting Algorithms')
container = ax.bar(np.arange(0, len(my_list), 1), my_list, align='edge', width=0.8)
ax.set(xlabel="Index", ylabel="Value")
ax.set_xlim([0, list_size])

#please, select the algorithm to be used by removing # in the following lines

#selection_sort(my_list)
#insertion_sort(my_list)
bubble_sort(my_list)
#bubble_sort_with_check(my_list)
#merge_sort(my_list)
#quick_sort(my_list)


def update(frame):
    for (rectangle, height) in zip(container.patches, my_list.full_copies[frame]):
        rectangle.set_height(height)
        rectangle.set_color('#1f77b4')

    return *container,


ani = animation.FuncAnimation(fig, update, frames=range(len(my_list.full_copies)),
                              blit=True, interval=1000. / images_per_second, repeat=False)

plt.show()
