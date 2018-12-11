# 1. To check if string is a palindrome

str_odd = "malayalam"
str_even = "heveh"

def is_palindrome(str):
    slen = len(str)

    for i in range(0, slen//2):
        if not str[i] == str[slen-i-1]:
            return False

    return True


print(is_palindrome(str_even))
print(is_palindrome(str_odd))