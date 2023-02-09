import numpy as np


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1



def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

arr = np.random.randint(0, 1000, size=10)
print("Unsorted: ")
print(arr)
size = len(arr)
quick_sort(arr, 0, size - 1)
print("Sorted: ")
print(arr)
