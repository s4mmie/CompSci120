import os
################################################################################
#
# CMSCI 120 E: Introduction to Computer Science I
# Programmer: Samuel Bartholomew
# Assignment Due Date: 12/14/2023
# Activity: Final Exam Activity: Importing and Analyzing Text Data from External Files
#
# Problem:  Write a program (custom functions are optional; see
#           below) that will evaluate and display each word in the
#           text file to check for the presence of single-instances of
#           all English vowels in the specific order of “A E I O U,”
#           even if there are letters in between the vowels. If the word
#           has more than one of any of the vowels, the program should capture all vowels, but this student
#           word would not be part of the displayed words.
################################################################################

def displayPurpose():
    print("This program will filter through a file given by the user for a filter given by the user.\nThe default filter will be AEIOU but the user may change that if they wish.")

def listFile():
    while 1:
        inputFile = input("Please provide the data file's name (EXAMPLE - wordList.txt): ")
       
        #ensure that the file is correct and if not keep looping
        try:
            listFileObj = open(inputFile,"r")
            break
        except FileNotFoundError:
            print("The file you provided is not in the directory. Please provide a file in the directory to use as the data file.\n")
    return listFileObj

def checkAEIOU(file, charFilter):
    charFilter = charFilter.lower()
    for line in file:
        word = line.strip()
        #Skip the word if the word is less than 7 characters
        if len(word) < 7:
            continue
        
        index = 0
        found = 0
        filterCount = []
        checkWord = 0
        
        #Go through each character of the filter and check how many times each letter in the filter occurs
        for i in charFilter:
            found = 0
            for j in word:
                if j.lower() == i:
                    found += 1
            filterCount.append(found)
            
        #check to see if every index in filtercount is equal to 1 meaningt here is only 1 "A" "E" "I" "O" "U"
        for x in filterCount:
            if x == 1:
                checkWord += 1
        #This will check to make sure to check the words that have one of each then check them in order and if the amounts are the same that
        #means that the word matches the filter
        if checkWord == len(filterCount):
            found = 0
            checker = 0
            #loop through characters in word
            for char in word:
                if char.lower() == charFilter[found]:
                        found += 1
                        checker += 1
                        if found > len(filterCount)-1:
                            found = len(filterCount)-1
            #print the word if the checker and check word are the same meaning the word is in the filters order
            if checker == checkWord:
                print("Found: ", word)

                
def main():
    # Declare/Initialize Variables
    fileDir = os.listdir()
    
    #If the file is main.py remove it from the list
    fileDir.remove("main.py")

    i=0
    
    #displayPurpose
    displayPurpose()
    
    print("\n===========Files in the directory===========")
        #Loop through the file directory
    for file in fileDir:
        i += 1
        #print the iteration + the file name
        print(str(i)+": "+file)
    print("============================================\n")
    
    #get the file obj
    listFileObj = listFile()
    
    #ask the user for a filter
    charFilter = input("Please input the filter you would like to use (EXAMPLE - AEIOU): ")
    charFilter = charFilter.strip()
    
    #check to make sure the filter is only letters, and is longer than one character long.
    if charFilter.isalpha():
        if len(charFilter) >= 1:
            charFilter = charFilter
        else:
            print("The filter you entered was too short. AEIOU will be used.")
            charFilter = "AEIOU"
    else:
        print("The filter you inputed was not all letters. AEIOU will be used.")
        charFilter = "AEIOU"
    print(f"\nSearching through the list with the filter of {charFilter}.\n============================================")
    
    #Check AEIOU function with file obj and filter
    checkAEIOU(listFileObj, charFilter)
    
main()
    
    
    
    
    
    
        
'''   CODE FOR AEIOU STATIC NOT DYNAMIC     
        for char in word:
            if char == cFilter[index]:
                if index < len(cFilter)-1:
                    index += 1
            

            if char.lower() == "a":
                a += 1
                
            if char.lower() == "e":
                if a == 0:
                    continue
                e += 1
            if char.lower() == "i":
                if a == 0 or e == 0:
                    continue
                i += 1
            if char.lower() == "o":
                if a == 0 or e == 0 or i == 0:
                    continue
                o += 1
            if char.lower() == "u":
                if a == 0 or e == 0 or i == 0 or o == 0:
                    continue
                u += 1
            #print(a, e, i, o, u)
            if a == 1 and e == 1 and i == 1 and o == 1 and u == 1:
                print(word)'''
    
