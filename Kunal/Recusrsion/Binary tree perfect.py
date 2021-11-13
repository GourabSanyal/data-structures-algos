def bs(arr, l, r, x):
    m = (l + (r - 1))//2

    if r >= l:
        if arr[m] == x:
            return m

        elif x < arr[m]:
            return bs(arr, l, m, x)

        else:
            return bs(arr, m+1, r, x)
    return -1


arr = [1, 2, 3, 5, 6, 10, 12]
x = 10

print(bs(arr, 0, len(arr)-1, x))
