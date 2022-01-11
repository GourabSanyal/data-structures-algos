# innitiate the node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# push algo
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
        return newData

# print List algo
    def printList(self):
        temp = self.head
        while(temp != None):
            print(str(temp.data) + '->', end=" ")
            temp = temp.next
            return temp

# delete list algo
    def deleteList(self):
        temp = self.next
        self.data = temp.data
        self.next = temp.next


# driver code
if __name__ == '__main__':

	# Start with the empty list
	head = None

	# Use push() to construct below list
	# 1->12->1->4->1
	head.push(head, 1)
	head.push(head, 4)
	head.push(head, 1)
	head.push(head, 12)
	head.push(head, 1)


    print("List before deleting")
    head.printList()
