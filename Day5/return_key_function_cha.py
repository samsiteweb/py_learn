# Create a function called power that takes two numeric values as arguments.

def power(num1, num2):
    return num1 ** num2

'''
Create a function called usd_to_eur that takes a numeric value 
(an amount in US dollars) as its only parameter, 
and returns the equivalent amount in euros as a result.
'''

EUR = 0.90
dollars = 1

def usd_to_eur(amount_in_usd):
    return amount_in_usd * EUR


'''
Create a function called reverse_word that 
takes the characters of a given word as an argument, 
reverses the order of their characters, 
and returns them that way and in uppercase.
'''

def reverse_word(word):
    char_list = list(word.upper())
    char_list.reverse()
    reversed = ''.join(char_list)
    return reversed

print(reverse_word("sam"))