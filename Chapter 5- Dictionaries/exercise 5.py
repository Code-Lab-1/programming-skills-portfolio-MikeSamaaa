pets = []
names = []

name = {"Name" : "Michael",
"Age" : "18",
"Gender" : "Male",
"Weight" : "65 kgs"}
for name in names:
    print("This is what I know about " + name["Name"] + ":")
    for word, value in name:
        print(word + value)
names.append(name)

pet = {"Species" : "Cat",
"Name" : "Mingming",
"Age" : "1 year old",
"Gender" : "Male",
"Weight" : "5 kgs"}

pets.append(pet)

pet = {"Species" : "Dog",
"Name" : "Brownie",
"Age" : "5 months",
"Gender" : "Male",
"Weight" : "15 kgs"}

pets.append(pet)

for pet in pets:
    print("This is what I know about " + pet["Name"] + ":")
    for info, value in pet.items():
        print(info + ": " + str(value))

for name in names:
    print("This is what I know about " + name["Name"] + ":")
    for word, value in name.items():
        print(word + ": " + value)

