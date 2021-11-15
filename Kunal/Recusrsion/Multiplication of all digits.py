# 1234
# 1 X 2 X 3 X 4


def multi(n):
    if (n % 10 == n):
        return n
    else:
        return (n % 10) * multi(int(n/10))


print(multi(12345))
