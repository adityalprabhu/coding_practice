# implementation of longest palindromic subsequence

def lps(str):

    # length of the string
    n =  len(str)

    # create memoization table
    L = [[0 for x in range(n)] for x in range(n)]

    # all substrings of length 1 are palindromes and count is 1 character
    for i in range(n):
        L[i][i] = 1

    # subsequence starts from 2 chars now
    for k in range(2, n+1):
        # subsequence of length 0 to of the right corners of the table
        for i in range(n-k+1):

            j = i+k-1

            # if two characters are the same then length is 2
            if str[i] == str[j] and k == 2:
                L[i][j] = 2

            #else remove both chars and check for the remaining string and add 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1]+2

            # else check for max of removing first char, or string after removing last char
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])

    # send value in the right most character, which is for the whole string
    return L[0][n-1]


if __name__ == '__main__':
    str = "helloelloh"
    print("\n Length of Longest Palindromic Sequence: ", lps(str))