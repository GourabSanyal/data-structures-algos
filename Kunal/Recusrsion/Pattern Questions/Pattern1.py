# Print the pattern underneed
# *
# **
# ***
# ****
# *****


def pattern1(n):
    for row in range(0, n):
        for col in range(0, row+1):
            print("* ", end="")
        print(" ")


pattern1(5)
