class Node:
    def __init__(self, data):
        self.head = data
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
            print(temp, end="")
            temp = temp.next

    def insertNode(self, data, position):
        newNode = Node(data)
        if self.head == None:
            self.head == Node
        else:
            temp = self.head
            count = 1

            while temp != None and count < position:
                temp = temp.next
                count += 1

            # inserting the node
            newNode.next == temp.next
            temp.next == newNode


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
print("Created Linked list is:")
llist.printList()
llist.insertNode(100, 2)
print("\nLinked List after Deletion is:")
llist.printList()
