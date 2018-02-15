from __future__ import print_function
import sys
import time
import random


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
    def __str__(self):
        return "[%s of %s] " %(self.rank, self.suit)
# ---------------------------------------------
    def __repr__(self):
        return str(self)
# ---------------------------------------------
    def get_rank(self):
        """Tells us the rank of the card: 2, 3, A, K etc."""
        return self.rank
# ---------------------------------------------
    def get_suit(self):
        """Tells us the suit of the card: Clubs, Spade, Diamond and Hearts"""
        return self.suit


# =======================================================================================================
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
# =======================================================================================================
# import random

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
        random.shuffle(self.cards_list)
# ---------------------------------------------
    def deal_card(self):
        """pops card from deck and returns the cards"""
        return self.cards_list.pop()
# =======================================================================================================
# import sys
# import time
# from __future__ import print_function


class Play(object):
    """This class is responsible for handling the flow of the game"""

    # Private attributes
# ---------------------------------------------

    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.bet = 0
        # boolean to know if hand is in play
        self.playing = False
        self.chip_pool = 100
        self.game_result = ""
# ---------------------------------------------
    def get_bet(self):
        return self.bet

    def set_bet(self, bet):
        self.bet = bet
# -------------------------
    def get_playing(self):
        return self.playing

    def set_playing(self, playing):
        self.playing = playing
# -------------------------
    def get_chip_pool(self):
        return self.chip_pool

    def set_chip_pool(self, chip_pool):
        self.chip_pool = chip_pool
# -------------------------
    def get_game_result(self):
        return self.game_result

    def set_game_result(self, game_result):
        self.game_result = game_result
# -------------------------

    def player_input(self):
        while True:
            input = raw_input("Press \"Enter(return) or e\" to hit otherwise enter \"stop or s\" or \"q\" to quit the game: ")
            input = input[:1].lower()
            if input == "" or input == "e":
                return True
            elif input == "s":
                return False
            elif input == "q":
                sys.exit(0)
            else:
                print ("Please press enter or type \"stop or s\"")
                continue

# ---------------------------------------------
    def make_bet(self):

        while True:
            bet_temp = raw_input("What amount of chips would you like to bet? (Enter just integer please): ")
            try:
                bet_temp = int(bet_temp)
            except:
                print ("Please enter \"integer\" only\n")
                continue

            if bet_temp >= 1 and bet_temp <= self.chip_pool:
                self.bet = bet_temp
                break
            else:
                print ("Invalid bet, you only have " + str(self.chip_pool) + " remaining\n")
                continue
# ---------------------------------------------
    def deal_cards(self):

        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())

        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        if self.playing == True:
            print ("Fold, Sorry")
            self.chip_pool -= self.bet

        # Set up to know currently playing hand
        self.playing = True
# ---------------------------------------------
    def hit(self):

        while self.player_input():
            if self.player_hand.get_score() <= 21:
                self.player_hand.add_card(self.deck.deal_card())

            time.sleep(0.4)
            print ("\nPlayer hand %s\n" %self.player_hand)

            if self.player_hand.get_score() > 21:
                self.game_result = "You Busted"

                self.chip_pool -= self.bet
                self.playing = False
                break

# ---------------------------------------------
    def stand(self):

        # If the game is still being played
        if self.playing:

            while self.dealer_hand.get_score() < 17 and self.playing:
                self.dealer_hand.add_card(self.deck.deal_card())


            # Dealer Busts
            if self.dealer_hand.get_score() > 21:
                self.game_result = "Dealer busts! You win!"
                self.chip_pool += self.bet
                self.playing = False

            # Player has better hand than dealer
            elif self.dealer_hand.get_score() < self.player_hand.get_score() and self.player_hand.get_score() <= 21:
                self.game_result = "You beat the dealer, you win!"
                self.chip_pool += self.bet
                self.playing = False

            # Push
            elif self.dealer_hand.get_score() == self.player_hand.get_score():
                self.game_result = "Tied up, push!"
                self.playing = False

            # Dealer beats player
            else:
                self.game_result = "Dealer Wins!"
                self.chip_pool -= self.bet
                self.playing = False
# ---------------------------------------------
    def game_status(self):
        """Print game status"""

        time.sleep(0.4)
        # Display Player Hand
        print ("Player Hand is: ")
        self.player_hand.draw(hidden = False, playing = self.playing)

        print ("Player hand total is: " + str(self.player_hand.get_score()) )

        # Display Dealer Hand
        print ("Dealer Hand is: ")
        self.dealer_hand.draw(hidden = True, playing = self.playing)

        # If game round is over
        if self.playing == False:
            print (" --- for a total of " + str(self.dealer_hand.get_score()))
            print ("Chip Total: " + str(self.chip_pool))

        # Otherwise, don't know the second card yet of dealer
        else:
            print ("With another card hidden upside down")


        # Print result of hit or stand
        print ("\n" + self.game_result + "\n")

# ---------------------------------------------
    def reset_hands(self):
        self.dealer_hand.reset_hand()
        self.player_hand.reset_hand()
# ---------------------------------------------
    def restart(self):
        while True:
            answer = raw_input ("\n\nDo you want to play again? (y or n): ")
            answer = answer.strip()
            answer = answer.lower()

            if answer[0] == "y":
                self.clear_terminal (0.4)
                return True
            elif answer[0] == "n":
                print ("Thank you for playing")
                sys.exit (0)
            else:
                print ("\n\nplease answer \"y\" or \"n\"!\n")
                continue
# ---------------------------------------------

    def clear_terminal(self, wait):

        print("\033[H\033[J")
        sys.stdout.flush()
        print("\033[H\033[J")
        sys.stderr.flush()


        # sleep for # seconds
        time.sleep(wait)
# ---------------------------------------------
# =======================================================================================================

def main():


    while True:


        new_game = Play()

        while new_game.get_chip_pool() > 0:
            new_game.set_game_result("")
            new_game.reset_hands()
            new_game.make_bet()
            new_game.deal_cards()
            new_game.game_status()
            new_game.hit()
            new_game.stand()
            new_game.game_status()

        if new_game.restart():
            continue
# =======================================================================================================

if __name__ == "__main__":
    main()
