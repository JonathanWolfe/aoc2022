from pathlib import Path
from typing import List

rootDir = Path(__file__).parent.resolve()


def main():
    path = (rootDir / "./part1-input.txt").resolve()

    inventories: List[List[float]] = []

    with open(path) as file:
        currentElf: List[float] = []

        for rawLine in file:
            line = rawLine.rstrip()

            if line:
                currentElf.append(float(line))
            else:
                inventories.append(currentElf)
                currentElf = []

    totals = [sum(items) for items in inventories]
    totals.sort(reverse=True)

    print(totals)
    print("")
    print("Highest", totals[0])
    print("2nd Highest", totals[1])
    print("3rd Highest", totals[2])
    print("")
    print("Combined total", sum(totals[0:3]))


if __name__ == "__main__":
    main()
