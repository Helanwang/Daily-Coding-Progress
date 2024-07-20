
def exercise_1():
    user = int(input("Enter a number: "))
    if user > 100:
        while user > 100:
            print("Number is too big")
            user2 = int(input("try a smaller number"))
            if user2 < 100:
                print("That's good")
                break
    else:
        print("Number is good")


def exercise_2():
    while True:
        try:
            user = int(input("Enter a number between 10 and 50: "))
            if user < 10 or user > 50:
                print("Number is out of range. Please try again.")
            else:
                print("That's good")
                break
        except ValueError:
            print("That's not an integer. Please enter a valid integer.")


exercise_2()
