import math


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def partition(arr, low, high):
    i, j, pivot = low, high, arr[low]
    while (i < j):
        while (arr[i] <= pivot):
            i = i+1
        while (arr[j] > pivot):
            j = j-1

        if i < j:
            swap(arr[i], arr[j])
    swap(arr[i], arr[j])
    return j


def quick_sort(arr, low, high):

    j = partition(arr, low, high)
    quick_sort(arr, low, j)
    quick_sort(arr, j+1, high)


# arr = [11, 13, 7, 12, 16, 9, 24, 5, 10, 3]
arr = [50, 90, 80]
low = 0
high = len(arr)-1

print(quick_sort(arr, low, high))
