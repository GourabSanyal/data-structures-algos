def missing(arr, size):
    for i in range(size):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print("the repeted number is: ", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("the missing number is: ", i + 1)


arr = [7, 3, 4, 5, 5, 6, 2]
n = len(arr)
missing(arr, n)
