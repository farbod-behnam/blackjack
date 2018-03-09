from __future__ import print_function
from time import sleep
from deck import Deck
from hand import Hand

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
                exit(0)
            else:
                print ("Please press enter or type \"stop or s\"")
                continue

# ---------------------------------------------
    def make_bet(self):

        while True:
            bet_temp = raw_input("What amount of chips would you like to bet? (Enter just integer please) or \"q\" to quit: ")

            # -------------------------
            # If player wanted to quit the game
            if bet_temp[:1] == "q":
                exit(0)
            #-------------------------
            # If player intered an integer or somehing other than "q"
            elif bet_temp[:1] != "q":
                try:
                    bet_temp = int(bet_temp)
                except:
                    print ("\nPlease enter \"integer\" or \"q\" only!\n")
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

            sleep(0.4)
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

        sleep(0.4)
        # Display Player Hand
        print ("\nPlayer Hand is: ")
        self.player_hand.draw(hidden = False, playing = self.playing)

        print ("Player hand total is: " + str(self.player_hand.get_score()) )

        # Display Dealer Hand
        print ("\nDealer Hand is: ")
        self.dealer_hand.draw(hidden = True, playing = self.playing)

        # If game round is over
        if self.playing == False:
            print ("\n --- for a total of " + str(self.dealer_hand.get_score()))
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
        self.set_game_result("")
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
                exit (0)
            else:
                print ("\n\nplease answer \"y\" or \"n\"!\n")
                continue
# ---------------------------------------------
