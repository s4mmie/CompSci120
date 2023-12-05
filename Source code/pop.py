
#q0 [] Push 1 
#q0 [1] Push 0 
#q1 [10] push None
#Go in reverse and pop all
#q1 [1]pop all until empty
#q1 []
#q2 accept

def go_through_file(string, popText, qCount, fName):
    if len(string) > 0:
        null = False
        pop = False
        for char in string:
            textLen = len(popText)-1
            if char == "1":
                if not null:
                    popText = popText[:textLen] + char + popText[textLen:]
            if char == "0":
                if not null:
                    popText = popText[:textLen] + char + popText[textLen:]
            if char == "*":
                qCount += 1
                null = True
                pop = True
            if char == "#":
                qCount += 1
            if pop == True:
                print(char, "q"+str(qCount) ,"None")
                print(char, "q"+str(qCount) ,"None", file = fName)
                break
            elif char == "#":
                print(char, "q"+str(qCount), "Accept")
                print(char, "q"+str(qCount), "Accept", file = fName)
            else:
                print(char, "q"+str(qCount) ,popText)
                print(char, "q"+str(qCount) ,popText, file = fName)
           
        textLen = len(popText)
        i = 0
        reversedPopText = popText[::-1]
        popTextFinal = ""
        
        if pop == True:
            for char in reversedPopText:
                if char != "]":
                    removeFrom = textLen - (i+1)
                    popTextFinal = popText[:removeFrom] + popText[removeFrom + i:]
                    if char != "[":
                        print(char, "q"+str(qCount) ,popTextFinal)
                        print(char, "q"+str(qCount) ,popTextFinal, file = fName)
                    else:
                        print("#", "q"+str(qCount) ,"Accept")
                        print("#", "q"+str(qCount) ,"Accept", file = fName)
                    #print("RemoveFrom: ", removeFrom)
                    i+=1
        popText = popTextFinal
    
        return popText, qCount
    else:
        return 0, 0
            
def main():
    
    FILE_NAME = input("Please provide an output file name: ")
    fileObj = open(FILE_NAME, "a")
    string = input("Please provide a string to parse through (Example 10110*0101#): ")
    qCount = 0 #push count
    popText = "[]" #The pop text 
    popText, qCount = go_through_file(string, popText, qCount, fileObj)
main()
