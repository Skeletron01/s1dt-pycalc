calculations = [] #create the list to save calculations to memory

def application(): #programme in a function so it can be run indefinatly
    opperation = input("What calculation would you like to perform? ") #ask for the opperation
    value1 = int(input("Enter the first number: ")) #ask for the first number
    value2 = int(input("Enter the second number: ")) #ask for the second number

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

    if restart == "y": #either exits the app or runs the function again
        application()
    elif restart == "n":
        print("Thankyou for using my calculator!")


application() #runs the function for the first time