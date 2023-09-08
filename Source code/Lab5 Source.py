######################
# Course: CompSci 120 E 
# Professor: Dr Stefaneli
# Code for lab Activity 5
# Programmer: Samuel Bartholomew
######################

#Declare Variables
userAge = 0
userNumber = 0
userName = ""
userColor = ""
userColorLower = ""
fort1 = "I am sensing... You should go and give your parents a hug!"
fort2 = "I am sensing... You enjoy the cold weather!"
fort3 = "I am sensing... That your left knee is hurting! You should get that checked out."
fort4 = "I am sensing... There is a reason you need a yes or no, the answer is YES!"
fort5 = "I am sensing... You do not know where your jacket is!"
fort6 = "I am sensing... That you should go on a nice walk and relax!"
fort7 = "I am sensing... Your favorite animal is a cat!"
fort8 = "I am sensing... That you need to go and drink a nice glass of water!"
fort9 = "I am sensing... You are very bored and need something fun to-do! Have a party!"
#Program Purpose - Fortune teller program
print("I will be your fortune teller today, I will need your name, your age, your favorite color, and your lucky number.\nI hope you are ready to play!")
userAge = int(input("First I will need your age. \n\tPlease enter your age in numbers: "))
userName = input("How rude of me not getting your name before asking your age. \n\tPlease enter your name: ")
userColor = input("Which of these colors are your favorite? \n\tRed?    \tBlue?   \tGreen?  \n\tYellow? \tOrange? \tPurple? \n\tBrown?  \tBlack?  \tYuck None!\n#################################################################\n#################################################################\n\t Which from above from the list of colors, do you like the most?: ")
userNumber = int(input("\nLastly pick your luckiest number.\n\t Please enter your favorite number: "))
userColorLower = userColor.lower()
print('')
print(" _______  _______  _        _______           _        _______ __________________ _        _______   ")
print('(  ____ \(  ___  )( \      (  ____ \|\     /|( \      (  ___  )\__   __/\__   __/( (    /|(  ____ \ ')
print('| (    \/| (   ) || (      | (    \/| )   ( || (      | (   ) |   ) (      ) (   |  \  ( || (    \/ ')
print('| |      | (___) || |      | |      | |   | || |      | (___) |   | |      | |   |   \ | || |   ')   
print('| |      |  ___  || |      | |      | |   | || |      |  ___  |   | |      | |   | (\ \) || | ____ ') 
print('| |      | (   ) || |      | |      | |   | || |      | (   ) |   | |      | |   | | \   || | \_  ) ') 
print('| (____/\| )   ( || (____/\| (____/\| (___) || (____/\| )   ( |   | |   ___) (___| )  \  || (___) | ') 
print('(_______/|/     \|(_______/(_______/(_______)(_______/|/     \|   )_(   \_______/|/    )_)(_______) ') 
print('                         ')                                                                           
if userAge < 18:
    #print("Less Than 18")
    if userColorLower[:3] == "red":
        print("Your fortune is Fortune #2\n\t"+fort2)
    elif userColorLower[:3] == "blu":
        print("Your fortune is Fortune #1\n\t"+fort1)
    else:
        if(userNumber >=62):
            print("Your fortune is Fortune #4\n\t"+fort4)
        else:
            print("Your fortune is Fortune #3\n\t"+fort3)
elif userAge == 18:
    if userNumber == 2:
        print("Your fortune is Fortune #9\n\t"+fort9)
    else:
        print("Your fortune is Fortune #8\n\t"+fort8)
elif userAge > 18:
    if userColorLower[:3] == "gre":
        if userNumber >8:
            print("Your fortune is Fortune #6\n\t"+fort6)
        else:
            print("Your fortune is Fortune #5\n\t"+fort5)
    else:
        print("Your fortune is Fortune #7\n\t"+fort7)

print("Programmed by: Samuel Bartholomew")
