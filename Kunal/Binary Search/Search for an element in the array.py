# [-1, 2, -6, 0, 1, ,5, ,8, 9]


def BinSer(arr, s, e, t):
    while s <= e:
        m = s + (e - s)/2
        if arr[m] == t:
            return m
        elif t < arr[m]:
                e = (m - 1)
            else:
                s = arr[m+1]
        return -1


arr = [-1, 2, -6, 0, 1, 5, 8, 9]
t = 8
result = BinSer(arr, 0, len(arr)-1, t)
print("target index is", result)
