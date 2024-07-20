def main():
    name = input("Please enter your name")
    print(f"Hello {name}, let's explore this thing")
    menu()


def print_menu():
    print("Main Menu")
    print("1 - Load Dataset one")
    print("2 - Load Dataset two")
    print("3 - Compare average temperatures")
    print("4 - Dates above threshold temperature")
    print("5 - Highest Historical dates")
    print("6 - Change start and end dates for dataset one")
    print("7 - Change start and end dates for dataset two")
    print("9 - Exit")


def menu():

    while True:
        print_menu()
        try:
            selection = int(input("What is your choice"))
        except ValueError:
            print("Please enter a number")
            continue

        match selection:
            case 1:
                print("I am loading one")
            case 2:
                print("I am loading two")
            case 3:
                print("I am compare average temperatures")
            case 4:
                print("Please enter start and end dates for dataset one")
            case 5:
                print("Please enter start and end dates for dataset two")
            case 6:
                print("Please enter start and end dates for dataset one")
            case 7:
                print("Please enter start and end dates for dataset two")
            case 9:
                print("Bye!")
                break
            case _:
                print("Please enter a valid choice")


if __name__ == '__main__':
    main()
