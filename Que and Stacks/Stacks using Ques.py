q = []


def append(val):
    size = len(q)
    q.append(val)

    for i in range(size):
        x = q.pop(0)
        q.append(x)


def pop():

    if (len(q) == 0):
        print("No elements")
        return -1

    x = q.pop(0)
    return x


def top():

    if(len(q) == 0):
        return -1
    return q[-1]


if __name__ == '__main__':

    s = []

    s.append(10)
    s.append(20)
    print("Top element :" + str(s[-1]))
    s.pop()
    s.append(30)
    s.pop()
    print("Top element :" + str(s[-1]))
