from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = read_file("input")

    # first line is list of numbers drawn for bingo
    draws = lines[0].split(",")

    # pull out each puzzle as a single string
    puzzles_as_strings = [line.strip() for line in "".join(lines[1:]).split("\n\n")]

    # keep the total for later
    total_number_of_puzzles = len(puzzles_as_strings)

    # get each puzzle's rows
    by_row = [
        list(map(lambda x: x.split(), puzzle.split("\n")))
        for puzzle in puzzles_as_strings
    ]

    # get each puzzle's columns
    by_column = []
    for puzzle in by_row:
        cols = []
        for ind in range(5):
            cols.append([row[ind] for row in puzzle])
        by_column.append(cols)

    # combine together cause they are evaluated the same way
    collections = [[*rows, *cols] for rows, cols in zip(by_row, by_column)]

    # loop over the length of the draws,
    for i in range(len(draws)):
        # the numbers up to and including (hence the +1) are the called numbers this round
        called_numbers = draws[: i + 1]

        # check which puzzles pass with this draw
        passed_puzzles = []
        for puzzle_num, collection in enumerate(collections):
            puzzle_is_bingo = check_puzzle_for_bingo(collection, called_numbers)
            if puzzle_is_bingo:
                passed_puzzles.append(puzzle_num)

        # now all the puzzles have been tested.
        if len(passed_puzzles) == total_number_of_puzzles:
            # all puzzles are passed, we need the last one
            last_puzzle_inds = [
                puzzle for puzzle in passed_puzzles if puzzle not in last_passed_puzzles
            ]
            assert len(last_puzzle_inds) == 1
            last_puzzle_ind = last_puzzle_inds[0]
            # don't do any more draws
            break
        else:
            # not all puzzles are passed, do another draw
            last_passed_puzzles = passed_puzzles
            continue

    # get the last draw
    last_called = int(draws[i])

    # get numbers in last puzzle by just grabbing it oriented by row
    last_puzzle = [number for row in by_row[last_puzzle_ind] for number in row]

    # see which numbers aren't used
    unmarked_numbers = [
        number for number in last_puzzle if number not in called_numbers
    ]

    # do the final math
    sum_of_unmarked = sum([int(number) for number in unmarked_numbers])

    return last_called * sum_of_unmarked


def check_collection_for_bingo(collection, vals):
    for spot in collection:
        if spot in vals:
            continue
        else:
            collection_is_bingo = False
            break
    else:
        collection_is_bingo = True

    return collection_is_bingo


def check_puzzle_for_bingo(collections, vals):
    for collection in collections:
        collection_is_bingo = check_collection_for_bingo(collection, vals)
        if collection_is_bingo:
            puzzle_is_bingo = True
            break
        else:
            continue
    else:
        puzzle_is_bingo = False

    return puzzle_is_bingo


if __name__ == "__main__":
    print("\n~~ Part Two ~~\n")

    answer = main()
    print(f"Part Two guess: {answer}")

    print("The correct answer is ->  2634  ")

    print("\n~~~~~~~~~~~~~~\n")
