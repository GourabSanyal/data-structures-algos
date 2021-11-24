

def linSrc(arr, n, target):
    for i in range(0, n):
        if (arr[i] == target):
            return target
    return -1


arr = [0, 1, 30, 5, 4, 32]
n = len(arr)
target = 2
index = linSrc(arr, n, target)

if (index == -1):
    print("Element ")
else:
    print("Element is not present in", index)
