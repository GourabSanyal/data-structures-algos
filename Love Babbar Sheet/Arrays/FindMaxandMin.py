# arr = [32, 43, 76, 98, 132]
# max = arr[0]
# n = len(arr)

# # Finding maximum

# for i in range(0, n):
#     if arr[i] > max:
#         max = arr[i]

# print(max)

# # Finding min

# min = arr[0]
# n = len(arr)

# for i in range(0, n):
#     if arr[i] < min:
#         min = arr[i]

# print(min)

# Approach 2: Competitive GFG


def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # If thewre is ony on e element

    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return(arr_max,  arr_min)

    # If there is only two element

    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return(arr_max,  arr_min)
    else:
         # If there is more than tewo elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)

    return(max(arr_max1,  arr_max2), min(arr_min1,  arr_min2))


# Driver Code
arr = [100, 45, 67, 234]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print("Maximum number:",  arr_max)
print("Minimum number:",  arr_min)
