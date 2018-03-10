from __future__ import print_function
from time import sleep
from deck import Deck
from hand import Hand

class Play(object):
    """This class is responsible for handling the flow of the game"""


# ---------------------------------------------
	# Private attributes
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.bet = 0
        # boolean to know if hand is in play
        self.playing = False
        # total amount of chip
        self.chip_pool = 100
        self.game_result = ""

# get and set methods for class attributes
# -------------------------
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

#-----------------------------------------------------------------------------------
# player_input
# -----------------------------------------------------------------------------------
    def player_input(self):
    	"""
    	player_input: Gets the player input
    	IN: Nothing
    	RETURN: True of False
    	MODIFIES: Nothing
    	CALL: Nothing
    	Description: If the player press "Enter" keyword or "e" the program
    	will give the player another card but if the player entered "s" or
    	"stop" the program will stop giving the player card or if the player
    	entered "q" the program will quit.
    	"""

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
#-----------------------------------------------------------------------------------
# make_bet
# -----------------------------------------------------------------------------------
    def make_bet(self):
    	"""
        make_bet: Gets the amount of chip that player want bet
        IN: self.bet , self.chip_pool
        RETURN: Nothing
        MODIFIES: self.bet attribute
        CALL: Nothing
        Description: Asks the player amount of chip that want to bet in a while loop
        until the player gives the right answer. player can exit the game by pressing
        "q" or just entering the amount of chip that wants to bet and method checks
        if there is the right amount of chip that could be bet against the dealer or
        not.
        """

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

                # check to see if there is enough chip
                if bet_temp >= 1 and bet_temp <= self.chip_pool:
                    self.bet = bet_temp
                    break
                else:
                    print ("Invalid bet, you only have " + str(self.chip_pool) + " remaining\n")
                    continue
#-----------------------------------------------------------------------------------
# deal_cards
# -----------------------------------------------------------------------------------
    def deal_cards(self):
    	"""
    	deal_cards: Deals card to player and dealer
    	IN: self.player_hand, self.dealer_hand, self.playing, self.chip_pool, self.bet
    	RETURN: Nothing
    	MODIFIES: self.card_list in self.player_hand and self.dealer_hand
    	CALL: add_card method of Hand class and deal_card of Deck class
    	Description: It deals card to player and dealer hand and checks to see if the
        game is still on (self.playing) then the player has lost that turn.
    	"""


        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())

        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        if self.playing == True:
            print ("Fold, Sorry")
            self.chip_pool -= self.bet

        # when you deal cards, it definitely means that the game is on
        self.playing = True
#-----------------------------------------------------------------------------------
# hit
# -----------------------------------------------------------------------------------
    def hit(self):
    	"""
    	hit: if the player wants method gives additional cards to the player
    	IN: self.game_result, self.chip_pool, self.bet, self.playing
    	RETURN: Nothing
    	MODIFIES: self.card_list in self.player_hand and self.dealer_hand, self.playing, self.chip_pool, self.playing
    	CALL: add_card and get_score method of Hand class and deal_card of Deck class
    	Description: It deals card to player and dealer hand and checks to see if the
        game is still on (self.playing) then the player has lost that turn.
    	"""


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

#-----------------------------------------------------------------------------------
# stand
# -----------------------------------------------------------------------------------
    def stand(self):
    	"""
    	stand: It gives dealer card
    	IN: self.game_result, self.chip_pool, self.bet, self.playing
    	RETURN: Nothing
    	MODIFIES: self.chip_pool, self.playing
    	CALL: add_card and get_score method of Hand class and deal_card of Deck class
    	Description: If the game is still on the dealer will get cards and then it checks
        dealer and player hand to set the result.
    	"""


        # If the game is still being played
        if self.playing:

            while self.dealer_hand.get_score() < 17:
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

#-----------------------------------------------------------------------------------
# game_status
# -----------------------------------------------------------------------------------
    def game_status(self):
    	"""
    	game_status: Ptints the game status.
    	IN: self.game_result, self.chip_pool, self.playing
    	RETURN: Nothing
    	MODIFIES: self.chip_pool, self.playing
    	CALL: add_card , get_score and draw method of Hand class
    	Description: It prints the cards list of player and dealer hand
        and shows the result of the game.
    	"""


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

        # Otherwise, don't know the second card of dealer yet
        else:
            print ("With another card hidden upside down")


        # Print result of hit or stand
        print ("\n" + self.game_result + "\n")


#-----------------------------------------------------------------------------------
# reset_hands
# -----------------------------------------------------------------------------------
    def reset_hands(self):
    	"""
    	reset_hands: resets the hands of player and dealer to none
    	IN: Nothing
    	RETURN: Nothing
    	MODIFIES: self.cards_list of dealer and player from Hand class and game_result of Play class
    	CALL: reset_hand method of Hand class and set_game_result of Play class
    	Description: It renews the list in self.dealer_hand and self.player_hand and set the self.game_result
        to nothing
    	"""

        self.dealer_hand.reset_hand()
        self.player_hand.reset_hand()
        self.set_game_result("")


#-----------------------------------------------------------------------------------
# restart
# -----------------------------------------------------------------------------------
    def restart(self):
    	"""
    	restart: It asks the player if he or she wants to play again
    	IN: Nothing
    	RETURN: True of False
    	MODIFIES: Nothing
    	CALL: clear_terminal method of Play class , exit function
    	Description: It asks the player in a loop whether he or she wants to play again.
    	"""

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

#-----------------------------------------------------------------------------------
# clear_terminal
# -----------------------------------------------------------------------------------
    def clear_terminal (wait):
        """
        preparation: It clears the terminal
        IN; Nothing
        RETURN: Nothing
        MODIFIES: board_list
        CALL: flush method from sys.stderr
        Description: It clears the terminal and it waits a little bit.
        """

        print("\033[H\033[J")
        print("\033[H\033[J")

        # sleep for # seconds
        sleep(wait)
