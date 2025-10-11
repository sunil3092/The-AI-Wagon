# if
train_coming = True
if train_coming:
    print("Putting up the barriers!")

# if else
in_stock = True
if in_stock:
    print("Producing Invoice")
else:
    print("Please come back later")

need_a_snack = input("Hey you need a snack ?")
if need_a_snack =="yes" or "yep":
    print(f"Lets grab some")
else:
    print(f"Okes")

# If elif else
cup_size = input("What size would you prefer ?").lower()

if cup_size == "small":
    print(f"Price of the tea is : 10")
elif cup_size == "medium":
    print(f"Price of the tea is : 20")
elif cup_size == "large":
    print(f"Price of the tea is : 30")
else:
    print("Invalid size")

# Better approch
size_cup = input("What size would you prefer ?")
available_size_per_price = {"small" : 10, "medium" : 12, "large" : 20}
if size_cup in available_size_per_price:
    print(f"Price of the tea is : {available_size_per_price[size_cup]}")
else:
    print("Invalid size")

# Another example
device_status = True
temprature = 30
if device_status:
    if temprature > 30:
        print("Warning Temperature High!")
    else:
        print("its plesent")
else:
    pass 

# And Another example
order_amt = int(input("Enter an order amount "))

# Delivery fees is 0 if the order amount is greater than 300 else its 30
delivery_fees = 0 if order_amt > 300 else 30
print(f"delivery fees is : {delivery_fees}")

# One last example
seat_type = input("Enter Seat type (sleeper/AC/General)").lower()
match seat_type:
    case "sleeper":
        print("Got a bed")
    case "ac":
        print("Got a bed and a AC")
    case "general":
        print("Can sit")
    case _:
        print("Invlid input")
