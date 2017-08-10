import random
tie = 0
win = 0
lost = 0
playgame = True

print("Let's play Rock,Paper,Scissors.")
while playgame == True:
    
    computerChoice = random.randint (1,3)
    if computerChoice == 1:
        computerChoice = "rock"
    elif computerChoice == 2:
        computerChoice = "paper"
    elif computerChoice == 3:
        computerChoice = "scissors"

    print("What's your choice r, p, or s?")
    print("or q to quit")


    playerChoice = input()
    if playerChoice == "r":
        playerChoice = "rock"
        print("You chose rock.")
    elif playerChoice == "p":
        playerChoice = "paper"
        print("You chose paper.")
    elif playerChoice == "s":
        playerChoice = "scissors"
        print("You chose scissors")
    elif playerChoice == "q":
        print("Thanks for playing Rock,Paper,Scissors!")
        playgame = False
    print ("The computer randomly picked " + (str)(computerChoice) + ".")

    if playerChoice == computerChoice:
        print ("You have tied.")
        tie +=1

    elif playerChoice == "rock" and computerChoice == "scissors":
        print ("You have won!")
        win +=1
        
    elif playerChoice == "paper" and computerChoice == "rock":
        print ("You have won!")
        win += 1
        
    elif playerChoice == "scissors" and computerChoice == "paper":
        print ("You have won!")
        win +=1

    elif playerChoice == "rock" and computerChoice == "paper":
        print ("You have lost.")
        lost +=1
        
    elif playerChoice == "paper" and computerChoice == "scissors":
        print ("You have lost.")
        lost +=1
        
    elif playerChoice == "scissors" and computerChoice == "rock":
        print ("You have lost.")
        lost +=1

    print("wins: " +(str)(win)+ " losses: " + (str)(lost) + " ties: " +(str)(tie))
    
    
           
