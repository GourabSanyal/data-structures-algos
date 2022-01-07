# arr = [ 5,4,3,2,1]


def BS(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]


arr = [5, 4, 3, 2, 1]

resullt = BS(arr)
print("sorted array is ", resullt)
