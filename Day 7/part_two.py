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
        fuel = min(
            fuel, sum([calc_fuel_cost(abs(position - i)) for position in positions])
        )

    answer = fuel

    return answer


def calc_fuel_cost(distance):
    cost = sum([i + 1 for i in range(distance)])

    return cost


if __name__ == "__main__":
    print("\n~~ Day 7 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
