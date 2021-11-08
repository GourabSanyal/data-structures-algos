# Init node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# init Linked List


class LinkedList:
    def __init__(self):
        self.head = None

    # push algo to insert data
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    # print algo to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end="")
            temp = temp.next

    # Fast and slow pointer
    def findLoop(self):
        fast = self.head
        slow = self.head
        while(fast and slow and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


# driver code

llist = LinkedList()
llist.push(23)
llist.push(3)
llist.push(53)
llist.push(7)

llist.head.next.next = llist.head
if llist.findLoop():
    print("loop Found")
else:
    print("loop not fuond")
