# SDESheet Striver Array Qsestion


def merged(arr):
    arr.sort(key == lambda x: x[0])

    merge = []
    start = -10000
    max = -10000

    for i in range(len(arr)):
        if arr[0] > max:
            if i != 0:
                merge.append([start, max])
            max = arr[1]
            start = arr[1]
        else:
            if arr[0] >= max:
                max = arr[1]

    if max != -10000 and [start, max] not in merge:
        merge.append([start, max])
    print("The merged intervals are: ", end=" ")
    for i in range(len(merge)):
        print(merge[1], end=" ")


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
merged(arr)
