from card import Rank_Dict

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

#-----------------------------------------------------------------------------------
# add_card
# -----------------------------------------------------------------------------------
    def add_card(self, card):
    	"""
    	add_card: adds a card to the hand
    	IN: card, self.ace, self.cards_list, self.score and Rank_Dict of Card class
    	RETURN: Nothing
    	MODIFIES: self.cards_list, self.score, self.ace
    	CALL: get_rank method of Card class
    	Description: It adds card to the hand and while doing so it checks wheter that
        card is an ace card and if so set the self.ace to True and at the end it adds the
        score of that card to self.score.
    	"""
        self.cards_list.append(card)

        if card.get_rank() == 'A':
            self.ace = True

        self.score += Rank_Dict[ card.get_rank() ]

#-----------------------------------------------------------------------------------
# get_score
# -----------------------------------------------------------------------------------
    def get_score(self):
    	"""
    	get_score: Gives us the score of the hand
    	IN: card, self.ace, self.score
    	RETURN: self.score
    	MODIFIES: self.score if necessary
    	CALL: Nothing
    	Description: It checks to see if self.ace is True and self.score is less than
        12 then Ace card shold be valued as 11 (that's why adds 10 to the hand) otherwise
        the Ace shold be values as 1
    	"""
        if self.ace == True and self.score < 12:
            return self.score + 10
        else:
            return self.score

#-----------------------------------------------------------------------------------
# reset_hand
# -----------------------------------------------------------------------------------
    def reset_hand(self):
    	"""
    	reset_hand: renews the self.cards_list and self.score
    	IN: self.score, self.cards_list
    	RETURN: Nothing
    	MODIFIES: self.score, self.cards_list
    	CALL: Nothing
    	Description: It resets the hands cards_list and score. If this won't happen
        then in the while loop in main function when it comes back, the new score and new
        cards will get sumed up with the old cards in the list and score
    	"""
        self.cards_list = []
        self.score = 0

#-----------------------------------------------------------------------------------
# get_cards
# -----------------------------------------------------------------------------------
    def get_cards(self):
    	"""
    	get_cards: get the list of cards from Hand class of player or dealer
    	IN: Nothing
    	RETURN: self.cards_list
    	MODIFIES: Nothing
    	CALL: Nothing
    	Description:
    	"""

        return self.cards_list

#-----------------------------------------------------------------------------------
# draw
# -----------------------------------------------------------------------------------
    def draw(self, hidden, playing):
    	"""
    	draw: It prints the cards_list of player and dealer hand
    	IN: playing (self.playing of Play class), hidden, self.cards_list
    	RETURN: Nothing
    	MODIFIES: Nothing
    	CALL: Nothing
    	Description: If both booleans are True then index will be at one
        and draw method won't show the first card in dealer_hand. starding_card
        was specifically designed for dealer_hand in Play class in order to hide
        the first card in dealer's hand.
    	"""

        # playing boolean is used to know if the game is still on
        if hidden == True and playing == True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0

        for index in range(starting_card, len(self.cards_list)):
            print (self.cards_list[index])

