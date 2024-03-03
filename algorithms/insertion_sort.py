def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1  # element(arr[i]) previous to that we need to compare
        x = arr[i]

        while arr[j] > x and j > -1:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = x

    return arr


print(insertion_sort([10, 2, 9, 11, 15, 13]))

# 2, 9 , 10, 11, 15

# 13
