# Write a Python program to create a two-player Dice Game.

# The program should:
# 1. Allow two players to play the game.
# 2. Each player gets a chance to roll the dice or hold their score.
# 3. If the player rolls the dice, generate a random number between 1 and 6.
# 4. If the dice shows 1, the player's score becomes 0, and the turn moves to the other player.
# 5. If the dice shows any number from 2 to 6, add that number to the player's score.
# 6. If the player chooses to hold, save their current score and move to the next player.
# 7. The first player to reach 20 or more points wins the game.


#Import random module
import random

print("===========Dice Game=========")
#Initialize both players' scores
player_1 = 0
player_2 = 0

#Set Player 1 as the first player
current_player = 1

#Continue the game until a player reaches 20 points
while player_1< 20  and  player_2< 20 :
    print()
    print("Player No :",current_player)
    option=input("\nEnter option (r/h) :")
    if option.lower()=="r":
        #Generate a random dice number between 1 and 6
        dice=random.randint(1,6)
        print("Dice :",dice)

        #Switch to the other player
        if dice== 1 :
            print("You Rolled 1 ")

            if current_player== 1:
                player_1= 0
                current_player=2
            else:
                player_2= 0
                current_player=1
        else:
            #Add dice number to the current player's score
            if current_player== 1:
                player_1 = player_1 + dice
                print("Player 1 Score :",player_1)

                # Stop the game if Player 1 reaches 20 points
                if player_1 >= 20 :
                    break
            else :
                player_2 = player_2 + dice
                print("Player 2 Score :",player_2)

                # Stop the game if Player 2 reaches 20 points
                if player_2 >= 20 :
                    break

    #If player chooses to hold, switch the turn
    elif option.lower()=="h":
        if current_player== 1 :  
            print('Player 1 Score  hold at:',player_1)        
            current_player=2

        else :
            current_player= 1
            print('Player 2 Score hold at:',player_2)

    #Display message for invalid input
    else :
        print("Enter valid option (Roll/Hold) :")

#Display final scores
print("\nPlayer No 1 :",player_1)
print("Player No 2 :",player_2)

#Check and display the winner
if player_1 >= 20:
    print("Player No 1  Wins !!!!")
else:
    print("Player No 2 Wins !!!!")

print("=========Game Over=======")