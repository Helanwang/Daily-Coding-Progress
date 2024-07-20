def main():
    user = int(input("Enter a number: "))
    while user > 100:
        print("Number is too big")
        user = int(input("Try a smaller number: "))
        if user <= 100:
            print("That's good")
            break


if __name__ == '__main__':
    main()
