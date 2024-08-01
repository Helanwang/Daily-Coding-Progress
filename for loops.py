user_input = str(input("Enter sentence"))

count = 0
for x in user_input:
    if x == " ":
        count += 1

print(count)

user_input1 = str(input("enter something"))

count = 0
vowels = "aeiou"
for y in user_input1:
    if y.lower() in vowels:  # y.lower, just make sure that the input is converted into lower case, so it can count.
        count += 1

print(f"the total vowels is {count}")

''''''
user_input3 = str(input("enter here"))
count = 0

for words in user_input3:
    if words == " ":
        count += 1

print(f"the total space is {count}")
