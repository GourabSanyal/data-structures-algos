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

# Approach 3: Sorting each number to a counter

# Function to start the array from 0,1,2


def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


def sortArr(arr, n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

# Count the number of 0s, 1s, 2s
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1

        elif arr[i] == 1:
            cnt1 += 1

        elif arr[i] == 2:
            cnt2 += 1
# Change the value of i

    i = 0

# Sort all the 0s if the beginign

    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1

# Sort all the 1s

    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1

# Sort all the 2s

    while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1

# Print the array
    printArr(arr, n)


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)
sortArr(arr, n)
