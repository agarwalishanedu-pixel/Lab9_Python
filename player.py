"""
Program Name: Lab 9 (player.py)
My name: Ishan Agarwal
Purpose: This program is meant to deepen my understanding of classes in python. Also this is used to make a game that flips coins.
Starter Code: None
Date: 03/15/2026 
"""

from coin import Coin

class Player:
    # This class is representing a player

    def __init__(self, name):
        """
        This initializes the player
        """

        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """
        This tosses the coin
        """

        self.__coin.toss()

    def get_coin_side(self):
        """
        This returns the side the coin flip is
        """

        return self.__coin.get_sideup()
    
    def win_coin(self):
        """
        Add coin to waller
        """

        self.__wallet += 1

    def lose_coin(self):
        """
        remove coin to waller
        """

        self.__wallet -= 1

    def get_wallet(self):
        """
        return current val of wallet
        """

        return self.__wallet
    
    def get_name(self):
        """
        return player name
        """

        return self.__name
        