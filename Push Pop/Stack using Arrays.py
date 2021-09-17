from sys import maxsize

# create the srtack


def createStack():
    stack = []
    return stack

# stack is empty when stack is zero


def emptyStack(stack):
    return len(stack) == 0

# Add an item to the stack


def push(stack, item):
    stack.append(item)
    print(item + "added to the stack")

# remove an item from the stack


def pop(stack):
    if (emptyStack(stack)):
        return str(-maxsize - 1)  # return minus infinite

    return stack.pop()

# return top element without removing it


def peek(stack):
    if (emptyStack(stack)):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")
