sandwich_orders = ["Tuna Sandwich", "Vegetarian Sandwich", "Chicken Sandwich", "Pastrami Sandwich", "Pastrami Sandwich", "Pastrami Sandwich"]
while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")
finished_sandwiches = []

print("\t")
while sandwich_orders:
    sandwiches_being_made = sandwich_orders.pop()
    print(f"Your {sandwiches_being_made} is being cooked")
    finished_sandwiches.append(sandwiches_being_made)

print("\t")
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " is done!")
