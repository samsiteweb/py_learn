word = input("Enter the word you would love to analysis: ")

letter = []

letter.append(input("Enter first letter: ").lower())
letter.append(input("Enter second letter: ").lower())
letter.append(input("Enter third letter: ").lower())


print("\n")

print(f"The first letter `{letter[0]}` occured {word.count(letter[0])}")
print(f"The first letter `{letter[1]}` occured {word.count(letter[1])}")
print(f"The first letter `{letter[2]}` occured {word.count(letter[2])}")


print("\n")

word_to_list = word.split()

print(f"The total word count for the entered phrase is {len(word_to_list)}")

print("\n")

print(f"First letter {word[0]}")
print(f"Las letter {word[-1]}")

print("\n")

word_to_list.reverse()
inverted_text = ' '.join(word_to_list)

print(f"inverted text {inverted_text}")

print("\n looking for the word python")


is_python = 'python' in word

dic = {True: "was found", False: "was not"}

print(f"word python {dic[is_python]} found ")

