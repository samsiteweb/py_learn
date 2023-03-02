age = 16
has_license = False
legal_age = 18

if age < legal_age:
    print("You can't drive yet. You must be 18 years old and have a license")
elif age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You can't drive. You need to have a license")
