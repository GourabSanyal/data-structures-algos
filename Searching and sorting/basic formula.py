# [1, 2, 4, 6, 8, 19, 25]
# When the array is sorted in ascending order


def binSrc(arr, target):
    s = 0
    e = len(arr)-1

    while (s <= e):
        mid = (s + (e - s)//2)
        if target < arr[mid]:
            e = (mid - 1)
        elif target > arr[mid]:
            s = (mid + 1)
        else:
            # target == arr[mid]
            return mid
    return -1


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 8, 19, 25]
    target = 19
    result = binSrc(arr, target)

    print("Index of target is", result)

# when the array is not sorted


def binSrc(arr, target):
    s = 0
    e = len(arr)-1

    isAsc = arr[s] < arr[e]

    while (s <= e):
        mid = (s + (e - s)//2)

        if isAsc == True:
            if target < arr[mid]:
                e = (mid - 1)
            elif target > arr[mid]:
                s = (mid + 1)
            else:
                # target == arr[mid]
                return mid

        else:
            if target > arr[mid]:
                e = (mid - 1)
            elif target < arr[mid]:
                s = (mid + 1)
            else:
                # target == arr[mid]
                return mid
    return -1


if __name__ == '__main__':
    arr = [10, 9, 8, 7, 6, 5, 4]
    target = 9
    result = binSrc(arr, target)

    print("Index of target is", result)
