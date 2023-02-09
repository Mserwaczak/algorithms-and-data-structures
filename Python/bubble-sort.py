import numpy as np


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = np.random.randint(0, 1000, size=10)
print("Unsorted: ")
print(arr)
bubble_sort(arr)
print("Sorted: ")
print(arr)
