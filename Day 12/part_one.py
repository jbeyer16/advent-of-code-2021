from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = [chunk.strip() for chunk in read_file("test_input")]

    answer = 0

    return answer


if __name__ == "__main__":
    print("\n~~ Day 12 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
