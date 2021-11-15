

# the reverse of digits
def rev(n, temp):

    # base case
    if (n <= 0):
        return temp

    # stores the reverse of a number
    temp = (temp * 10) + (n % 10)

    return rev(n / 10, temp)


# Driver Code
n = 121
temp = rev(n, 0)

if (temp != n):
    print("yes")
else:
    print("no")

# def revr(n):
#     sum = 0
#     if n == 0:
#         return
#     else:
#         rem = (n % 10)
#         sum = (sum * 10) + rem
#         # n = n//10
#         return revr(n/10)


# n = 1234
# print(revr(n))
