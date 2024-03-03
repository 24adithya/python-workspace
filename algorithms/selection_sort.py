def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(0, len(arr)):
        j, k = i, i
        while j < len(arr):
            if arr[j] < arr[k]:
                k = j
            j = j+1
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp

    return arr


print(selection_sort([8, 6, 3, 2, 5, 4]))
