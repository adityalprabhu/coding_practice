# solution to longest palindromic substring
# consecutive letters should be palindromic
import sys

def printSubStr(st,low,high) :
    sys.stdout.write(st[low : high + 1])
    sys.stdout.flush()
    return ''

def lpss(str):

    n = len(str)

    L = [[0 for x in range(n)] for y in range(n)]

    maxlen = 1
    i = 0

    while i < n:
        L[i][i] = True
        i = i + 1

    start = 0
    i = 0

    while i < n - 1:
        if str[i] == str[i+1]:
            L[i][i+1] = True
            start = i
            maxlen = 2
        i = i + 1

    k = 3

    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if (L[i+1][j-1] == True) and (str[i] == str[j]):
                L[i][j] = True

                if k > maxlen:
                    start = i
                    maxlen = k

            i = i + 1
        k = k + 1

    # print("Longest palindrome substring is: ", printSubStr(str, start, start + maxlen - 1))

    return maxlen


if __name__ == '__main__':
    str = "helloolleh"
    print(lpss(str))