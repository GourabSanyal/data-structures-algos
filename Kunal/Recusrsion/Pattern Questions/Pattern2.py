# print

# ****
# ***
# **
# *


def pattern2(n):
    for row in range(0, n):
        for col in range(0, (n-row)):
            print("* ", end="")
        print(" ")


print(pattern2(4))
