while True:
    age = input("What is your age? ").lower()
    if age == "quit":
        break
    age = int(age)
    if age < 3:
       print("The ticket is free")
    elif age < 13:
       print("The ticket is $10")
    else:
        print("The ticket is $15")
