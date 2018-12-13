# solution with memoization

def lcs(x,y):

    m = len(x)
    n = len(y)

    L = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i==0 or j==0:
                L[i][j] = 0

            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1

            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


if __name__ == '__main__':
    str1 = "helloworld"
    str2 = "hqeqlqlqo"
    print("\nFrom solution with memoization")
    print("Length of LCS is ", lcs(str1, str2))


##############################################################


# naive solution without memoization

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0;
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1);
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));


if __name__ == '__main__':
    X = "helloworld"
    Y = "hqeqlqlqo"

    print("\nFrom solution without memoization")
    print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))