from card import Rank_List


class Hand(object):
    """It repesents the hand of dealer or player"""

# ---------------------------------------------
    def __init__(self):
        self.cards_list = []
        self.score = 0
        # to determine wheter our ace has 1 or 11 points
        self.ace = False
# ---------------------------------------------
    def __str__(self):
        cards_in_hand = ""
        for card in self.cards_list:
            card_name = card.__str__()
            cards_in_hand += " " + card_name

        return "contains: %s" %cards_in_hand
# ---------------------------------------------
    def add_card(self, card):
        """Used to add a card to the hand"""
        self.cards_list.append(card)

        if card.get_rank() == 'A':
            self.ace = True

        self.score += Rank_List[ card.get_rank() ]
# ---------------------------------------------
    def get_score(self):
        """Tells us the score of the hand"""
        if self.ace == True and self.score < 12:
            return self.score + 10
        else:
            return self.score
# ---------------------------------------------
    def reset_hand(self):
        self.cards_list = []
        self.score = 0
# ---------------------------------------------
    def get_cards(self):
        return self.cards_list
# ---------------------------------------------
    def draw(self, hidden, playing):
        # playing boolean is used to know if hand is in play
        if hidden == True and playing == True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0

        for index in range(starting_card, len(self.cards_list)):
            print (self.cards_list[index])

