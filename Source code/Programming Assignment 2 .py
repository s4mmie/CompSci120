################################################################################
#
# CMSCI 120 E: Introduction to Computer Science I
# Programmer: Samuel Bartholomew
# Assignment Due Date: Septermber 22nd 2023
# Activity: Programming Assignment #2, Using Conditional Logic to Alter Program Execution
#
# Problem: Write a program, customized to the user, which performs two different conversion
#          calculations between the three domain units. (ounces / milliliters / tablespoons)
#
# Algorithms used: multiplication
#                 -Ounces -> milliliters is multiply the volume value by 29.574
#                 -Ounces -> Tablespoons is multiply the volume value by 2
#                 -Tablespoons -> milliliters is multiply the volume value by 14.787
#
#                  division
#                 -Tablespoons -> ounces is divide the volume value by 2
#                 -Milliliter -> tablespoons is divide the volume value by 14.787
#                 -Milliliters -> ounces is divide the volume value by 29.574
################################################################################

    

# Assigning variables to hold data
userName = ""
userValue = "" #initilaze as a string but will be converted into a float after spaces removed and checked.

userConvertChoice = ""
userConvertTo = ""

userConvertString = ""
userConvertToString = ""

convertValue = 0.0

convertString = ""

mLConversionRate = 29.574
tbsConversionRate = 14.787

errorString = "\n" + "################################################################################################" + "\n" + "################################################################################################"

stringFilter = "1234567890"
stringToList = []
def calculateValue(userConvertTo, userConvertChoice, userValue):
    if(userConvertTo[:1] == "0"):
        userConvertToString = "Ounce(s)"
        if(userValue == 0):
            convertValue = 0 
        else:
            if(userConvertChoice[:1] == "0"):
                convertValue = userValue #oz to oz
                
            elif(userConvertChoice[:1] == "1"):
                convertValue = userValue / mLConversionRate #ml to oz
                
            elif(userConvertChoice[:1] == "2"):
                convertValue = userValue / 2 #tbs to oz
            
    elif(userConvertTo[:1] == "1"):
        userConvertToString = "Milliliter(s)"
        
        if(userValue == 0):
            convertValue = 0 
        else:
            if(userConvertChoice[:1] == "0"):
                convertValue = userValue * mLConversionRate #oz to ml
                
            elif(userConvertChoice[:1] == "1"):
                convertValue = userValue #ml to ml
                
            elif(userConvertChoice[:1] == "2"):
                convertValue = userValue * tbsConversionRate#tbs to ml
    elif(userConvertTo[:1] == "2"):
        userConvertToString = "Tablespoon(s)"
        
        if(userValue == 0):
            convertValue = 0 
        else:
            if(userConvertChoice[:1] == "0"):
                convertValue = userValue * 2 #oz to tbs
                
            elif(userConvertChoice[:1] == "1"):
                convertValue = userValue / tbsConversionRate #ml to tbs
                
            elif(userConvertChoice[:1] == "2"):
                convertValue = userValue #tbs to tbs
    return convertValue, userConvertToString
def takeUserValue():
    #Get value and test to make sure it as a float
    userValue = input ("\n\tWhat is the amount you would like to convert: ")
    userValue = userValue.replace(" ", "")
    stringToList = list(filter(lambda userValue: userValue in stringFilter, userValue)) #This will take the string userValue and filter the string 
    userValue = "".join(stringToList)                                                   #with the filter i set so only numbers can be entered
    try:
        userValue = float(userValue) #Convert String of numbers into a float
    except ValueError:
        print("\nThe value your provided was not a number.\nYou will be asked again please be sure to enter a number.")
        userValue = takeUserValue()
    return userValue
#This is a function for doing the conversions
def convertUnit(userName):
    #Get value and test to make sure it as a float
    userValue = takeUserValue()
    #Get convert choice
    print("\n\tThe choices are Ounces[0], Milliliters[1], or Tablespoons [2].\n\tYou should enter a 0, 1 or 2.")
    userConvertChoice = input("\t\tWhich unit was entered above: ")
    userConvertChoice = userConvertChoice.replace(" ", "")#This will remove spaces typed by the user
    
    #Check user choice
    if(userConvertChoice[:1] == "0" or userConvertChoice[:1] == "1" or userConvertChoice[:1] == "2"):
        userValue = userValue #Do nothing to continue
    else:
        print(errorString + "\n\nYou have entered a unit choice that was not.\nNext time please enter 0, 1, or 2.\nThe program will now end.")
        exit()
    #Get covert to choice
    print("\n\tThe choices are Ounces[0], Milliliters[1], or Tablespoons [2].\n\tYou should enter a 0, 1 or 2.")
    userConvertTo = input("\t\tWhich unit would you like to conver to: ")
    userConvertTo = userConvertTo.replace(" ", "")#This will remove spaces typed by the user
    
    #Check covert to choice
    if(userConvertTo[:1] == "0" or userConvertTo[:1] == "1" or userConvertTo[:1] == "2"):
        userValue = userValue #do nothing to continue
    else:
        print(errorString + "\n\nYou have entered a unit choice that was not.\nNext time please enter 0, 1, or 2.\nThe program will now end.")
        exit()
        
    #Conversions
    if(userConvertChoice[:1] == "0"):
        userConvertString = "Ounce(s)"
    elif(userConvertChoice[:1] == "1"):
        userConvertString = "Milliliter(s)"
    elif(userConvertChoice[:1] == "2"):
        userConvertString = "Tablespoon(s)"
        
    convertValue, userConvertToString = calculateValue(userConvertTo, userConvertChoice, userValue)
    #dislpay to user what values they have now.
    print("\n\n\tHello " + userName + ", " + str(userValue) + " " + userConvertString + "is equal to " + str(convertValue) + " " + userConvertToString)
    return 0
    
#Print Program Purpose to user
print("This program will convert a number given by you, representing an Ounce, Milliliter, or Tablespoon.\n\tThe conversion will be of the two liquid amounts that you do not choose.")

#Get User's name
userName = input("\n\t What is your name: ")

for i in range(2) :
    print("Conversion #" + str(i+1))
    convertUnit(userName)
    
print("\n\nProgrammer: Samuel Bartholomew")



