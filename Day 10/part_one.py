from pathlib import Path
from typing import ParamSpecKwargs

OPEN = ["(", "[", "<", "{"]
CLOSE = [")", "]", ">", "}"]
SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def get_char_mate(in_char):
    if in_char == "(":
        out_char = ")"
    elif in_char == "[":
        out_char = "]"
    elif in_char == "<":
        out_char = ">"
    elif in_char == "{":
        out_char = "}"

    return out_char


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = [chunk.strip() for chunk in read_file("input")]

    invalid, valid, incomplete = [], [], []

    invalid_score = 0
    for line in lines:
        result, score = validate_line(line)

        if result == True:
            result = "valid"
            valid.append(line)
            pass
        elif result == False:
            result = "invalid"
            invalid_score += score
            invalid.append(line)
            pass
        elif result is None:
            result = "incomplete"
            incomplete.append(line)
            pass

        print(f"Line :: {line} :: is {result}")

    answer = invalid_score

    return answer


def validate_line(line_string):
    # checks line char by char for validity.
    # True if valid, False if invalid, None if incomplete
    starts = []
    ends = []

    for character in line_string:
        if character in OPEN:
            starts.append(character)
            ends.append(get_char_mate(character))
        elif character in CLOSE:
            if character == ends[-1]:
                starts.pop(-1)
                ends.pop(-1)
                continue
            else:
                line_score = SCORE[character]
                return False, line_score
    else:
        return None, None


if __name__ == "__main__":
    print("\n~~ Day 10 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
