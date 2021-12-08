from pathlib import Path
import math


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    entries = read_file("input")

    output_values = [entry.split("|")[-1].strip() for entry in entries]

    count = 0
    for output in output_values:
        digits = output.split(" ")

        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                count += 1

    answer = count

    return answer


if __name__ == "__main__":
    print("\n~~ Day 8 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
