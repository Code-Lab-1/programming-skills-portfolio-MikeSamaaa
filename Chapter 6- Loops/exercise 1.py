toppings = ("Toppings that you'd like to put on your pizza (Type quit when you are done): ")
while True:
    topping = input(toppings).lower()
    if topping != "quit":
        print("I'll add " + topping + " to your pizza")
    else:
        break
