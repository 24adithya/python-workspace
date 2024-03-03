def binary_search(n, arr):
    if arr == None or len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high)/2)

        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            high = mid - 1
        else:
            low = mid + 1

    return -1


print(binary_search(41, [4, 8, 10, 15, 18, 21,
      24, 27, 29, 33, 34, 37, 39, 41, 43]))
