list1 = ["Apple", "Banana", "Orange", "Mango", "Pineapple", "Strawberry",
    "Blue berry", "Raspberry", "Blackberry", "Cherry", "Peach", "Plum",
    "Pear", "Grapefruit", "Kiwi", "Papaya", "Guava", "Watermelon",
    "Cantaloupe", "Honeydew", "Lemon", "Lime", "Grape", "Apricot",
    "Fig", "Pomegranate", "Coconut", "Dragonfruit", "Lychee", "Passion fruit"]


"""Access the list"""
print(list1)
print(list1[0])  # the list index starts from zero
print(list1[5])

print(list1[-1])  # -1 meaning starting from the last one of the list
print(list1[-2])  # -2 meaning starting from the last two of the list


list1[1] = "a"
print(list1)
print(list1[1])  # Outputs will be "a"

"""Add one item on the list."""
list1.append("b")
print(list1)


"""Add one more list to the original list."""
list2 = ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",]
list1.extend(list2)
print(list1)


"""Remove one item from the list."""
list1.remove("Apple")
print(list1)


"""Remove the specified index from the list."""
list1.pop(1)
print(list1)  # removed orange from the list, index: 1


"""Delete function for the list"""
del list1[0]
print(list1)  # Deleted "a", index: 0 from the list


"""Loops the list"""
for x in list1:
    print(x)

"""Sorted the list in order."""
list1.sort()
print(list1)


"""Sort the list reversely."""
list1.sort(reverse=True)  # To sort descending, use the keyword argument (reverse = True)
print(list1)


"""Copy the list."""
list1.copy()
print(list1)


"""Join the list."""
list3 = list1 + list2  # Extend function also works in here
print(list3)

"""clear the list, the list still remains."""
list1.clear()
print(list1)


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

