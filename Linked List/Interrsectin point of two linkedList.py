# define node


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

# algo for intersection


def interSection(first, second):
    ptr1 = first
    ptr2 = second

    # When 1st and 2nd heads are not equal then
    # place the 1st pointer at 2nd List's head
    # and vice versa
    # Return the 1st

    while (ptr1 != ptr2):
        if ptr1 is None:
            ptr1 = second
        else:
            ptr1 = ptr1.next

        if ptr2 is None:
            ptr2 = first
        else:
            ptr2 = ptr2.next

    return ptr1

# driver code

# construct the first List


first = Node(1)
first.next = Node(2)
first.next.next = Node(3)


# construct the second List
second = Node(1)
second.next = Node(2)
second.next.next = Node(3)

first.next.next.next = Node(4)
first.next.next.next.next = Node(5)

# link tail of the second list to the fourth node of the first list
second.next.next.next = first.next.next.next
addr = interSection(first, second)
print("Intersection Node is", addr.data)

# 1-> 2-> 3-> 4-> 5
# 1-> 2-> 3->
