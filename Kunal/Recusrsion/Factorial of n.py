# 5 X 4 X 3 X 2 X 1


def factoorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        n * factoorial(n - 1)


print(factoorial(6))
