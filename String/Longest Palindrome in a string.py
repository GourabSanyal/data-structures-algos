def printSubStr(s, l, r):

    for i in range(l, r + 1):
        print(str[i], end="")


def longestPalindrome(s):
    res = 0
    resLen = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r <= len(s) and s[l] == s[r]:
            if (r - l + 1) > res:
                res = s[l: r+1]
                resLen = (r - l + 1)
            l = l-1
            r = r+1

        # even length
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[i]:
            if (r - l + 1) > res:
                res = s[l: r+1]
                resLen = (r - l + 1)
            l = l-1
            r = r+1
    return res


if __name__ == '__main__':
    input = "aabaab"
    longestPalindrome(input)
