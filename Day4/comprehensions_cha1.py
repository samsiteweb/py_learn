values = [1, 2, 3, 4, 5, 6, 9.5]

square_values = [v ** 2 for v in values]

print(square_values)

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

even_values = [v for v in values if v % 2 == 0]

print(even_values)

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius.

temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(v -32) * (5/9) for v in temperature_fahrenheit]

print(degrees_celsius)