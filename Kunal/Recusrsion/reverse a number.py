

def revr(n):
    sum = 0
    if n == 0:
        return
    else:
        rem = (n % 10)
        sum = (sum * 10) + rem
        n = n//10
        return revr(n)


n = 1234
print(revr(n))
