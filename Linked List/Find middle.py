# define a node object
class Node:
    # init self
    def __init__(self, data):
        self.data = data
        self.next = None

# define a linkedist


class LinkedList:
    # init head
    def __init__(self):
        self.head = None

# push algo
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

# Print the list
    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.data) + "->", end="")
            temp = temp.next
        print("null")

# FInd the middle
    def printMiddle(self):
        # define slow and fast
        slow = self.head
        fast = self.head
    # move slopw and fast
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            print("the middle element is", slow.data)

# driver code


if __name__ == '__main__':
    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()
