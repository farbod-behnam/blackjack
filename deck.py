from random import shuffle
from card import Card, Suit_List, Rank_Dict


class Deck(object):
    """
    Deck: It represents the pack of 52 cards. It is used to deal cards to the dealer and player
    IN: Rank_Dict, Suit_List
    MODIFIES: Nothing
    Description: It uses the name of each suit in Suit_List and and the keys of Rank_Dict
    dictionary to create the 52 individual cards in the deck using Card constructor in
    self.cards_list
    """

    def __init__(self):
        self.cards_list = []
        for suit in Suit_List:
            for rank in Rank_Dict.keys():
                self.cards_list.append(Card(suit, rank))

# -----------------------------------------------------------------------------------
    def __str__(self):
        deck_set = ""

        for card in self.cards_list:
            deck_set += " " + card.__str__()

        return "The deck has: %s" %deck_set

#-----------------------------------------------------------------------------------
# shuffle
# -----------------------------------------------------------------------------------
    def shufle(self):
        """
    	shuffle: shuffles the cards in the deck using random method of python
    	IN: card, self.ace, self.cards_list, self.score and Rank_Dict of Card class
    	RETURN: Nothing
    	MODIFIES: self.cards_list
    	CALL: shuffle method from random library
    	"""
        shuffle(self.cards_list)
#-----------------------------------------------------------------------------------
# deal_card
# -----------------------------------------------------------------------------------
    def deal_card(self):
        """
    	deal_cards: it gives one card to the dealer or player
    	IN: Nothing
    	RETURN: A card from Card class
    	MODIFIES: self.cards_list
    	CALL: Nothing
    	Description: It pops the last card from self.card_list to the self.cards_list
        attributes of player or dealer from Hand class
    	"""
        return self.cards_list.pop()

