import csv
from pathlib import Path

import pandas as pd


def use_pure_python():
    input_file = Path(__file__).parent / "input"

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    measurements = [int(line.strip()) for line in lines]

    increased_from_previous_count = 0
    for current, previous in zip(measurements[1:], measurements):
        if current > previous:
            increased_from_previous_count += 1

    print(f"Answer is: {increased_from_previous_count}")


def use_pandas():
    input_file = Path(__file__).parent / "input"

    df = pd.read_csv(input_file, header=None, squeeze=True)

    increased_from_previous_count = (df > df.shift(1)).sum()

    print(f"Answer is: {increased_from_previous_count}")


if __name__ == "__main__":

    print("Using Pure Python:")
    use_pure_python()

    print("Using Pandas:")
    use_pandas()

    print("The correct answer is ->  1451  ")
