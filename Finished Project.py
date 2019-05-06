#Car Sales Application

def menu_function():
    print("Welcome to Alex's Vehicle Shop! What would you like to do?")
    print("1. Purchase Vehicle")
    print("2. End program")

def totalPrice_function(selectInput, colourInput):
    totalPrice = selectInput + colourInput
    return totalPrice

vehicle = {"1":2000, "2":4000}
color = {"1":250, "2":200}

file = open("application.txt","w")
file.close()

userExit = False
while(userExit == False):
    menu_function()
    userInput = input("enter a selection: ")
    if(userInput == "2"):
        userExit = True
    elif(userInput == "1"):
        print("Would you like to purchase a 'car' or 'truck'? ")
        print("1. car")
        print("2. truck")
        while(True):
            selectInput = input("enter a selection: ")
            if(selectInput == "1"):
                print("You have chosen a car")
                break
            elif(selectInput == "2"):
                print("You have chosen a truck")
                break
            else:
                print("please type '1' or '2'")
        print("What colour would you like your vehicle to be?")
        print("1. blue")
        print("2. black")
        while(True):
            colourInput = input("enter a selection: ")
            if(colourInput == "1"):
                print("you have chosen your vehicle to be colour'd blue")
                break
            elif(colourInput == "2"):
                print("you have chosen your vehicle to be colour'd black")
                break
            else:
                print("please type '1' or '2'")
        print("the price is $" + str(totalPrice_function(vehicle[selectInput], color[colourInput])))
        file = open("application.txt","a")
        file.write("would you like to purchase a 'car' or 'truck'?\n")
        file.write("1. car\n")
        file.write("2. truck\n")
        file.write(selectInput)
        file.write("\nWhat colour would you like your vehicle to be?\n")
        file.write("1. blue\n")
        file.write("2. black\n")
        file.write(colourInput)
        file.write("\nthe price is $" + str(totalPrice_function(vehicle[selectInput], color[colourInput])))
        file.write("\n")
        file.close()
    else:
        print("please type '1' or '2'")

    
