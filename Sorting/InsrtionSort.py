# My try


def insSort(arr, n):

    for i in range(0, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        else:
            arr[j + 1] = key


arr = [5, 3, 4, 6, 9]
n = len(arr)
print("sorted array is: ", insSort(arr, n))
