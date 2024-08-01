n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

total_1 = 0
total_2 = 0

while total_1 <= n1:
    if total_1 % 2 == 1:
        print(total_1)

    total_1 += 1

while total_2 <= n2:
    if total_2 % 2 == 1:
        print(total_2)

    total_2 += 1

print(total_1 + total_2)

# this code might be not correct. don't refer maybe
