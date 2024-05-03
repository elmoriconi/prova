def binary_search(array: list[int], x: int) -> int:
    low = 0
    high = len(array)
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        else:
            if x > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return None