# print

# 1
# 12
# 123
# 1234


def pattern3(n):
    for row in range(1, n):
        for col in range(1, row+1):
            print(col, "", end="")
        print("  ")


pattern3(5)
