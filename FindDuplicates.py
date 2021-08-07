def printRepeating(arr, size):
    ans = []
    for i in range(0, size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            ans.append(abs(arr[i]))
    return ans


arr = [1, 2, 3, 1, 3, 6, 6]
print(printRepeating(arr, len(arr)))
