from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def whittle(list_of_number_strings, kind, position=0):
    """ Recursive! """
    # list of numbers, pull values for a position
    position_sum = sum(
        [int(number_string[position]) for number_string in list_of_number_strings]
    )

    # Use the sum to see how many are there, determine which values to keep
    middle = len(list_of_number_strings) / 2
    if position_sum < middle:
        # if sum is less than middle, most common is a 0
        # oxygen keeps most common
        keep = "0" if kind == "oxygen" else "1"
    elif position_sum >= middle:
        # if sum is greater than or equal to middle, most common is a 1
        # oxygen keeps most common
        keep = "1" if kind == "oxygen" else "0"

    # filter the list down based on matching that keep value on that position
    new_list_of_number_strings = [
        number_string
        for number_string in list_of_number_strings
        if number_string[position] == keep
    ]

    if len(new_list_of_number_strings) > 1:
        # if more than one, run again with next position
        return whittle(new_list_of_number_strings, kind, position + 1)
    else:
        # if just one is left, that's the final value
        return int(new_list_of_number_strings[0], 2)


def main():
    binary_numbers = [l.strip() for l in read_file("input")]

    oxygen_generator_rating = whittle(binary_numbers, "oxygen")

    co2_scrubber_rating = whittle(binary_numbers, "co2")

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    print(f"O2: {oxygen_generator_rating} -- CO2: {co2_scrubber_rating}")

    print(f"LS: {life_support_rating}")


if __name__ == "__main__":
    print("\n~~ Part Two ~~\n")

    main()

    print("The correct answer is ->  7440311  ")

    print("\n~~~~~~~~~~~~~~\n")
