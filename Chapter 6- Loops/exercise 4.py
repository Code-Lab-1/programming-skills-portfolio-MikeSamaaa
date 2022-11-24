sandwich_orders = ["Tuna Sandwich", "Vegetarian Sandwich", "Chicken Sandwich"]
finished_sandwiches = []
while sandwich_orders:
    sandwiches_being_made = sandwich_orders.pop()
    print(f"Your {sandwiches_being_made} is being cooked")
    finished_sandwiches.append(sandwiches_being_made)

print("\t")
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " is done!")
