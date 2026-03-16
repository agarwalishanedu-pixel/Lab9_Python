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
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")

    print("")
    play = input("Do you want to toss the coins? (y/n): ")
    print("")

    while play.lower() == "y":
        
        #Both player toss coin
        print("Tossing...")
        player1.toss_coin()
        player2.toss_coin()


main()