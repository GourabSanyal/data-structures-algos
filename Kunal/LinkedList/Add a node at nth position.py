class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end="->")
            temp = temp.next

    def insertAt(self, data, i):
        temp = self.head
        count = 1
        while (temp != None):
            temp = temp.next
            count += 1
        if (count == i):
            temp.next = data
            data = temp


ll = LinkedList()
ll.push(1)
ll.printList()
ll.push(4)
ll.printList()
ll.push(5)
ll.printList()
ll.insertAt(12,  x2)
ll.printList()
