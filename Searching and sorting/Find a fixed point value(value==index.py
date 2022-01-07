def search(arr, n):
    for i in range(0, n):
        if i == arr[i]:
            return i


arr = [15, 1, 45, 12, 7]
n = len(arr)

result = search(arr, n)
print("asnwer is", result)
