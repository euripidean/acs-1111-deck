"""
Deck of Cards
"""
import random

class Card:
    """
    Card class
    """
    def __init__(self, suit, value, colour):
        self.suit = suit
        self.value = value
        self.colour = colour

    def show(self):
        """
        Print the card value and suit
        """
        print(f'{self.value} of {self.suit}.')

class Deck:
    """
    Deck class
    """
    def __init__(self, cards):
        self.cards = cards

    def create_deck(self):
        """
        Builds out deck.
        """
        values = [2,3,4,5,6,7,8,9,10, 'Jack','Queen','King','Ace']
        suits = ['Spades','Clubs','Hearts','Diamonds']
        for value in values:
            for suit in suits:
                if suit == 'Spades' or suit == 'Clubs':
                    temp = Card(suit,value,'black')
                else:
                    temp = Card(suit,value,'red')
                self.cards.append(temp)
        print(len(self.cards))


    def shuffle(self):
        """
        Shuffle deck
        """
        random.shuffle(self.cards)


deck = Deck(cards =[])
deck.create_deck()
deck.shuffle()
