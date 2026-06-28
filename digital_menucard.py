### Learning Dictionaries (dicts) by building a first Program about it

## Digital Menucard

menucard = {
    "water" : 2.50,
    "thee" : 2.20,
    "cola" : 2.80
}

drink = menucard["water"]
print(f"Price of water: {drink}")


menucard["orange"] = 2.70

menucard["water"] = 3.00

print(menucard)


changed_price = menucard["water"]
# print(f"New water price: {changed_price}")


## Below here, The System Control, if there's a certain drink on the menu-card or not

search_word = "coffee"

if search_word in menucard:
    new_drink = menucard[search_word]
    print(f"New drink price: {new_drink}")
else:
    print(f"{search_word} is not on the menucard.")
