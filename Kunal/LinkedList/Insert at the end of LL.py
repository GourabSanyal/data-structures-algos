class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        # newNode = Node(data)
        # newNode.next = self.head
        # self.head = newNode

    def display(self):
        temp = self.tail
        if (temp != None):
            print(temp.data, end="")
            temp = temp.next

    def insertEnd(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


ll = LL()
ll.insertEnd(1)
ll.display()
ll.insertEnd(5)
ll.display()
ll.insertEnd(8)
ll.display()
