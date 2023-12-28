import random
from typing import Dict, List
from RPS_types import move, moveStrict


def player(
    prev_play: move,
    opponent_history: List[moveStrict] = [],
    play_order: Dict[str, int] = {},
) -> moveStrict:
    """The code that the player uses to determine their next move"""
    prev_play_: moveStrict = prev_play if prev_play else "R"
    prediction: moveStrict = "S"
    opponent_history.append(prev_play_)

    if len(opponent_history) >= 5:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1
        potential_plays = [
            "".join([*opponent_history[-4:], v]) for v in ["R", "P", "S"]
        ]
        sub_order = {k: play_order[k] for k in potential_plays if k in play_order}

        if sub_order:
            prediction = max(sub_order, key=lambda x: sub_order[x])[-1]

    viable_options: Dict[moveStrict, moveStrict] = {"P": "S", "R": "P", "S": "R"}

    guess: moveStrict = viable_options[prediction]

    random_or_not = random.randint(0, 5000)
    if random_or_not == 2:
        guess = random.choice(["P", "R", "S"])

    return guess
