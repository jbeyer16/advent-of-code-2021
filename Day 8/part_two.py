from pathlib import Path
import math


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    entries = read_file("input")

    final_sum = 0
    for entry in entries:
        patterns = entry.split("|")[0].strip()
        outputs = entry.split("|")[-1].strip()

        digits = patterns.split(" ")

        known = {}
        mapping = {}
        for digit in digits:
            digit = "".join(sorted(digit))

            if len(digit) == 2:
                k = "1"
            elif len(digit) == 3:
                k = "7"
            elif len(digit) == 4:
                k = "4"
            elif len(digit) == 7:
                k = "8"
            else:
                continue
            known[k] = digit
            mapping[digit] = int(k)

        for digit in digits:
            digit = "".join(sorted(digit))

            if len(digit) == 6:
                if all([d in digit for d in known["4"]]):
                    k = "9"
                elif all([d in digit for d in known["1"]]):
                    k = "0"
                else:
                    k = "6"
            else:
                continue

            known[k] = digit
            mapping[digit] = int(k)

        for digit in digits:
            digit = "".join(sorted(digit))

            if len(digit) == 5:
                if all([d in digit for d in known["1"]]):
                    k = "3"
                elif all([d in known["9"] for d in digit]):
                    k = "5"
                else:
                    k = "2"
            else:
                continue

            known[k] = digit
            mapping[digit] = int(k)

        output_str = ""
        for output in outputs.split(" "):
            output = "".join(sorted(output))
            output_str += str(mapping[output])

        final_sum += int(output_str)
    answer = final_sum

    return answer


if __name__ == "__main__":
    print("\n~~ Day 8 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
