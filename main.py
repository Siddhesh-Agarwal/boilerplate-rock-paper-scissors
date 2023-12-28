# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player

TESTING_MODE = True

# Uncomment line below to run unit tests automatically
if __name__ == "__main__":
    play(player, quincy, 1000)
    play(player, abbey, 1000)
    play(player, kris, 1000)
    play(player, mrugesh, 1000)

    if TESTING_MODE:
        from unittest import main

        main(module="test_module", exit=False)
