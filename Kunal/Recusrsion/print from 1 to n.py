# 5 -> 4 -> 3 -> 2-> 1


def func(n):
    if n == 1:
        return 1
    while (n >= 1):
        print(n, end=' ')
        n = n - 1
        return func(n)


n = 5
print(reversed(func(n)))
