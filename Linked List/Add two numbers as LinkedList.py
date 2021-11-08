# innitialize the node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Init Linkd List


class LinkedList:
    def __init__(self):
        self.head = None

# Init push algo

    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    # Sum of two numbers algo

    def sumOfTwo(self, first, second):

        # define temp, carry and sum nodes
        temp = None
        carry = 0
        prev = None

        # when 1st and 2nd is not zero set data to sum and carry
        while (first and second is not None):

            # define sum overall
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata

            # define carry when sum > 10
            carry = 1 if Sum >= 10 else 0

            # define sum when sum < 10
            Sum = Sum if Sum < 10 else Sum % 10

            # define temp for next iteration
            temp = Node(sum)

            # if this is the first node
            # set it as head of the resultant list

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            # define prev as next node
            prev = temp

            # move first and the second pointers to the net Node
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

    def printSelf(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# driver code
first = LinkedList()
second = LinkedList()

# create first List

first.push(7)
first.push(4)
first.push(6)
first.push(9)
print("first list is "),
first.printSelf()

# create second List

second.push(1)
second.push(8)
second.push(5)
print("second list is  "),
second.printSelf()

# created second list

res = LinkedList()
res.sumOfTwo(first.head, second.head)
print("/nResultant List is")
res.printSelf()
