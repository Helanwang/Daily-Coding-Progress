# Scope: a region that a variable is recognized
# Local Scope: A variable created inside the function, and can only being used within the Function
# Global Scope: The variable is created within the module, it is available at all scopes(both global and local)

# Local Scope

def my_function():
    x = 300
    print(x)


my_function()


# Global Scope

y = 400  # Global Variable


def my_function1():
    print(y)


print(y)


my_function1()
