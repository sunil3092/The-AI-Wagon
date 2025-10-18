# for using range()
for ticket in range(0,10):
    print(f"Despensing ticket for number {ticket}")

for batch in range(1, 5):
    print(f"Peparing food batch number #{batch}")

# Looping through a list
orders = ["Sam", "John", "Pete"]

for name in orders:
    print(f"Filling the order for {name}")

# Get numbered list
seasons = ['Summer', 'Winter', 'Spring', 'Autumn']

for idx, item in enumerate(seasons, start=1):
    print(f"Seasons {item} with number {idx}")

# Use Case , Order Summary using 2 lists using zip
names = ["Sam", "Jhon", "Lucy" ]
bill = [23,34,54]
for  amount,name in zip(bill, names):
    print(f"{name} paid {amount}")

# Simulate a kettle that starts at 40 Degree and stops at 100 degree
temp = 40

while temp < 100 :
    temp += 15
    print(f"The Temprature is {temp}")

print("Water is boiled")

# continue and break and for else
flavours = ["Ginger", "Out of stock", "Lemon", "Discontiued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        print(f"Out of stock item found")
        continue
    if flavour == "Discontiued":
        print(f"Disconued item found")
        break
    print(f"the flavour is {flavour}") # No Tulsi flsvour as it broke out of the loop

staff = [("Sam", 12), ("Lenorad", 11), ("Amy", 14)]

for name, age in staff:
    if age >= 18:
        print(f"{name} can be hired")
        break
else:
    print("All Underaged")

for name, age in staff:
    if age <= 18:
        print(f"{name} cant be hired")
        break
else:
    print("age is a limit")

# Walrus operator

# Normal Way
value = 13
reminder = value  % 5
if reminder:
    print(f"Not Divisible, Reminder is {reminder}")

# using Walrus operator
walrus_count = 13
if (stranded_walrus := walrus_count % 5):
    print(f"There cant be stranded walrus, Reminder is {stranded_walrus}")

sizes = ["small", "medium", "large"]
if(requested_size := input("Whats the size : ")) in sizes :
    print(f"Requested Size {requested_size}")
else:
    print(f"Size not available")

flavours = ["masala", "ginger"]
print(f"Available flavours : {flavours}")

# Creating Infinite loop
while (available_flavour := input("Choose a flavour : ")) not in flavours :
    print(f"Choosen flavour  {available_flavour} is not available  ")
print(f"chosen flavour is {available_flavour}")

# Using Dictonary to avoid match case
users = [
    {"id" : 1, "total": 100, "coupon" : "P120"},
    {"id" : 2, "total": 140, "coupon" : "P1233"},
    {"id" : 3, "total": 102, "coupon" : "P121210"}
]

discounts = {
    "P120" : (0.2, 0),
    "P1233" : (0.3, 0),
    "P1221210" : (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} got a discount of {discount}")