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
            print(temp.data, end="")
            temp = temp.next

    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):

            # If count of nodes in the
            # given list is less than 'n'
            if(second.next == None):

                # If index = n then
                # delete the head node
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next

        while(second.next != None):
            second = second.next
            first = first.next

        first.next = first.next.next


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
print("Created Linked list is:")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion is:")
llist.printList()
