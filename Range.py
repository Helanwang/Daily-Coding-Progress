
for numbers in range(1, 11):
    print(numbers)


"""range from left side starts from 0, range from right side minus 1"""
x = range(6)  # means from 0 to 5
for n in x:
    print(n)

"""Range(100), means 0 to 99."""

y = range(100)
for n in y:
    print(n)

"""If you want to include 100, needs to add one."""
z = range(101)
for n in z:
    print(n)

"""if you want sequences start from besides 0, then indicate the starting point."""
x = range(3, 51)  # count from 3 to 50
for n in x:
    print(n)
