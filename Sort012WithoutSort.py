# # My Approach:


# def search(arr, l, r):
#     for i in range:
#         if len(arr[i]) > len(arr[i + 1]):
#             len(arr[i]) = len(arr[i + 1])
#             len(arr[i + 1])
#         else:
#             print("Not Sorted")


# arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# search(arr)

# Method 2: GFG

def sort012(arr, size):
    low = 0
    high = size - 1
    mid = 0

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high-1
    return arr

# Driver code


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
low = 0
size = len(arr)
mid = 0
print("sorted array:")
print(sort012(arr, size))
