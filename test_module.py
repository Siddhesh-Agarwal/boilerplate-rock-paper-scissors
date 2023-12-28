import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player


class UnitTests(unittest.TestCase):
    """Tests the RPS game."""

    verbose = False  # If you want to see the results printed, set this to True
    print()

    def test_player_vs_quincy(self):
        """Tests that player defeats quincy at least 60% of the time."""
        print("Testing game against quincy...")
        actual = play(player, quincy, 1000, self.verbose) >= 60
        self.assertTrue(
            actual, "Expected player to defeat quincy at least 60% of the time."
        )

    def test_player_vs_abbey(self):
        """Tests that player defeats abbey at least 60% of the time."""
        print("Testing game against abbey...")
        actual = play(player, abbey, 1000, self.verbose) >= 60
        self.assertTrue(
            actual, "Expected player to defeat abbey at least 60% of the time."
        )

    def test_player_vs_kris(self):
        """Tests that player defeats krish at least 60% of the time."""
        print("Testing game against kris...")
        actual = play(player, kris, 1000, self.verbose) >= 60
        self.assertTrue(
            actual, "Expected player to defeat kris at least 60% of the time."
        )

    def test_player_vs_mrugesh(self):
        """Tests that player defeats mrugesh at least 60% of the time."""
        print("Testing game against mrugesh...")
        actual = play(player, mrugesh, 1000, self.verbose) >= 60
        self.assertTrue(
            actual, "Expected player to defeat mrugesh at least 60% of the time."
        )


if __name__ == "__main__":
    unittest.main()
