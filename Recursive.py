def square(n):
    return n**n


print(square(10))


def sum1(a, b):
    return a+b


print(sum1(5, 6))


def countdown(x):  # x = 50, x = 49.
    if x == 0:
        return x
    else:
        print(x)  # x = 50
        return countdown(x-1)  # x = 50 - 1, x = 49. call to the beginning of the function


countdown(50)


def recursion(k):
    if k > 0:
        print(k)
        return recursion(k-1)
    else:
        print("recursion finished")


recursion(10)
