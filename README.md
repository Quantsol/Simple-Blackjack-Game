# Simple-Blackjack-Game
This is my first Python project  and my first attempt at building a program using OOP

Table of Contents:

    1. Installation
    2. How to Play?
    3. OOP Implementation

1. Installation Instructions:

    1. Requires python version 3.11.1 or later
        
        Python can be downloaded here: https://www.python.org/downloads/
    2. Download/Fork blackpack.py and run in terminal/IDE using the following command:
        
        python blackjack.py
    3. Play the game which uses a command line interface to play

2. How to play blackjack?

    Blackjack hands are scored by their point total. 
    The hand with the highest total wins as long as 21 isn't exceeded; a hand greater than 21 is said to bust. 
    Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10.
    
    Note: 
        In this implementation, one card from the dealer will always be hidden to the player, and only allows for 1 player vs the Dealer.

3. OOP Implementation:

    This version is designed with four clases: Card, Deck, Hand, and Game
        * Game contains all the UI and objects storing the information of the player and dealer
        * Hand contains value of player and dealer's hand with special properties when dealing with the dealer's hand
        * Deck contains a randomized deck of cards that is shuffled every time a card is taken
        * Card contains the names of each card in the Deck and their value
    Helper functions were added to easily check win conditions after each turn
