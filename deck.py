from random import shuffle
from card import Card, Suit_List, Rank_List


class Deck(object):
    """It represents the pack of 52 cards. It is used to deal cards to the dealer and player"""


# ---------------------------------------------
    def __init__(self):
        self.cards_list = []
        for suit in Suit_List:
            for rank in Rank_List.keys():
                self.cards_list.append(Card(suit, rank))

# ---------------------------------------------
    def __str__(self):
        deck_set = ""

        for card in self.cards_list:
            deck_set += " " + card.__str__()

        return "The deck has: %s" %deck_set

# ---------------------------------------------
    def shufle(self):
        """shuffles the cards in the deck using random method of python"""
        shuffle(self.cards_list)
# ---------------------------------------------
    def deal_card(self):
        """pops card from deck and returns the cards"""
        return self.cards_list.pop()

