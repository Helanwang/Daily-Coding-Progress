total = 1
while total <= 20:
    if total % 2 == 1:
        print(total)

    total += 1

# output: printed out all the odd numbers from 1 - 20


total = 1
while total <= 30:
    if total % 2 == 0:
        print(total)

    total += 1

# output: printed out all the even numbers from 1 - 30 [2, 4, 8, 10...]


user_input = str(input("please type begin to start the program"))

while user_input != "begin":  # only if the requirement is not met, it will enter the loop.
    user_input = str(input("please enter again"))

print("The while loop condition has been met.")  # if the user type "begin", it will not enter the loop


"""
Sum of odd numbers
Write a program that reads two integer values, n1 and n2. Use a while loop to calculate the sum of odd numbers between
 n1 and n2 (inclusive of n1 and n2). Remember, a number is odd if number % 2 != 0.
"""


