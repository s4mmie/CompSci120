######################
#
# Code for lab Activity 4
# Programmers: Sam, and Jacob
######################

#Declare vars
liquidDict = {
    "cup":0,
    "gal":1,
    "pnt":2,
    "qt":3,
    "l":0,
    "ml":1
}
userName = ""
ounceAmount = 0 
conToUs = [0,0,0,0]#Cups, Gallons, Pints, Quarts
conToMetric = [0,0] #Liter, MilLiter
#Print program purpose
print("This program will be converting ounces into all liquid forms in metric and US units.")
userName = input("\n\tPlease provide your name: ")
ounceAmount = float(input("\tPlease provide the number of ounces you would like to convert: "))

for i in range(0,6): #For loop for all of the conversions 
    conversionRate = 0
    if i == 0:
        conversionRate = float(ounceAmount) / 8
    if i == 1:
        conversionRate = float(ounceAmount) / 128
    if i == 2:
        conversionRate = float(ounceAmount) / 16
    if i == 3:
        conversionRate = float(ounceAmount) / 32
    if i == 4:
        conversionRate = float(ounceAmount) / 33.814
    if i == 5:
        conversionRate = float(ounceAmount) * 29.574
    if i <= 3:
        conToUs[i] = conversionRate
        #print(conToUs[i]) Debugging
    elif i > 3:
        conToMetric[i-4] = conversionRate
        #print(conToMetric[i-4]) Debugging

print("\n######################################################################################################\n\nConversions for " + userName)
print("US Units \t" + str(ounceAmount) + "oz. = Cup(s): " + str(conToUs[liquidDict["cup"]]) + "\t Pint(s): " + str(conToUs[liquidDict["pnt"]]) + "\t Gallon(s): " + str(conToUs[liquidDict["gal"]]) + "\t Quart(s): " + str(conToUs[liquidDict["qt"]]))
print("Metric Units\t" + str(ounceAmount) + "oz. = Liter(s): " + str(conToMetric[liquidDict["l"]]) + "\t MilLiter(s): " + str(conToMetric[liquidDict["ml"]]))
print("\n\n Programmers: Samuel and Jacob")




