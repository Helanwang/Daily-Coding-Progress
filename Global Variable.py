def function():
    global x  # To create a global variable inside a function, you can use the global keyword.
    x = "Nice Work!"
    print(x)


function()


x = "Baby"  # Global Variable accessible outside out the function
print(x)
