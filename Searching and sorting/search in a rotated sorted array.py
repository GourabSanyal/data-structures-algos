def search(arr):
    n = len(arr) - 1

    for i in range(0, n):
        while arr[i] < arr[i+1]:
            i = i+1
        if arr[i] > arr[i+1]:
            return i+1
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
result = search(arr)
print("index is ", result)
