arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left, right = 0, len(arr) - 1


def binary_search(arr, target, left, right):

    mid = (left + right) // 2
    if target < arr[mid]:
        return binary_search(arr[:mid], target, mid + 1, right)
    elif target > arr[mid]:
        return binary_search(arr[mid:], target, left, mid - 1)
    elif target == arr[mid]:
        return arr[mid]


print(binary_search(arr, 6, left, right))
