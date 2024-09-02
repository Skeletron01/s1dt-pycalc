def application():
    opperation = input("What calculation would you like to perform? ")
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))

    if opperation == "+":
        answer = value1 + value2
        print("Answer is " + str(answer))
    elif opperation == "-":
        answer = value1 - value2
        print("Answer is " + str(answer))
    elif opperation == "*":
        answer = value1 * value2
        print("Answer is " + str(answer))
    elif opperation == "/":
        answer = value1 / value2
        print("Answer is " + str(answer))
    

    restart = input("Would you like to use the calculator again? ")

    if restart == "y":
        application()
    elif restart == "n":
        print("Thankyou for using my calculator!")


application()