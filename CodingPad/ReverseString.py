# Code to reverse a string with no extra data structure

def reverse_string(str):
    return str[::-1]

def reverse_string_recursion(str):
    if len(str) == 1:
        return str[0]
    else:
        return reverse_string_recursion(str[1::]) + str[0]

if __name__ == '__main__':
    str = "This is a sample string"
    print(reverse_string(str))
    print(reverse_string_recursion(str))