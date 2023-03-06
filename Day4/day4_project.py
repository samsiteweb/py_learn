from random import randint

max_tries = 8
number_tries = 0
life_left = 0

secret_number = randint(1, 3)


name = input("Please what is your name: ")

print(f"Hello {name} Welcome to my first game \n")

print(f"Instruction, please enter any number between 1 and 100 to guess my SECRET NUMBER. \n You only have a maximum of {max_tries} tries. \n Thanks and good luck")

while max_tries != number_tries:
    user_input = input(f"Please enter your guess: ")

    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid entry, please enter an integer between 1 and 100")
        continue

    number_tries += 1
    life_left = max_tries - number_tries

    match user_input:
        case x if x > 100 or x < 1:
            print("The number you have entered is out of play")
        case x if x == secret_number:
            print("You got it right. Congratulations")
            break
        case _:
            print(f"You are wrong please try again. {life_left} tries left")
else:
    print("You are out of tries")