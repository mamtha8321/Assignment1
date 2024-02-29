def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            # the target value has been found
            return mid
        elif arr[mid] < target:
            # the target value is in the right half of the list
            low = mid + 1
        else:
            # the target value is in the left half of the list
            high = mid - 1

    # the target value was not found
    return -1
arr = [1, 3, 5, 7, 9]
target = 5
print(binary_search(arr, target))  # output: 2
