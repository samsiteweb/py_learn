values = [1, 2, 3, 4, 5, 6, 9.5]

square_values = [v ** 2 for v in values]

print(square_values)

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

even_values = [v for v in values if v % 2 == 0]

print(even_values)