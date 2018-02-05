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
    def __init__(self):
        self.cards_list = []
        self.soft_score = 0
        self.hard_score = 0
# ---------------------------------------------
    def add_card(self, card):
        """Used to add a card to the hand"""
        if card.get_rank() == "A":
            Hand.number_of_aces -= 1

        self.cards_list.append(card)
# ---------------------------------------------
    def get_hard_value(self):
        """Tells us the score of the hand (Hard Score)"""
        self.reset_score()
        for card in self.cards_list:
            self.hard_score += Rank_List[ card.get_rank() ]

        return self.hard_score
# ---------------------------------------------
    def get_soft_value(self):
        """Tells us the soft value of the hand"""
        self.soft_score = self.hard_score - 10

        return self.soft_score

    def get_score(self):
        if self.get_hard_value() > 21 and Hand.number_of_aces > 0:
            return self.get_soft_value()

        return self.get_hard_value()
# ---------------------------------------------
    def get_cards(self):
        return self.cards_list

    def reset_score(self):
        setattr(self, 'soft_score', 0)
        setattr(self, 'hard_score', 0)
# ---------------------------------------------
    def __str__(self):
        return "Cards List: %s, Hard Score: %s, Soft Score: %s" %(self.get_cards(), self.get_hard_value(), self.get_soft_value())
# =======================================================================================================
# import random

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
# import sys
# import time
# from __future__ import print_function


class Play(object):
    """This class is responsible for handling the flow of the game"""

    # Private attributes
    __player_round = True
    __blackjack = False
    __lost = False
# ---------------------------------------------

    def __init__(self):
        self.deck = Deck()
        self.player = Hand()
        self.dealer = Hand()
        self.win_count = 0
        self.lose_count = 0
# ---------------------------------------------

    def player_input(self):
        while True:
            input = raw_input("Press \"Enter(return) or e\" to hit you otherwise enter \"stop or s\": ")
            input = input[:1].lower()
            if input == "" or input == "e":
                return True
            elif input == "s":
                return False
            else:
                print ("Please press enter or type \"stop or s\"")
                continue

# ---------------------------------------------


    def display_deck(self):
        if Play.__player_round:
            dealer_cards_list = self.dealer.get_cards()
            print ("Dealer: [",dealer_cards_list[0],",** of ******] Score: ",Rank_List[ dealer_cards_list[0].get_rank() ])
            print ("Player: ",self.player.get_cards(), "Score: ", self.player.get_score())
            print ("Wins: ", self.win_count, "Loses: ", self.lose_count)
        else:
            print("Cards: ", len(self.deck.cards_list))
            print ("Dealer: ")
            print ("Dealer: ",self.dealer.get_cards(), "Score: ", self.dealer.get_score())
            print ("Player: ")
            print ("Player: ",self.player.get_cards(), "Score: ", self.player.get_score())
            print ("Wins: ", self.win_count, "Loses: ", self.lose_count)



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


    def start(self):
        """Used when the player wants to Hit. It adds a card to the player's deck. It also checks if player/dealer busted
        while invoking hit. Also if player reaches 21, it displays message of blackjack."""


        # Major While Loop begins in main-------------------------------------------------------------------------------------------------

        print ("Welcome to blackjack")

        self.deck.shufle()

        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())

        self.display_deck()

        if self.player.get_score() == 21:
            print ("Blackjack!")
            self.win_count += 1
            self.clear_terminal(0.4)
            self.restart()

        # while loop for player begins ----------------------------------------------------------
        while True:
            self.display_deck()


            if self.player_input():
                self.player.add_card(self.deck.deal_card())
                self.display_deck()


            if self.player.get_score() > 21:
                print ("You lost!")
                self.lose_count += 1
                Play.__lost = True
                break

            if self.player.get_score() == 21:
                print ("Yout won, Blackjack")
                Play.__blackjack = True
                self.win_count += 1
                break

            else:
                break

        # while loop for player ends ----------------------------------------------------------

        self.display_deck()


        # check to see if you hit blackjack or you have lost
        if Play.__blackjack or Play.__lost:
            self.restart()

        # Now display_deck() will show the hand of dealer completely
        Play.__player_round = False


        self.display_deck()


        # while loop for dealer begins --------------------------------------------------------
        while True:
            if self.dealer.get_score() <= 17:
                self.dealer.add_card(self.deck.deal_card())
                continue
            else:
                break
        # while loop for dealer ends --------------------------------------------------------


        # Check for the win ----------------------------------
        if self.player.get_score() >= self.dealer.get_score():
            print ("Player won")
            self.win_count += 1

        else:
            print ("Dealer won")
            self.lose_count += 1


        self.restart()
        # Major While Loop ends-------------------------------------------------------------------------------------------------
#
# =======================================================================================================

def main():


    while True:
        new_game = Play()
        if new_game.start():
            continue
# =======================================================================================================

if __name__ == "__main__":
    main()

        # # Major While Loop begins-------------------------------------------------------------------------------------------------
        # while True:

        #     print ("Welcome to blackjack")

        #     print (self.deck.cards_list)
        #     self.deck.shufle()

        #     self.player.add_card(self.deck.deal_card())
        #     self.player.add_card(self.deck.deal_card())


        #     self.dealer.add_card(self.deck.deal_card())
        #     self.dealer.add_card(self.deck.deal_card())

        #     self.display_deck()

        #     if self.player.get_score() == 21:
        #         print ("Blackjack!")
        #         self.win_count += 1
        #         if self.restart():
        #             continue
        #         else:
        #             return False

        #     # while loop for player begins ----------------------------------------------------------
        #     while True:
        #         self.display_deck()


        #         if self.player_input():
        #             self.player.add_card(self.deck.deal_card())
        #             self.display_deck()


        #             if self.player.get_score() > 21:
        #                 print ("You lost!")
        #                 self.lose_count += 1
        #                 Play.__lost = True
        #                 break

        #             elif self.player.get_score() == 21:
        #                 print ("Yout won, Blackjack")
        #                 Play.__blackjack = True
        #                 self.win_count += 1
        #                 break

        #             else:
        #                 continue

        #         else:
        #             break
        #     # while loop for player ends ----------------------------------------------------------

        #     self.display_deck()


        #     # check to see if you hit blackjack or you have lost
        #     if Play.__blackjack or Play.__lost:
        #         if self.restart():
        #             continue

        #     # Now display_deck() will show the hand of dealer completely
        #     Play.__player_round = False


        #     self.display_deck()


        #     # while loop for dealer begins --------------------------------------------------------
        #     while True:
        #         if self.dealer.get_score() <= 17:
        #             self.dealer.add_card(self.deck.deal_card())
        #             continue
        #         else:
        #             break
        #     # while loop for dealer ends --------------------------------------------------------


        #     # Check for the win ----------------------------------
        #     if self.player.get_score() >= self.dealer.get_score():
        #         print ("Player won")
        #         self.win_count += 1

        #     else:
        #         print ("Dealer won")
        #         self.lose_count += 1


        #     if self.restart():
        #         continue
        # Major While Loop ends-------------------------------------------------------------------------------------------------
