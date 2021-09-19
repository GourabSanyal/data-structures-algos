# Define 2 stacks


class QueStacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

# add elements to 1st stack
    def Add(self, item):
        self.stack1.append(item)

# pop/remove elements from stack 1 to stack 2
# pop element from stack 2
# return popped element from stack2
    def Remove(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


r = QueStacks()
r.Add(10)
r.Add(12)
r.Add(16)
r.Remove()
