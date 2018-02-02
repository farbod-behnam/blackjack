
Rank_List = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
Suit_List = ["Clubs", "Spade", "Diamond", "Heart"]
# =======================================================================================================
class Card(object):
    """It repesents individual cards."""

# ---------------------------------------------
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
# ---------------------------------------------
    def get_rank(self):
        """Tells us the rank of the card: 2, 3, A, K etc."""
        return getattr(self, "rank")
# ---------------------------------------------
    def get_suit(self):
        """Tells us the suit of the card: Clubs, Spade, Diamond and Hearts"""
        return getattr(self, "suit")
# ---------------------------------------------
    def __str__(self):
        return "%s of %s " %(self.get_rank(), self.get_suit())

    def __repr__(self):
        return str(self)
# =======================================================================================================
class Hand(object):
    """It repesents the hand of dealer or player"""

    number_of_aces = 4
# ---------------------------------------------
    def __init__(self, soft_score = 0, hard_score = 0):
        self.cards_list = []
        self.soft_score = soft_score
        self.hard_score = hard_score
# ---------------------------------------------
    def add_card(self, card):
        """Used to add a card to the hand"""
        self.cards_list.append(card)
        if card.get_rank() == "A":
            Hand.number_of_aces -= 1
# ---------------------------------------------
    def get_hard_value(self):
        """Tells us the score of the hand (Hard Score)"""
        for card in self.cards_list:
            self.hard_score += Rank_List[ card.get_rank() ]

        self.soft_score = self.hard_score
        return self.hard_score
# ---------------------------------------------
    def get_soft_value(self):
        """Tells us the soft value of the hand"""
        if self.hard_score > 21 and Hand.number_of_aces > 0:
            self.soft_score = self.hard_score - 10

        return self.soft_score
# ---------------------------------------------
    def get_cards(self):
        return self.cards_list
# ---------------------------------------------
    def __str__(self):
        return "Cards List: %s, Hard Score: %s, Soft Score: %s" %(self.get_cards(), self.get_hard_value(), self.get_soft_value())
# =======================================================================================================
import random

class Deck(object):
    """It represents the pack of 52 cards. It is used to deal cards to the dealer and player"""

    # private attribute
    cards_list = []

# ---------------------------------------------
    def __init__(self):
        for suit in Suit_List:
            for rank in Rank_List.keys():
                Deck.cards_list.append(Card(suit, rank))

# ---------------------------------------------
    def shufle(self):
        """shuffles the cards in the deck using random method of python"""
        random.shuffle(Deck.cards_list)
# ---------------------------------------------
    def deal_card(self):
        """pops card from deck and returns the cards"""
        return Deck.cards_list.pop()

# =======================================================================================================

class Play(object):
    """This class is responsible for handling the flow of the game"""

    def __init__(self):
        self.mydeck = Deck()
        self.player = Hand()
        self.dealer = Hand()

    def player_input(self):
        pass

    def display_deck(self):
        pass

    def win_check(self):
        pass

    def start(self):
        pass

# =======================================================================================================

def main():
    newDeck = Deck()



    newDeck.shufle()


    # print newDeck.cards_list


    # create new hands
    player = Hand()
    dealer = Hand()

    # before poping the last card into a hand count all the cards
    count = 0
    for i in Deck.cards_list:
        count += 1


    # -----------------------------------------
    player.add_card(newDeck.deal_card())

    count_player = 0
    for i in Deck.cards_list:
        count_player += 1


    #------------------------------------------
    dealer.add_card(newDeck.deal_card())


    count_dealer = 0
    for i in Deck.cards_list:
        count_dealer += 1


    # -----------------------------------------
    print "Total Cards: ", count
    print "Player: ", player, "Count: ", count_player
    print "Dealer: ", dealer, "Count: ", count_dealer

# =======================================================================================================

if __name__ == "__main__":
    main()
