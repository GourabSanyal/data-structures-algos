# define a node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


# define a LinledList


class LL:
    def __init__(self):
        self.head = None

    def addToList(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def displayList(self):
        temp = self.head
        while (temp != None):
            print(temp.data, "->", end="")
            temp = temp.next


def merge(h1, h2):
    dummy = Node(0)
    tail = dummy

    while True:
            # if any onr of the lists gets empty
        while h1 == None:
            tail.next = h2
            break
        if h2 == None:
            tail.next = h1
            break
        # Compare the data and put into new LL
        if h1.data <= h2.data:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next

        tail = tail.next

    return dummy.next


if __name__ == '__main__':

    L1 = LL()
    L2 = LL()

    L1.addToList(1)
    L1.addToList(2)
    L1.addToList(3)

    L2.addToList(3)
    L2.addToList(4)
    L2.addToList(5)

    L1.head = merge(L1.head, L2.head)

    print("merged Linked List is: ")
    L1.displayList()
