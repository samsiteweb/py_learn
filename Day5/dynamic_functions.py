'''
Create a function (all_positives) that returns True if all the values in a list are positive,
 and False if at least one of the values is negative.
'''

def all_positives(list):
    for n in list:
        if n < 0:
            return False
    return True

result = all_positives([-1,3,5])

print(result)

'''
Create a function (sum_less) that adds the numbers of a 
list as long as they are greater than 0 and less than 1000, 
and returns the result of said sum. 
'''

def sum_less(numbers):
    sum = 0
    for n in numbers:
        if n is range(0, 1000):
            sum += n

    return sum

print(sum([1,2,3,4]))