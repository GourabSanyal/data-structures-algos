def LinearSearch(arr, n, target):
    if len(arr) == 0:
        return False
    for i in range(0, n):
        if (target == arr[i]):
            return i
    return False


arr = "abcd"
n = len(arr)
target = "d"
result = LinearSearch(arr, n, target)
print("Target index is", result)


# unpack method to turn a string into anarray
# word = "sample"
# print([*word]) // returns ['', 'a', 'm', 'p', 'l', 'e']
