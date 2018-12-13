# implementation of longest palindromic subsequence

def lps(str):

    # length of the string
    strlen =  len(str)

    # create memoization table
    L = [[0 for x in range(strlen)] for x in range(strlen)]

    # all substrings of length 1 are palindromes and count is 1 character
    for i in range(strlen):
        L[i][i] = 1

    # subsequence starts from 2 chars now
    for sub in range(2, strlen+1):
        # subsequence of length 0 to of the right corners of the table
        for i in range(strlen-sub+1):

            j = i+sub-1

            # if two characters are the same then length is 2
            if str[i] == str[j] and sub == 2:
                L[i][j] = 2

            #else remove both chars and check for the remaining string and add 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1]+2

            # else check for max of removing first char, or string after removing last char
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])

    # send value in the right most character, which is for the whole string
    return L[0][strlen-1]


    return 0



if __name__ == '__main__':
    str = "helloelloh"
    print("\n Length of Longest Palindromic Sequence: ", lps(str))