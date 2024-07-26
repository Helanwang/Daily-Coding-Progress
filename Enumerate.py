list1 = ["apple", "banana", "cherry"]
y = enumerate(list1)

print(list(y))

numbers = [37, 84, 22, 95, 48, 13, 79, 53, 61, 7]
numbers_2 = enumerate(numbers)

print(list(numbers_2))

grocery = [
    "Apples", "Bananas", "Bread", "Milk",
    "Eggs", "Chicken breast", "Spinach",
    "Carrots", "Yogurt", "Rice", "Cheese",
    "Tomatoes", "Olive oil", "Cereal"]

grocery1 = enumerate(grocery)
print(list(grocery1))

# using for loops

for i in enumerate(grocery):
    print(i)

