######################
#
# Code for Programming Assignment #1
#
######################

# Assigning variables to hold data
whichDir = ""
weightAm = 0 

#Definition to check the "direction" of which conversion
def checkDir():
    whichDir = input("Enter 0 or 1 : ") #Taking user input
    
    if whichDir == "1":
        return 1 #Exit definition and return 1
    elif whichDir == "0":
        return 0 #Exit definition and return 0
    print("Please use a valid number try again \n #######################")
    Start() #Restart the program if the user input was not correct
    

def Start():
    print ('Will you be converting to [0] Cups to Ounces or [1] Ounces to Cups')
    whichDir = checkDir() #store whichDir from checkDir
    
    if whichDir == 0:
        print("How many cups would you like to convert to ounces.")
        weightAm = input("How many cups : ") #Take the amount of cups
        weightAm = int(weightAm)
        weightAm = weightAm * 8
        print("Programmer: Samuel Bartholomew\n\t Course: Computer Science 120")
        print("You have " + str(weightAm) + " ounces from your cup(s).")
    if whichDir == 1:
        print("How many ounces would you like to convert to cups.") 
        weightAm = input("How many ounces : ") #Take the amount of ounces
        weightAm = float(weightAm)
        weightAm = weightAm / 8
        print("Programmer: Samuel Bartholomew\n\t Course: Computer Science 120")
        print("You have " + str(weightAm) + " cups from your ounce(s).")
Start()

