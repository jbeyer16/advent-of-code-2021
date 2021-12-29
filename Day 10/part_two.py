from pathlib import Path
from typing import ParamSpecKwargs

OPEN = ["(", "[", "<", "{"]
CLOSE = [")", "]", ">", "}"]
SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
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

    corrupt_lines, incomplete_lines = [], []

    for line in lines:
        result = validate_line(line)

        if result == True:
            result = "incomplete"
            incomplete_lines.append(line)
            pass
        elif result == False:
            result = "invalid"
            corrupt_lines.append(line)
            pass
        else:
            raise NotImplementedError("Invalid result")

    scores = []
    for line in incomplete_lines:
        closing_string = repair_line(line)
        string_score = score_string(closing_string)
        scores.append(string_score)
        print(f"String: {closing_string} :: Score: {string_score}")

    answer = sorted(scores)[round(len(scores) / 2)]

    return answer


def score_string(string):
    score = 0

    for char in string:
        score = score * 5 + SCORE[char]

    return score


def repair_line(line_string):
    # checks line char by char and determines characters needed to append to make it valid
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

    closing_string = "".join(reversed(ends))

    return closing_string


def validate_line(line_string):
    # checks line char by char for corruption.
    # True if incomplete, False if corrupted
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
                break
    else:
        return True

    return False


if __name__ == "__main__":
    print("\n~~ Day 10 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
