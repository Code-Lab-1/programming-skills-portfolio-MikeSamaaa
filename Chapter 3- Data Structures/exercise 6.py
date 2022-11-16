guests = ["Michael Renier C. Bagadiong ", "Cesar James Mangcoy ", "Philip Salvador "]
print("Greetings!" + guests[0] + ", I would like to invite you in a dinner with me and my friends.")
print("Greetings!" + guests[1] + ", I would like to invite you in a dinner with me and my friends.")
print("Greetings!" + guests[2] + ", I would like to invite you in a dinner with me and my friends.")
print(guests[0] + "can't make it for today's dinner, So I'll try to invite Jack Hammer instead.")

guests[0] = "Jack Hammer "  # indexing was used to replace the value in a list

print("Greetings!" + guests[0] + ", I would like to invite you in a dinner with me and my friends.")
print("Greetings!" + guests[1] + ", I would like to invite you in a dinner with me and my friends.")
print("Greetings!" + guests[2] + ", I would like to invite you in a dinner with me and my friends.")

print("Things got unexpected, I can only invite two people for dinner.")

print(guests.pop(0) + ",I'm sorry that I can't invite you to dinner because of unexpected things that happened.")
print(guests[0] + ",you are still invited to come later for our dinner")
print(guests[1] + ",you are still invited to come later for our dinner")
del (guests[0])
del (guests[0])
print(guests)
