# define Node and Init it


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define head and Init it


class LinkedList:
    def __init__(self):
        self.head = None

# reverse list algo

    def reverse(self):
        prev = None
        curr = self.head
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


# put data in list

    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

# print List
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# driver code

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
