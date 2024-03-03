def find_pairs(arr):
    pairs = dict()
    sum = 10
    for i in range(0, len(arr)-1):
        if arr[i] in pairs:
            print(f"Pair is '{arr[i]},{pairs[arr[i]]}'")
        else:
            pairs[sum-arr[i]] = arr[i]


print(find_pairs([6, 3, 8, 10, 16, 7, 5, 2, 9, 14]))
