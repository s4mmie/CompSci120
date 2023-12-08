import os
import random
from datetime import datetime

################################################################################
#
# CMSCI 120 E: Introduction to Computer Science I
# Programmer: Samuel Bartholomew
# Assignment Due Date: TBD
# Activity: PA #4, Building and Using Data from External Databased Sources
#
# Problem:  You need to create a program to analyze the
#           movie data based on a set of criteria and to
#           display the movie with the highest profit from the collection of movies.
################################################################################

#display program purpose function
def displayPurpose():
    print("This program will parse through a CSV file made for information about movies, and how much the budget was along with the profit.\nThe user will be prompted to give a letter A-Z to use to sort the files.The user will next be asked to take a guess at what the profit and loss will be for the file sorted by the letter. Next using the letter the highest and lowest movie with that data will be given to he user.")
    print("===How to make your own file==")
    print("If you would like to create your own master data file, the format should be the movie's release date Month/Day/Year (EXAMPLE 8/25/1939).\nFollowed by a comman with the next vlaue being the movie's title(EXAMPLE The Wizard of Oz). Followed by a commma the movies budget (EXAMPLE 2777000).\n Lastly followed by a comma and the profit of the movie (EXAMPLE 33711566).")

#Get the user to input the file they would like to use for the master movie csv file
def movieFile():
    while 1:
        inputFile = input("Please provide the data file's name (EXAMPLE - movies.csv): ")
        #ensure that the file is correct and if not keep looping
        try:
            movieFileObj = open(inputFile,"r")
            break
        except FileNotFoundError:
            print("The file you provided is not in the directory. Please provide a file in the directory to use as the data file.\n")
    return movieFileObj

#Get the out file depending on which mode is given
def outputFile(mode):
    if mode == "a":
        outputFileObj = open("specialList.csv","a")
    if mode == "w":
        outputFileObj = open("profitList.csv","w")
    return outputFileObj
        
    
#Output data to a given file 
def outputData(data, fileObj):
    if fileObj.name == "specialList.csv":
        timestamp =datetime.now()
        data = str(timestamp) + "\n" + data
    fileObj.write(data)
    return

