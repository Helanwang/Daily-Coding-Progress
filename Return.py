def square(x):
    return x*x


result = square(100)
print(result)


def greet(name):
    return f"Hello {name}!"


greeting = greet("John")
print(greeting)


def list_sum(nums):
    return sum(nums)


list1 = list_sum([1, 2, 3, 4, 5])
print(list1)


def add_numbers(x, y):
    return x + y


result1 = add_numbers(123, 65465)
result2 = add_numbers(4564, 564621)
print(result1)
print(result2)


def is_positive(n):
    return n > 0


positive_check = is_positive(-1)
print(positive_check)
