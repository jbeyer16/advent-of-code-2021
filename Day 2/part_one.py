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

    for command in commands:
        direction, amount = command.split(" ")
        amount = int(amount)

        if direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        elif direction == "forward":
            horizontal_position += amount

    answer = horizontal_position * depth

    print(f"Answer: {answer}")


if __name__ == "__main__":
    print("\n~~ Part One ~~\n")

    main()

    print("The correct answer is ->  2039912  ")

    print("\n~~~~~~~~~~~~~~\n")
