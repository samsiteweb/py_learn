list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_even = 0
sum_odd = 0
for num in list_numbers:
    if num % 2 == 0:
        sum_even = sum_even + num
    else:
        sum_odd = sum_odd + num