#Process the file
def dataProcess(file):
    #variables
    fileContent = []
    
    highestProfit = 0.0
    highestLoss = 10000000000000.0
    
    movieTitle = ""
    lowMovieTitle = ""
    
    releaseDate = ""
    lowReleaseDate = ""
    
    wholeData = ""
    sortedData = ""
    
    guessAmount = ""
    lossGuessamount = ""
    
    i = 0
    #get user input for a char use char to sort title
    while 1:
        letterCheck = input("Please provide the letter you would like to sort the highest profit by: ")
        #Make sure the input is a letter and only one length
        if letterCheck.isalpha():
            if len(letterCheck) == 1:
                break
            else:
                print("Please make sure you are only entering one letter.")
        else:
            print("Please enter a letter from A-Z no numbers or extra symbols please.")
        print("") 
    print("")
    
    #Get the user to input a guess of the highest profit 
    while 1:
        try:
            guessAmount = input("Please guess the amount that will have the highest profit with the movie starting with the letter you provided (EXAMPLE 1210000).: ")
            guessAmount = float(guessAmount)
            break
        except:
            print("Please be sure to provide a number (EXAMPLE 150000).")
            
    #Get the user to input a guess of the highest loss
    while 1:
        try:
            lossGuessamount = input("Please guess the amount that  will have the highest loss with the movie starting with the letter you provided (EXAMPLE -10000).: ")
            lossGuessamount = float(lossGuessamount)
            break
        except:
            print("Please be sure to provide a number (EXAMPLE -100000).")
    #loop through the file line by line
    for line in file:
        i += 1
        #strip the line and append it to filecontent to pick a random line later
        line = line.strip()
        fileContent.append(line)
        #make sure that each line is correctly formmated
        try:
            date, title, budget, earned = line.split(",")
        except ValueError:
            print("The file you have enetered is improperly formatted and missing or has too many additional values per line. Please make sure your file is formatted in this order.\nThe release date, the movie's title, the movie's budget, and how much the movie earned.")
            return 0, 0
        #make sure profit is a float / int to ensure formatting is correct
        try:
            profit = float(earned) - float(budget)
        except ValueError:
            print("The file you have entered has the correct amount of values per line, but the data is in an incorrect order. Please make sure your file is formatted in this order.\nThe release date, the movie's title, the movie's budget, and how much the movie earned.")
            return 0, 0
        #add to the whole data to feed to the text file
        wholeData += date+","+title+","+str(profit)+"\n"
        #check to see if the title has the first letter as the letter given
        if title[0].lower() == letterCheck.lower():
            sortedData += str(date)+","+str(title)+","+str(profit)+"\n"
            #check to see if the current profit is higher than the highest profit so far
            if float(profit) > float(highestProfit):
                highestProfit = profit
                movieTitle = title
                releaseDate = date
            #check to see if the profit / money loss is lower than the biggest loss
            if float(profit) < float(highestLoss):
                highestLoss = profit
                lowMovieTitle = title
                lowReleaseDate = date
    
    #get a random line and store the information into date title budget earned and store the date into month day year
    randomLine = random.randint(0,i-1)
    date, title, budget, earned = fileContent[randomLine].split(",")
    month, day, year = date.split("/")
    
    #store the data to the profitList.csv
    profitListObj = outputFile("w")
    outputData(wholeData,profitListObj)
    profitListObj.close()
    
    #store the sorted data into the specialList.csv
    specialListObj = outputFile("a")
    outputData(sortedData,specialListObj)
    specialListObj.close()
    
    #claculate the difference in your guesses
    highDifference = float(highestProfit) - float(guessAmount)
    lowDifference = float(highestLoss) - float(lossGuessamount)
    
    #display to the user the random file selected
    print("*\n====Picking a random movie to display the information on====*")
    print("\t-Month: ", month)
    print("\t-Day: ", day)
    print("\t-Year: ", year)
    print("\t-Movie Title: ", title)
    print("\t-Movie Budget: ", "$"+str(budget))
    print("\t-Movie Box Office Gross: ", "$"+str(earned))
    print("*============================================================*")
    
    #display the user the highest profit and loss based off the letter sorted and how close the guesses were
    print("\nThe movie with the highest profit with the letter " + letterCheck +" is " +movieTitle+". The movie was released on " + releaseDate + " with a profit of $"+str(highestProfit)+".")
    print("The movie with the highest loss with the letter " + letterCheck +" is " +lowMovieTitle+". The movie was released on " + lowReleaseDate + " with a loss of $"+str(highestLoss)+".")
    print("\tYour guess was for the profit: ", "$"+str(guessAmount), "\tThe highest profit was: ", "$"+str(highestProfit) , "\n\tYou were off for the profit by: ", "$"+str(highDifference))
    print("\tYour guess was for the loss: ", "$"+str(lossGuessamount), "\tThe highest loss was: ", "$"+str(highestLoss) , "\n\tYou were off for the loss by: ", "$"+str(lowDifference))
    
    return highestProfit, movieTitle
    
def main():
        
    # Declare/Initialize Variables
    fileDir = os.listdir()
    
    #If the file is main.py remove it from the list
    fileDir.remove("main.py")

    i=0
    
    #get the programs purpose
    displayPurpose()
    print("\n===========Files in the directory===========")
        #Loop through the file directory
    for file in fileDir:
        i += 1
        #print the iteration + the file name
        print(str(i)+": "+file)
    print("============================================\n")
    
    #call the movie file to store it as an object
    movieFileObj = movieFile()
    
    #get the highets profit and movie title
    highProfit, movieTitle = dataProcess(movieFileObj)
    
    #close the file
    movieFileObj.close()
main()
