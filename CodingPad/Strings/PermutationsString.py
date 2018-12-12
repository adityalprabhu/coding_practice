# Generating all permutations of a string

def permute(arr, l, r):
    if l == r:
        return "".join(arr)

    else:
        for i in range(l, r+1):
            #swap one character with other and permute for the rest
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            print("".join(arr))
            # backtrack once done for the l, i combination
            # next it will permute for l, i+1 combination
            arr[l], arr[i] = arr[i], arr[l]

# main function
if __name__ == '__main__':
    str = "abc"
    permute(list(str), 0, len(str)-1)