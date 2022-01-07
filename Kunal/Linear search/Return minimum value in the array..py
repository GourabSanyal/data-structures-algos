def minvalue(arr, n):
    min = []
    for i in range(0, n):
        if arr[i] < arr[i+1]:
            min.append(i)
            return arr[i]
    return -1


arr = [20, 2, 3, 4, 5]
n = len(arr)

result = minvalue(arr, n)
print("minimum value is", result)
