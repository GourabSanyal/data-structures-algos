# Approach 1: use "reverse()"

# list = [21, 32, 65, 87, 55]
# list.reverse()
# print("Approach 1:", list)

# Approach 2: Python slicing method

list = [21, 32, 65, 87, 55]
list1 = list[::-1]
print("Approach 2:", list1)

# Approach 3: Iterative way


def reverseList(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start = +1
        end = -1


list = [21, 32, 65, 87, 55]
print(list)
reverseList(list, 0, 4)
print("reverse List is")
print(list)
