calculations = [] #create the list to save calculations to memory

def collectCalculation(): #function to select opperation
    value1 = int(input("Enter the first number: ")) #ask for the first number
    opperation, value2 = validateOpperation() #calls validate opperation function and stores returned values as 'opperation' & 'value2'
    return value1, opperation, value2

def validateOpperation():
    while True:
        opperation = collectOpperation()
        if opperation in "+-*/": #checks if the opperation is valid
            value2 = int(input("Enter the second number: ")) #asks for the second number
            return opperation, value2
        elif opperation == "?": #opens the help prompt if the user types '?'
            print("Valid opperations are + (add), - (subtract), * (multiply), / (divide). Type 'H' to view history")
        else: # if the opperation selected is not valid
            print("The opperation you selected is not valid. Type ? for help")


def calculate(): #function to collect the calculation from the user
    value1, opperation, value2 = collectCalculation()

    #if statement to select the correct opperation depending on the given opperation
    if opperation == "+":
        answer = value1 + value2
        print("Answer is " + str(answer)) #addition
    elif opperation == "-":
        answer = value1 - value2
        print("Answer is " + str(answer)) #subtraction
    elif opperation == "*":
        answer = value1 * value2
        print("Answer is " + str(answer)) #multiplication
    elif opperation == "/":
        answer = value1 / value2
        print("Answer is " + str(answer)) #division
    
    calculations.append(str(value1) + opperation + str(value2)) #adds calculation to memory
    print('Calculation ' + str(value1) + opperation + str(value2) + ' stored to memory') #states that the calculation was saved to memory
    restart = input("Would you like to use the calculator again? ") #asks if they would like to use it again

    if restart == "y" or "yes": #either exits the app or runs the function again
        menu()
    elif restart == "n" or "no":
        exit()

def collectOpperation():
    opperation = input("What calculation would you like to perform? ") #ask for the opperation
    return opperation

def menu(): #function for the menu of the application
    print("Welcome to the calculator. Please select from the following options")
    print("1: Preform a calculation")
    print("2: View history")
    print("3: Help")
    print("4: Exit")
    selection = (input("What would you like to do? "))
    if selection == "1":
        calculate()
    elif selection == "2":
        print("The previous calculations performed this session are: ")
        for item in calculations:
            print(item)
        menu()
    elif selection == "3":
        print("Help menu")
        print("You are in the main menu, Select an option by pressing the corresponding number on your keyboard followed by the enter or return key")
        menu()
    elif selection == "4":
        exit()
    else:
        print("unknown option")
        menu()


def exit():
    print("Thank you for using my calculator!")

menu() #runs the function for the first time
