def func(r, c):
    if (c == 0):
        return
    if (c < r):
        print("*", end=" ")
        func(r, c+1)
    else:
        print(" ")
        func(r-1, c)


print(func(4, 0))
