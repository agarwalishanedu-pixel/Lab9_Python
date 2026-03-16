"""
Program Name: Lab 9 (Main File)
My name: Ishan Agarwal
Purpose: This program is meant to deepen my understanding of classes in python. Also this is used to make a game that flips coins.
Starter Code: None
Date: 03/15/2026 
"""

#import player class
from player import Player

#Make the main function
def main():

    print("--- Coin Match Game ---")

    # Create the two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    print("")
    play = input("Do you want to toss the coins? (y/n): ")
    print("")

    while play.lower() == "y":
        
        #Both player toss coin
        print("Tossing...")
        player1.toss_coin()
        player2.toss_coin()

        #it sets a variable to store value
        sidep1 = player1.get_coin_side()
        sidep2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {sidep1}")
        print(f"{player2.get_name()} tossed {sidep2}")

        #checks for who wins, if both same, then player 1, otherwise player 2 wins
        if sidep1 == sidep2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.")
        else:
            player1.lose_coin()
            player2.win_coin()
            print("...No Match! Player 2 wins a coin.")

        print("")
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
        print("")

        play = input("Do you want to toss the coins? (y/n): ")
        print("")
        #If either player has no balance left then it changes the condition value to end loop.
        if(player1.get_wallet() == 0 or player2.get_wallet() == 0):
            play = "n"

    print("--- Final Score ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    #Check for who wins or has more coins
    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins!")
    else:
        print("It's a draw!")


main()