#prompt the user to input an item
item = input ("Item: ").strip().lower()

#create a dictionary of fruits(keys) and their corresponding calories(lists)
fruit = {
    "apple": "130",
    "avacado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

#check if the item inputted is in the dictionary and print the calories corresponding to that fruit or item inputted.
if item in fruit:
    print("Calories:", fruit[item])

else:
    print("Enter a fruit from the list given")