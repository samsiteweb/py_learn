'''
Given two stringA and stringB, return true if stringA can be formed from the characters of string B and each character of stringB can only be used onces
'''

from collections import Counter

def cha_analysis(string_a, string_b):
    string_b = list(string_b)

    for char in string_a:
        if char in string_b:
            string_b.remove(char)
        else:
            return False

    return True


def can_be_formed(string_a, string_b):
    dic_cha_b = dict(Counter(string_b))

    for char in string_a:
        if dic_cha_b[char] and dic_cha_b != 0:
            dic_cha_b[char] -= 1
        else:
            return False
    return True





def can_be_formed_comprehension(string_a, string_b):
    dic_from_string = {char: string_b.count(char) for char in string_b}
    for char in string_a:
        if dic_from_string[char] and dic_from_string != 0:
            dic_from_string[char] -= 1
        else:
            return False
    return True

print(can_be_formed_comprehension("aab", "aba"))
