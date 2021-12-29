from pathlib import Path
import math


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    height_map = [
        [int(c) for c in string]
        for string in [line.strip() for line in read_file("input")]
    ]

    num_cols = len(height_map[0])
    num_rows = len(height_map)

    low_points = []
    for row in range(num_rows):
        print(f"Row: {row+1}")
        for col in range(num_cols):
            position = height_map[row][col]
            if is_position_low_point(position, height_map, row, col):
                low_points.append(position)
                print(f"LP: {position} at {row+1}, {col+1}")
            else:
                continue

    risk_levels = [point + 1 for point in low_points]

    print(f"Low points are {low_points}")
    print(f"Risk levels are {risk_levels}")
    answer = sum(risk_levels)

    return answer


def is_position_low_point(position, height_map, row, col):
    # check above
    try:
        if row == 0:
            above_lower = True
        else:
            adjacent_value = height_map[row - 1][col]
            if adjacent_value > position:
                above_lower = True
            else:
                above_lower = False
    except IndexError:
        above_lower = True

    # check below
    try:
        adjacent_value = height_map[row + 1][col]
        if adjacent_value > position:
            below_lower = True
        else:
            below_lower = False
    except IndexError:
        below_lower = True

    # check right
    try:
        adjacent_value = height_map[row][col + 1]
        if adjacent_value > position:
            right_lower = True
        else:
            right_lower = False
    except IndexError:
        right_lower = True

    # check left
    try:
        if col == 0:
            left_lower = True
        else:
            adjacent_value = height_map[row][col - 1]
            if adjacent_value > position:
                left_lower = True
            else:
                left_lower = False
    except IndexError:
        left_lower = True

    return all([above_lower, below_lower, right_lower, left_lower])


if __name__ == "__main__":
    print("\n~~ Day 9 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
