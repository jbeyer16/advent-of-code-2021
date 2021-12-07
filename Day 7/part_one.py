from pathlib import Path
import math


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    positions = [int(x) for x in read_file("input")[0].split(",")]

    max_position = max(positions)
    min_position = min(positions)

    fuel = math.inf

    for i in range(min_position, max_position + 1):
        fuel = min(fuel, sum([abs(position - i) for position in positions]))

    answer = fuel

    return answer


if __name__ == "__main__":
    print("\n~~ Day 7 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
