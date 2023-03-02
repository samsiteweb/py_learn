speak_french = True
knows_python = False

if speak_french or knows_python:
    if not knows_python and speak_french:
        print("To apply, you need to know how to program in Python")
    elif not speak_french and knows_python:
        print("To apply, you need to speak French")
    else:
        print("You meet the requirements to apply")
else:
    print("To apply, you need to know how to program in Python and speak French")
