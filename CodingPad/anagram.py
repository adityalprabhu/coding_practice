# Check if two string are anagrams
# if they have the same characters in both
# one string is the jumbled version of the other


# Method -  Create count array from 0-256, for that ascii value increment by for first string
# for second string decrements. If count array = 1 then its an anagram


str1 = "helo"
str2 = "hole"


def is_anagram(str1, str2):
    if not len(str1) == len(str2):
        return False

    carr = [0] * 128
    for i in range(len(str1)):
        carr[ord(str1[i].lower())] += 1
        carr[ord(str2[i].lower())] -= 1

    for i in range(len(carr)):
        if not carr[i] == 0:
            return False

    return True


print(is_anagram(str1, str2))