# Insert a node at the first place of a linked list
# 12 = 3 = 4 = 6 = 9

# Makde a node


class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
        self.prev = None

# Make a DLL


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

# Push Algo
    def insert(self, data):
        newNode = Node(data)
        while(self.head != None):
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode

# Print DLL
    def display(self):
        temp = self.head
        while(temp != None):
            print(str(temp.data), end=" ")
            temp = temp.next
            return temp


# driver code
if __name__ == '__main__':
    dll = DLL()
    dll.insert(3)
    dll.insert(4)
    dll.insert(6)
    dll.insert(9)
    dll.display()
