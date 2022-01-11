class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class InsertEnd:
    # Represent the head and tail of the singly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # addAtEnd() will add a new node to the end of the list
    def addAtEnd(self, data):
        # Create a new node
        newNode = Node(data)

        # Checks if the list is empty
        if(self.head == None):
            # If list is empty, both head and tail will point to new node
            self.head = newNode
            self.tail = newNode
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode will become new tail of the list
            self.tail = newNode

    # display() will display all the nodes present in the list
    def display(self):
        # Node current will point to head
        current = self.head

        if(self.head == None):
            print("List is empty")
            return

        print("Adding nodes to the end of the list: ")
        while(current != None):
            # Prints each node by incrementing pointer
            print(current.data)
            current = current.next


sList = InsertEnd()

# Adding 1 to the list
sList.addAtEnd(1)
sList.display()

# Adding 2 to the list
sList.addAtEnd(2)
sList.display()

# Adding 3 to the list
sList.addAtEnd(3)
sList.display()

# Adding 4 to the list
sList.addAtEnd(4)
sList.display()
