# DO NOT MODIFY THIS FILE
import random
from typing import Callable, Dict, List
from RPS_types import move, moveStrict


def play(
    player1: Callable[[move], moveStrict],
    player2: Callable[[move], moveStrict],
    num_games: int,
    verbose: bool = False,
):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if any(
            [
                p1_play == "P" and p2_play == "R",
                p1_play == "R" and p2_play == "S",
                p1_play == "S" and p2_play == "P",
            ]
        ):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif any(
            [
                p2_play == "P" and p1_play == "R",
                p2_play == "R" and p1_play == "S",
                p2_play == "S" and p1_play == "P",
            ]
        ):
            results["p2"] += 1
            winner = "Player 2 wins."
        else:
            results["tie"] += 1
            winner = "Tie."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results["p2"] + results["p1"]

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results["p1"] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate:0.2f}%")

    return win_rate


def quincy(prev_play: move, counter: List[int] = [0]) -> moveStrict:
    counter[0] += 1
    choices: List[moveStrict] = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_opponent_play: move, opponent_history: List[move] = []) -> moveStrict:
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == "":
        most_frequent = "S"

    ideal_response: Dict[moveStrict, moveStrict] = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[most_frequent]


def kris(prev_opponent_play: move) -> moveStrict:
    if prev_opponent_play == "":
        prev_opponent_play = "R"
    ideal_response: Dict[moveStrict, moveStrict] = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prev_opponent_play]


def abbey(
    prev_opponent_play: move,
    opponent_history: List[move] = [],
    play_order: List[Dict[str, int]] = [
        {
            "RR": 0,
            "RP": 0,
            "RS": 0,
            "PR": 0,
            "PP": 0,
            "PS": 0,
            "SR": 0,
            "SP": 0,
            "SS": 0,
        }
    ],
) -> moveStrict:
    if not prev_opponent_play:
        prev_opponent_play = "R"
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {k: play_order[0][k] for k in potential_plays if k in play_order[0]}

    prediction = max(sub_order, key=lambda x: sub_order[x])[-1:]

    ideal_response: Dict[moveStrict, moveStrict] = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prediction]


def human(prev_opponent_play: move) -> moveStrict:
    play = ""
    while play not in ["R", "P", "S"]:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play


def random_player(prev_opponent_play: move) -> moveStrict:
    return random.choice(["R", "P", "S"])
