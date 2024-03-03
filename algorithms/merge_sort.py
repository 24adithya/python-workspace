def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    # low = 0
    # high = len(arr)-1
    # leftArr = arr[low:mid]
    # rightArr = arr[mid:high+1]

    leftArr = arr[:mid]
    rightArr = arr[mid:]

    unsorted_left = merge_sort(leftArr)
    unsorted_right = merge_sort(rightArr)

    print(
        f'unsorted_left = {unsorted_left}, unsorted_right = {unsorted_right}')

    i, j, k = 0, 0, 0
    # sortedArr = []
    while i < len(unsorted_left) and j < len(unsorted_right):
        if unsorted_left[i] <= unsorted_right[j]:
            arr[k] = unsorted_left[i]
            i = i+1
        else:
            arr[k] = unsorted_right[j]
            j = j+1
        k = k+1

    while i < len(unsorted_left):
        arr[k] = unsorted_left[i]
        i = i+1
        k = k+1

    while j < len(unsorted_right):
        arr[k] = unsorted_right[j]
        j = j+1
        k = k+1

    return arr


print(merge_sort([8, 3, 7, 4, 9, 2, 6, 5]))
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
