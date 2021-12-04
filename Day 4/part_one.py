from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = read_file("input")

    draws = lines[0].split(",")

    puzzles_as_strings = [line.strip() for line in "".join(lines[1:]).split("\n\n")]

    puzzles_by_row = [
        list(map(lambda x: x.split(), puzzle.split("\n")))
        for puzzle in puzzles_as_strings
    ]

    puzzles_by_column = []
    for puzzle in puzzles_by_row:
        cols = []
        for ind in range(5):
            cols.append([row[ind] for row in puzzle])
        puzzles_by_column.append(cols)

    for i in range(len(draws)):
        called_numbers = draws[: i + 1]

        for puzzle_rows, puzzle_cols in zip(puzzles_by_row, puzzles_by_column):
            puzzle_is_bingo = check_puzzle_for_bingo(
                puzzle_rows, puzzle_cols, called_numbers
            )
            if puzzle_is_bingo:
                break
            else:
                continue
        else:
            puzzle_is_bingo = False

        if puzzle_is_bingo:
            break
        else:
            continue

    last_called = int(draws[i])

    winning_puzzle = [spot for row in puzzle_rows for spot in row]

    unmarked_numbers = [
        number for number in winning_puzzle if number not in called_numbers
    ]

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


def check_puzzle_for_bingo(rows, cols, vals):
    for collection in [*rows, *cols]:
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
    print("\n~~ Part One ~~\n")

    answer = main()
    print(f"Part One guess: {answer}")

    print("The correct answer is ->  25023  ")

    print("\n~~~~~~~~~~~~~~\n")
