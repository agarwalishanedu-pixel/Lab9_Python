"""
Program Name: Lab 9 (coin.py)
My name: Ishan Agarwal
Purpose: This program is meant to deepen my understanding of classes in python. Also this is used to make a game that flips coins.
Starter Code: None
Date: 03/15/2026 
"""

import random

#Create the class
class Coin:
    # This class is representing a single tossable coin

    def __init__(self):
        """
        This initializes the coin to heads
        """

        self.__sideup = "Heads"

    def toss(self):
        """
        This function does the tossing and generates the value
        """

        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """
        This returns the value of the flip
        """

        return self.__sideup