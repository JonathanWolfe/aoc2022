from pathlib import Path
from typing import List, Tuple

rootDir = Path(__file__).parent.resolve()
inputPath = (rootDir / "./part1-input.txt").resolve()

encryption = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

shapePoints = {"rock": 1, "paper": 2, "scissors": 3}

LOSS = 0
DRAW = 3
WIN = 6


def main():
    rounds = processFile()
    # print(rounds)

    wins = 0
    losses = 0
    draws = 0

    our_points = 0

    for round in rounds:
        [theirs, ours] = decrypt(round)

        if theirs == ours:
            draws += 1
            points_gained = DRAW + shapePoints[ours]
            print(f"result: draw ({theirs} vs {ours})")
            print("points gained:", points_gained)
            our_points += points_gained
        elif (
            (theirs == "rock" and ours == "paper")
            or (theirs == "paper" and ours == "scissors")
            or (theirs == "scissors" and ours == "rock")
        ):
            wins += 1
            points_gained = WIN + shapePoints[ours]
            print(f"result: win ({theirs} vs {ours})")
            print(f"points gained: {points_gained} ({LOSS} + {shapePoints[ours]})")
            our_points += points_gained
        elif (
            (theirs == "rock" and ours == "scissors")
            or (theirs == "paper" and ours == "rock")
            or (theirs == "scissors" and ours == "paper")
        ):
            losses += 1
            points_gained = LOSS + shapePoints[ours]
            print(f"result: loss ({theirs} vs {ours})")
            print(f"points gained: {points_gained} ({LOSS} + {shapePoints[ours]})")
            our_points += points_gained

    print("wins", wins)
    print("losses", losses)
    print("draws", draws)
    print("total rounds", wins + losses + draws)
    print("")
    print("our points", our_points)


def processFile():
    rounds: List[Tuple[str, str]] = []

    with open(inputPath) as file:
        while line := file.readline().rstrip():
            rounds.append((line[0], line[2]))

    return rounds


def decrypt(input: Tuple[str, str]):
    return (encryption[input[0]], encryption[input[1]])


if __name__ == "__main__":
    main()
