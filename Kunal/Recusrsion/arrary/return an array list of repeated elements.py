# 1,2,6,6,7


# def repeat(arr, index, target, list):
#     if arr[index] == target:
#         return list
#     else:
#         arr[index] == target
#         list.append(int(index))
#         index = index+1
#         return repeat(arr, index+1, target, list)

def repeat(arr, index, target, list):
    if arr[index] == target:
        return list
    else:
        arr[index] == target
        list.append(int(index))
        index = index+1
        return repeat(arr, index+1, target, list)


arr = [1, 2, 6, 6, 7]
index = arr[0]
target = 6
list = []

print(repeat(arr, index, target, list))

# https://www.geeksforgeeks.org/find-duplicates-constant-array-elements-0-n-1-o1-space/
