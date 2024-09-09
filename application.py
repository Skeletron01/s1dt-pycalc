import tkinter as tk #import external module tkinter

root = tk.Tk()


root.geometry("500x700") #set window size to 500x700px

root.title("calculator-(OAC-P2)")


helpButton = tk.Button(root, text="?")
helpButton.pack(pady=5)

typeInput = tk.Entry(root)
typeInput.pack(pady=10)

keypad = tk.Frame(root)
keypad.columnconfigure(0, weight=1)
keypad.columnconfigure(1, weight=1)
keypad.columnconfigure(2, weight=1)
keypad.columnconfigure(3, weight=1)
keypad.columnconfigure(4, weight=1)
keypad.columnconfigure(5, weight=1)



#Numpad keys for 0-9 + 00 & .
key1 = tk.Button(keypad, text="1")
key1.grid(row=4, column=0, sticky=tk.W+tk.E)
key2 = tk.Button(keypad, text="2")
key2.grid(row=4, column=1, sticky=tk.W+tk.E)
key3 = tk.Button(keypad, text="3")
key3.grid(row=4, column=2, sticky=tk.W+tk.E)
key4 = tk.Button(keypad, text="4")
key4.grid(row=3, column=0, sticky=tk.W+tk.E)
key5 = tk.Button(keypad, text="5")
key5.grid(row=3, column=1, sticky=tk.W+tk.E)
key6 = tk.Button(keypad, text="6")
key6.grid(row=3, column=2, sticky=tk.W+tk.E)
key7 = tk.Button(keypad, text="7")
key7.grid(row=2, column=0, sticky=tk.W+tk.E)
key8 = tk.Button(keypad, text="8")
key8.grid(row=2, column=1, sticky=tk.W+tk.E)
key9 = tk.Button(keypad, text="9")
key9.grid(row=2, column=2, sticky=tk.W+tk.E)
key0 = tk.Button(keypad, text="0")
key0.grid(row=5, column=0, sticky=tk.W+tk.E)
key00 = tk.Button(keypad, text="00")
key00.grid(row=5, column=1, sticky=tk.W+tk.E)
keyDP = tk.Button(keypad, text=".")
keyDP.grid(row=5, column=2, sticky=tk.W+tk.E)


#numpad keys for opperations

keyPlus = tk.Button(keypad, text="+")
keyPlus.grid(row=5, column=3, sticky=tk.W+tk.E)
keyMinus = tk.Button(keypad, text="-")
keyMinus.grid(row=4, column=3, sticky=tk.W+tk.E)
keyTimes = tk.Button(keypad, text="x")
keyTimes.grid(row=3, column=3, sticky=tk.W+tk.E)
keyDivide = tk.Button(keypad, text="÷")
keyDivide.grid(row=2, column=3, sticky=tk.W+tk.E)
keyEqual = tk.Button(keypad, text="=")
keyEqual.grid(row=5, column=4, sticky=tk.W+tk.E)
keySquare = tk.Button(keypad, text="x²")
keySquare.grid(row=4, column=4, sticky=tk.W+tk.E)
keySqRoot = tk.Button(keypad, text="√")
keySqRoot.grid(row=3, column=4, sticky=tk.W+tk.E)



#Numpad keys misc.
keyClear = tk.Button(keypad, text="C")
keyClear.grid(row=2, column=4, sticky=tk.W+tk.E)


keypad.pack(fill='x')





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


root.mainloop()
