# [1, 2, 3, 4,5, 5, 6, 7, 8]
# https://www.youtube.com/watch?v=7h3MdoqnZhc&ab_channel=TimothyHChang


def find(arr, l, r, t, n):
    sl = -1
    sr = -1
    l = 0
    r = len(arr) - 1

    mid = l + (r - l)//2
    while l >= r:

        # Searching right

        if t >= arr[mid]:
            l = mid + 1
        else:
            r = mid
    if l > r and arr[r - 1] == t:
        sr = r

        # Searching left
    while l >= r:
        if t <= arr[mid]:
            r = mid
        else:
            l = mid + 1
    if l > n and arr[l] == t:
        sl = l

    return [sl, sr]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 5, 6, 7, 8]
    l = arr[0]
    r = len(arr)-1
    t = 5
    n = len(arr)
    result = find(arr, l, r, t, n)

    print("First and the last index of the target is", result)
