# Pseudocode
# Ask the user what size cup they want, choosing between small, medium, and large.
# Ask the user what kind of coffee they want, choosing between brewed, espresso, and cold brew.
# Ask the user what flavoring they want, if any. Choices include hazelnut, vanilla, and caramel.
# Store types of coffee size, coffee kind, and flavour in dictionaries
# Add cost to one variable, throughout the order

import sys


total_cost = 0

sizes = {
    "small": 2,
    "medium": 3,
    "large": 4
    }

types = {
    "brewed": 0,
    "espresso": 0.5,
    "cold brew": 1
    }

coffee_size = input("Would you like a small, medium, or large? ")
if coffee_size == "small" or coffee_size == "medium" or coffee_size == "large":
    print(f'You selected the {coffee_size} size.')
    total_cost = sizes[f"{coffee_size}"]
else:
    sys.exit("You provided an incorrect response, let's start again. ")



coffee_kind = input("Would you like brewed, espresso, or a cold brew? ")
if coffee_kind == "brewed" or coffee_kind == "espresso" or coffee_kind == "cold brew":
    print(f"You selected {coffee_kind} coffee. ")
    total_cost = total_cost + types[f"{coffee_kind}"]
else:
    sys.exit("You provided an incorrect response, let's start again. ")


flavour = input("Would you like to add a flavouring? Choices include hazelnut, vanilla, and caramel. ")
if flavour == "hazelnut" or flavour == "vanilla" or flavour == "caramel":
    print(f"You selected the {flavour} syrup. ")
    total_cost = total_cost + 0.5
elif flavour == "no":
    print("You did not select a syrup.")
else:
    sys.exit("You provided an incorrect response, let's start again. ")


print(f"To summarise, you asked for a {coffee_size} cup of {coffee_kind} coffee, with {flavour} syrup. ")
print(f"Your total comes to ${total_cost}. ")
