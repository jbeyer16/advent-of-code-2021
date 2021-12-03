from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():

    binary_numbers = [l.strip() for l in read_file("input")]

    most_common_string = ""
    for position_values in zip(*binary_numbers):
        position_sum = sum([int(p) for p in position_values])

        if position_sum < 500:
            most_common = "0"
        elif position_sum > 500:
            most_common = "1"
        else:
            raise Exception("sum was 500")

        most_common_string += most_common

    gamma_rate = int(most_common_string, 2)

    print(f"Most common: {most_common_string} -  Gamma Rate: {gamma_rate}")

    least_common_string = ""
    for char in most_common_string:
        if char == "1":
            least_common_string += "0"
        elif char == "0":
            least_common_string += "1"

    epsilon_rate = int(least_common_string, 2)

    print(f"Least common: {least_common_string} -  Epsilon Rate: {epsilon_rate}")

    power_consumption = gamma_rate * epsilon_rate

    print(f"Power consumption: {power_consumption}")


if __name__ == "__main__":
    print("\n~~ Part One ~~\n")

    main()

    print("The correct answer is ->  3959450  ")

    print("\n~~~~~~~~~~~~~~\n")
