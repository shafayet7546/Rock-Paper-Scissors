from random import randint

UserScore = 0
ComputerScore = 0

#computer selects their choice from: Rock, Paper or Scissor
def ComputerPick():
    return(randint(1,3))

#function checks whether ComputerInput satisfies given conditions, and returns designated string representation
def ConvertString1(C):
    if(C == 1):
        return ("Rock")
    elif(C == 2):
        return ("Paper")
    elif(C == 3):
        return ("Scissors")
    else:
        return ("Invalid input")

#function checks whether UserInput satisfies given conditions, and returns designated string representation
def ConvertString2(U):
    if(U == 1):
        return ("Rock")
    elif(U == 2):
        return ("Paper")
    elif(U == 3):
        return ("Scissors")
    else:
        return ("Invalid input")

#function checks whether computer or user won
def GuessCheck(C, U):
    if ((C == 1) and (U == 2)) or ((U == 1) and (C == 3)) or ((C == 2) and (U == 3)):
        return True
    elif ((C == 1) and (U == 3)) or ((C == 2) and (U == 1)) or ((C == 3) and (U == 2)):
        return False
    else: 
        return "1"

#returns 'true' if user won
#returns 'false' if user lost
#returns '1' when draw

#main
def main():

    #1: Rock
    #2: Paper
    #3: Scissors

    print("Let's play Rock Paper Scissors!")
    UserInput = int(input("Select your choice by entering the number 1, 2, or 3 as shown below... \n 1. Rock \n 2. Paper \n 3. Scissors \n"))  #takes int input, and stores in 'UserInput'
    ComputerInput = ComputerPick()                            #calls function 'ComputerPick' and stores returned value in ComputerInput
    global UserScore
    global ComputerScore
    

    if((GuessCheck(ComputerInput, UserInput) == "1")):        #If '1' is received from function 'GuessCheck', it is a draw.
        ConvertComputer = ConvertString1(ComputerInput)       #Converts int to desired string representation: "Rock", "Scissor", or "Paper"
        ConvertUser = ConvertString2(UserInput)
        print("Wow! Your choice of:", ConvertUser, "drawed against", ConvertComputer,". No Points awarded. \nCurrent Score: \nYou =", UserScore, "Computer =", ComputerScore)
        UserDecision = str(input("Do you want to play again? Say 'yes' to continue! "))
        
        if(UserDecision.lower() == "yes"):                    #checks if user wants to continue. If so, loop main
            main()
        else:                                                 #if false, prints final scores and the winner of session
            if(ComputerScore > UserScore):
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **Computer is the winner of this session**")
            elif(ComputerScore == UserScore):
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **No one is the winner of this session**")
            else:
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **You are the winner of this session**")
            #print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore)
    
    elif (GuessCheck(ComputerInput, UserInput)):              #checks for 'True', then asks user whether they want to continue or not
        ConvertComputer = ConvertString1(ComputerInput)       #Converts int to desired string representation: "Rock", "Scissor", or "Paper"
        ConvertUser = ConvertString2(UserInput)
        UserScore = UserScore + 1
        print("Congratz! Your choice of:", ConvertUser, "won against", ConvertComputer, "and earned +1 point. \n Current Score: \n You =", UserScore, "Computer =", ComputerScore)
        UserDecision = str(input("Do you want to play again? Say 'yes' to continue! "))

        if(UserDecision.lower() == "yes"):                    #if true, loops main
            main()
        else:                                                 #if false, prints final scores and the winner of session
            if(ComputerScore > UserScore):
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **Computer is the winner of this session**")
            elif(ComputerScore == UserScore):
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **No one is the winner of this session**")
            else:
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **You are the winner of this session**")

    else:
        ConvertComputer = ConvertString1(ComputerInput)
        ConvertUser = ConvertString2(UserInput)
        ComputerScore = ComputerScore + 1                                                     
        print("You lost! Your choice of:", ConvertUser, "lost against", ConvertComputer, ". You earned 0 points, and computer earned 1 point. \nCurrent Score: \nYou =", UserScore, "Computer =", ComputerScore)
        UserDecision = str(input("Do you want to play again? Say 'yes' to continue! "))
        
        if(UserDecision.lower() == ("yes")):                  #checks if user wants to continue or not
            main()
        else:                                                 ##if false, prints final scores and the winner of session
            if(ComputerScore > UserScore):
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **Computer is the winner of this session**")
            elif(ComputerScore == UserScore):
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **No one is the winner of this session**")
            else:
                print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore, "\n **You are the winner of this session**")
            #print("Thank you for playing! \nFinal Score =", UserScore, "Computer =", ComputerScore)

main()
