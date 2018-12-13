# solution for edit distance

def ed(str1, str2):
    m = len(str1)
    n = len(str2)

    L = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            # if first string is empty
            if i == 0:
                L[i][j] = j

            # if second string is empty
            elif j == 0:
                L[i][j] = i

            # if last two characters are equal
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1]

            else:
                L[i][j] = 1 + min(L[i][j-1] # insert
                                  , L[i-1][j] # remove
                                  , L[i-1][j-1] # replace
                                  )


    return L[m][n]


# main function
if __name__ == '__main__':
    str1 = "hello"
    str2 = "hgel1sllfdo"
    print(ed(str1,str2))