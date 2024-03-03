def find_missing_elements(arr):
    if len(arr) <= 1:
        return []

    low = arr[0]
    diff = arr[0]-0
    missing = []
    for i in range(1, len(arr)):
        if arr[i] - i != diff:
            num = i + diff
            while num < arr[i]:
                missing.append(num)
                num = num + 1
            diff = arr[i] - i

    return missing


print(find_missing_elements([6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19]))
