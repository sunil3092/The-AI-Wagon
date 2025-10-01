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
