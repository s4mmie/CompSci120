import string
import os
##########################################################################
#
# CMSCI 120: Introduction to Computer Science I
#   Unit 6, File I/O Single CSV File READ
#   Students: Samuel Bartholomew & Sishir Kanamala
#
# Implementation of code to evaluate data in a CSV file using File Read
#
#   Prints a restricted data set from a data file (elementsFULL.csv);
#   Periodic table data, including atomic number, element symbol, element
#   name, atomic weight, electron orbital pattern, element form in natural
#   state, and type of element form 
#
#   This verion of the program searches for a single data file
#
##########################################################################

#Test case files
#       The periodicTable.txt is a replica of the elementsFULL.csv to show the user can input their own data.
#       The incorrectTable.txt will show if you do not provide enough parameters in the input file, the file will crash when checking.
#       The incorrectOrderTable.txt will show if you do not order the file correctly, the program will crash and tell the user to format correctly.


# Declare/Initialize Variables
fileDir = os.listdir()
#If the file is main.py remove it from the list
fileDir.remove("main.py")

userFileName = ""
stringFilter = '''!()[]{};:'"\,<>/?@#$%^&*~"'''
userMinWeight = ""
userMaxWeight = ""

ELEMENT_DATA_FILE = "elementsFULL.csv"
writeObj = ""
elementObject = ""
line = ""
atomicNumber = ""
atomicWeight = ""
elementName = ""
elementSymbol = ""
orbitPattern = ""
elementForm = ""
elementType = ""

i = 0

#display the program purpose
print("This program will be asking the user to input a properly formatted Periodic Table.\nThe user will then be queried asking how the user would like to sort the atoms by the atomic weight.\nThen all data will be sent to 'filteredDATA.txt'.\n")

print("The files in your programs directory.\nIf you do not see your input file, please stop the program and put your-\ninput file in this programs directory.\n")
#Loop through the file directory
for file in fileDir:
    i += 1
    #print the iteration + the file name
    print(str(i)+": "+file)
    
print('')

#loop until the user provides a valid file to take input data from
while 1:
    #Loop until you get a valid file name
    while 1:
        #Get the user input for a file name
        userFileName = input("Please input your data file that is case sensitive for the Periodic Table (Example - elementsFULL.csv) : ")
        
        #Remove all special characters from the user file that can not be used in a file name
        for char in userFileName:
            if char in stringFilter:
                userFileName = userFileName.replace(char, "")
                
        #If the user has given a name see if it exist in the current directory
        if userFileName != "":
            break
        #Tell the user the entry was invalid and restart this loop
        print("Invalid entry, please do not write symbols in your text file's name.")

    #check to see if the input file is in the directory
    try:
        #Generate the input file object
        elementObject = open(userFileName, "r")
        break
    #If the input file is not in the directory tell the user the file is not found
    except FileNotFoundError:
        print('The input data file was not found, please make sure to provide the file and enter the name correctly.\n')
        
#Generate the write object file
writeObj = open("filteredDATA.txt", "a")

#formatting
print("")

#ask the user for the minimum weight and make sure the returned value is a digit while also making sure that the min weight is less than the max weight
while userMinWeight >= userMaxWeight:
    while 1:
        userMinWeight = input("Please enter the minimum atomic weight you would like to sort: ")
        if not userMinWeight.isdigit():
            print("Please enter a number (Example - 5).\n")
        else:
            break
            
    #ask the user for the maximum weight and make sure the returned value is a digit
    while 1:
        userMaxWeight = input("Please enter the maximum atomic weight you would like to sort: ")
        if not userMaxWeight.isdigit():
            print("Please enter a number (Example - 10).\n")
        else:
            break
        
    #If the min weight is not less than the max weight tell the user what is wrong
    if userMinWeight >= userMaxWeight:
        print("\nPlease make the minimum atmoic weight less than the maximum atmoic weight.\n")
    
#formatting
print("\n")

# Process each line of the data file, line-by-line
for line in elementObject:

    # Remove newline character from each line of the input data file
    line = line.strip()

    #Make sure the input file is returning 7 different inputs per line
    try:
        # Parse each line of the data file data
        atomicNumber, elementSymbol, elementName, atomicWeight, orbitPattern, elementForm, elementType = line.split(",")
    #if the input file is not returning all 7 values tell the user
    except ValueError:
        print("The data file provided is not in the proper format of the base file. Please provide the file in the order provided with commas seperating.\nThe Atmoic Number, Element Symbol, Element Name, Atmoic Weight, Orbit Pattern, ElementForm, and Element Type.")
        break

    #Make sure that the ordering of the file is correct when calling a variable.
    try:
        #make sure the weight is higher than the minimum and lower than the maximum
        if(float(userMinWeight) < float(atomicWeight) and float(userMaxWeight) > float(atomicWeight)):
            #Show which elements are being saved
            print("Saving: ", elementName)
            # Send the same data to an external data file
            writeObj.write(str(elementName)+ "\t\t"+ str(atomicWeight) + "\t\t" + str(elementType) +"\n")
    #if the ordering is incorrect when calling the atmoic weight tell the user the error and exit
    except ValueError:
        print("The data file provided is not in the proper format of the base file. Please provide the file in the order provided with commas seperating.\nThe Atmoic Number, Element Symbol, Element Name, Atmoic Weight, Orbit Pattern, ElementForm, and Element Type.")
        break

# Close the data file before termination
elementObject.close()
writeObj.close()
