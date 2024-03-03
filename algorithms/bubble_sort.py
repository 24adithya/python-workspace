def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

    return arr


print(bubble_sort([10, 2, 9, 11, 15, 13]))
