x = "This is Helen"
print(x[0])
print(x[1])

"""
T
h
"""

for x in "banana":
    print(x)

"""
b
a
n
a
n
a
"""

txt = "I love you"
print("love" in txt)


"""
True
"""


txt1 = "I love you too"
if "love" in txt1:
    print("That is really cute!")  # Output: That is really cute!


txt2 = "Why does this matter?"
if "love" not in txt2:
    print("It does not matter")  # It does not matter

