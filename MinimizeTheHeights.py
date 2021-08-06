def minHeight(arr, n, k):
    arr.sort()
    ans = arr[n-1] - arr[0]
    smallest = arr[0] + k
    highest = arr[n - 1] - k

    for i in range(0, n):
        small = min(smallest, arr[i] - k)
        big = max(highest, arr[i-1] + k)
        ans = min(ans, big - small)

    return ans


arr = [1, 10, 14, 14, 14, 15]
k = 6
print(minHeight(arr, len(arr), k))
