from random import choice, randint, random, uniform, shuffle

# randomly choose between a list
names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
raffle = choice(names)

# generate a random real number
real_number = random()

# generate a random number between a range
random_number = round(uniform(1, 5), 3)
print(random_number)

# shuffle a list
my_of_numbers = list(range(1, 51, 5))
shuffle(my_of_numbers)
shuffle(names)
print(my_of_numbers)
print(names)

# random integer within a range

print(f"{randint(1, 10)}")


