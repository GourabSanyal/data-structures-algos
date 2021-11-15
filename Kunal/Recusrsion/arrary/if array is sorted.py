# 1,6,8,3,4,


def ifSorted(arr, index):
    if (index == len(arr)-1):
        return True
    else:
        arr[index] < arr[index+1] and ifSorted(arr, index+1)
        return True


arr = [1, 2, 4, 3, 8]
index = arr[0]

print(ifSorted(arr, index))
