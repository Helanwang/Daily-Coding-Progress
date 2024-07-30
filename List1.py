foods = [
    "Lasagna",
    "Sushi",
    "Burrito",
    "Cheeseburger",
    "Caesar Salad",
    "Pad Thai",
    "Chocolate Cake",
    "Grilled Cheese Sandwich",
    "Tacos",
    "Clam Chowder",
]

print(foods[1])  # [1] ask for the index will print the string in the list.

foods.append("Cheeseburger")  # only append one item to the list
print(foods)

foods.remove("Tacos")  # remove one item from the list
print(foods)

"""list.insert(i, x)"""
#  Insert an item at a given position with index

foods.insert(0, "pineapple")
print(foods)


"""list.pop()"""
#  pop directly with the index, not the string/value
foods.pop(0)
print(foods)

foods.sort()
print(foods)