class Que:

    # innitialize the stack
    def __init__(self):
        self.stack = []
# enque item to the que

    def enQue(self, data):
        self.stack.append(data)

# deque an item from the que
    def deQue(self):

        # return if que is empty
        if len(self.stack) <= 0:
            print("staxk is empty")
            return

        # if stack is not empty then
        # pop an item from the stack
        x = self.stack[len(self.stack) - 1]
        self.stack.pop()

        # return the popped item
        if len(self.stack) <= 0:
            return x

        # push popped item back to the stack
        self.append(x)

        # return the result of deque call

# driver code


if __name__ == '__main__':
    q = Que()
    q.enQue(1)
    q.enQue(2)
    q.enQue(3)

    print(q.deQue())
    print(q.deQue())
    print(q.deQue())
