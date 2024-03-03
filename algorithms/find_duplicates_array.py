def find_duplicates(arr):
    if len(arr) <= 1:
        return 0
    duplicates = []
    last_duplicate = None
    for i in range(0, len(arr)-1):
        j = i+1
        if arr[i] == arr[j] and last_duplicate != arr[j]:
            last_duplicate = arr[j]
            duplicates.append(last_duplicate)

    return duplicates


print(find_duplicates([3, 6, 8, 8, 10, 12, 15, 15, 15, 20]))
