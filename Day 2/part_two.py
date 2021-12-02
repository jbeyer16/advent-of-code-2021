from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    commands = read_file("input")

    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        direction, amount = command.split(" ")
        amount = int(amount)

        if direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        elif direction == "forward":
            horizontal_position += amount
            depth += aim * amount

    answer = horizontal_position * depth

    print(f"Answer: {answer}")


if __name__ == "__main__":
    print("\n~~ Part Two ~~\n")

    main()

    print("The correct answer is ->  1942068080  ")

    print("\n~~~~~~~~~~~~~~\n")
