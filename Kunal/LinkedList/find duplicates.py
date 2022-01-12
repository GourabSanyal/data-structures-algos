# define a node


class Node:
    def __init__(self, data):
        self.data = data
        self.head = None


# define a LL
class LL:
    def __init__(self):
        self.head = None

# push algo
    def insert(self, newData):
        newNode = Node(newData)
        newData = self.head
        self.head = newNode
        return self.head

# print algo
    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end="")
            temp = temp.next


# Remove duplicate algo

    def removeDuplicate(self):
        if (self.head == None):
            return self.head
        if (self.head.next != None):
            if self.head.data == self.head.next.data:
                self.head = self.head.next.next
                return removeDuplicates(self)
            else:
                removeDuplicates(self.next)

# drive code


if __name__ == "__main__":
    ll = LL()
    ll.insert(2)
    ll.insert(4)
    ll.insert(4)
    ll.insert(5)
    ll.insert(5)
    ll.insert(7)
    print("Linked List innitialy ")
    ll.printList()
    print("After removal of the duplicates ")
    ll.removeDuplicate()
