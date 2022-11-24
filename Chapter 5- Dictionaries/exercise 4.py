rivers = {"Nile" : "Egypt",
"Cagayan River" : "Philippines",
"Yangtze River" : "China"}

for river, places in rivers.items():
    print("The " + river.title() + " flows through " + places.title())

print('\nThe following that are shown here are rivers:')
for river in rivers.keys():
    print(">" + river.title())

print('\nThe following that are shown here are countries:')
for places in rivers.values():
    print(">" + places.title())
