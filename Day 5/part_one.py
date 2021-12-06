from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = [line.strip() for line in read_file("input")]

    line_points = []
    for line in lines:
        start, end = line.split("->")

        start = [int(x) for x in start.strip().split(",")]

        end = [int(x) for x in end.strip().split(",")]

        if start[0] == end[0]:
            range_start = min([start[1], end[1]])
            range_end = max([start[1], end[1]]) + 1
            for i in range(range_start, range_end):
                point = (start[0], i)
                line_points.append(point)
            # horizontal
        elif start[1] == end[1]:
            range_start = min([start[0], end[0]])
            range_end = max([start[0], end[0]]) + 1
            for i in range(range_start, range_end):
                point = (i, start[1])
                line_points.append(point)
            # vertical
        else:
            continue

    unique_points = set(line_points)

    num_two_overlaps = 0
    for point in unique_points:
        if line_points.count(point) >= 2:
            num_two_overlaps += 1

    answer = num_two_overlaps

    return answer


if __name__ == "__main__":
    print("\n~~ Day 5 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
