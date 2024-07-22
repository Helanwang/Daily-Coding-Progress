def determine_age_group():
    try:
        age = int(input("Enter your age: "))
        if age < 12:
            print("You are a child")
        elif 13 < age < 18:
            print("You are a teenager")
        elif 20 < age < 59:
            print("You are a adult")
        elif age > 60:
            print("You are a senior")
    except ValueError:
        print("Please enter an integer")


def grading():
    try:
        letter_grade = int(input("Enter your letter grade: "))
        if 90 <= letter_grade <= 100:
            print("You got A")
        elif 80 <= letter_grade <= 90:
            print("You got B")
        elif 70 <= letter_grade <= 80:
            print("You got C")
        elif 60 <= letter_grade <= 70:
            print("You got D")
        elif 60 >= letter_grade:
            print("You got F")
        else:
            print("You got invalid grade")
    except ValueError:
        print("Please enter an integer")


def body_weights():
    try:
        body = int(input("Enter your body weight: "))
        if body < 18.5:
            print("You are underweight")
        elif 18.5 <= body <= 24.9:
            print("You have normal weights")
        elif 24.9 <= body < 29.9:
            print("You are overweight")
        elif body >= 30:
            print("You have fucking Obesity")
        else:
            print("This is not a valid input")
    except ValueError:
        print("Please enter an integer")


def weather():
    try:
        temp = int(input("Enter your temperature: "))
        if temp < 0:
            print("It's freezing outside")
        elif 0 < temp < 10:
            print("It's Cold outside")
        elif 10 < temp < 20:
            print("that is warm")
        elif 20 < temp < 30:
            print("It's hot now")
        else:
            print("It's hot")
    except ValueError:
        print("Please enter an integer")

