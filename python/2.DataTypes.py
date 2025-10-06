import sys
from fractions import Fraction
from decimal import Decimal

# Immutable Variables
amount = 2
print(f"Amount {id(amount)} {id(2)}: {amount}")

amount = 12
print(f"Amount {id(amount)} {id(12)} : {amount}")

# Mutable Variables
spice_mix = set()
print(f"Spices {id(spice_mix)}")

spice_mix.add("Ginga")
print(f"Spices {id(spice_mix)}")

spice_mix.add("Cardimumum")
print(f"Spices {id(spice_mix)}")

# Integers
shoes_qantity = 3
socks_quantity = 5

total_stock = shoes_qantity + socks_quantity
print(f"Total in stock are {total_stock}")

# Operation

# Basic Division
shoe_per_sock = socks_quantity/shoes_qantity
print(f"Shoes per sock  {shoe_per_sock}")

# Basic Division with Turncate
shoe_per_sock = socks_quantity//shoes_qantity
print(f"Shoes per sock  {shoe_per_sock}")

# Modulas/Reminder
shoe_per_sock = socks_quantity%shoes_qantity
print(f"Reminder shoes per sock  {shoe_per_sock}")

# Exponenet or ^n
shoe_per_sock = socks_quantity**shoes_qantity
print(f"Reminder shoes per sock  {shoe_per_sock}")

# Readability
long_ass_number = 1_00_000
print(f"Long ass number {long_ass_number} ")

# Booliean

    # Upcasting
is_boiling = True
stri_count = 5
total_actions = is_boiling + stri_count
print(f"Total actions : {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk {bool(milk_present)}")
print(f"Is there milk {bool(not milk_present)}")
print(f"Conversion None {bool(None)}")
print(f"Conversion 0 {bool(0)}")
print(f"Conversion String {bool("abc")}")
print(f"Conversion Random Number {bool(4588)}")

# Logical Operators
print(f"Logical True and False :  {True and False}")
print(f"Logical True and False :  {False and True}")
print(f"Logical True and False :  {True or True}")
print(f"Logical True and False :  {False or True}")

# Real Numbers
ideal_temp = 95.5
current_temp = 95.49999999999999

print(f"Ideal temp : {ideal_temp}")
print(f"Current temp : {current_temp}")
print(f"Ideal temp : {ideal_temp - current_temp}")
print(f"Ideal temp : {sys.float_info}")

# Strings
shoe_type = "Trainers"
color = "Blue"
print(f"We need {color} {shoe_type}")

foxc = "Quick Brown Fox"
print(f"The first word is : {foxc[0:5]}")
print(f"The first word is : {foxc[:5]}")
print(f"The first word is : {foxc[6:11]}")
print(f"The first word is : {foxc[::-1]}") # Reversing a string

standard_text = "á"
encoded_text = standard_text.encode("utf-8")
print(f"Standard Text {standard_text}")
print(f"Encoded Text {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded Text {decoded_text}") 


# Tuples 
holistic_weather = ("Rainy", "Sunny", "Windy")
(weather1, weather2, weather3) = holistic_weather # Detstructuring tuples
print(f"Its gonna be {weather1} in the morning leading with few hours of {weather2} weather and then it will be {weather3} the rest of the day.")

# The destructure of tuples can be similarly used in variable assignments
beatdown_ratio, winning_ratio = 2,1
print(f"Printed ratio {beatdown_ratio} , {winning_ratio}")
winning_ratio, beatdown_ratio = beatdown_ratio, winning_ratio
print(f"Flipped up ratio {beatdown_ratio}, {winning_ratio}")

# Membership
print(f"Is Rainy in weather option ? {'Rainy' in holistic_weather}" )
print(f"Is Rainy in weather option ? {'Downpour' in holistic_weather}" )

# List
ingredients = ["Water", "Milk", "Tea Leaves"]
ingredients.append("Sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("Water")
print(f"Reving Ingredients: {ingredients}")
spices = ["Ginger", "Cardimom"]
ingredients.extend(spices)
print(f"Extended Ingedients : {ingredients}")
ingredients.insert(2, "Cloves")
print(f"insert on a location : {ingredients}")
last_item = ingredients.pop()
print(f"Poped item : {last_item}")
print(f"Popped list : {ingredients}")
ingredients.reverse()
print(f"Reveresed list : {ingredients}")
ingredients.sort()
print(f"Sorted List {ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum of sugarlevel : {max(sugar_levels)}")
print(f"Maximum of sugarlevel : {min(sugar_levels)}")

# Operator Overloading
base_liquid = ["water" , "alcohol"]
extra_flavour = ["Mohito Mix"]
print(f"The combination is {base_liquid + extra_flavour}")
print(f"Make for 3 {(base_liquid + extra_flavour) * 3}")

# Bytearray
say_my_name = bytearray(b"Hisenberg")
print(f"Byte Array Output : {say_my_name}")

# Set
essentail_kits = {"Raspberry Pi", "AI Hat"}
essentail_Accessories = {"Case", "SSD Hat", "AI Hat"}

all_kits = essentail_kits | essentail_Accessories # Union operation
print(f"All kits by performing Union Operation {all_kits}") # Prints unique values

common_kits = essentail_kits & essentail_Accessories # Intersection operation
print(f"Common kits by performing Intersection  Operation {common_kits}") # Prints unique values


only_in_all_kits  = essentail_kits - essentail_Accessories # Intersection operation
print(f"Only in essential kits {only_in_all_kits}") # Prints unique values

print(f"Is 'Case' in  essentail_Accessories: {'Case' in essentail_Accessories}")

# Dictonary

parts_order = dict(type="Memory", size="128GB", slot="DDR5" )
print(f"Parts dict : {parts_order}")

parts_list = {}
parts_list["cooler"] = "Air Coller"
parts_list["CPU"] = "Intel"
print(f"Printing Part of dict {parts_list["CPU"]}")
del parts_list["cooler"] # Deleting values from the dict
print(f"Printing new  dict {parts_list}")
print(f"Is 'CPU' in the dict {'CPU' in  parts_list}")

print(f"Keys of the dict {parts_order.keys()}")
print(f"values of the dict {parts_order.values()}")
print(f"items of the dict {parts_order.items()}")

last_item = parts_order.popitem()
print(f"Last item {last_item}")

extra_parts = {"PSU" : "500W"}
parts_list.update(extra_parts) 
print(f"Updated Dict {parts_list}")

non_avail_part_fetch = parts_list.get("cooler", "No Cooler in list")
print(f"Safe Operation Dict {non_avail_part_fetch}")