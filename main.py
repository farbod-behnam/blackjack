from __future__ import print_function
import sys
import time
import random


# =======================================================================================================

# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
from play import Play


def main():


    while True:


        new_game = Play()

        while new_game.get_chip_pool() > 0:
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
