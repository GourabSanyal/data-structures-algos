# [1,2,5,3,8]


def find(arr, target, i):
    if arr[i] == target:
        return arr[i]
    else:
        i = i+1
        find(arr, target, i)
        return arr[i]


arr = [1, 2, 5, 3, 8]
i = arr[0]
target = 8

print(find(arr, target, i))
