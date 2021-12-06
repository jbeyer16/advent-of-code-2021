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
            # diagonal
            x_start = start[0]
            if end[0] > start[0]:
                x_incr = 1
            elif end[0] < start[0]:
                x_incr = -1
            x_end = end[0] + x_incr

            y_start = start[1]
            if end[1] > start[1]:
                y_incr = 1
            elif end[1] < start[1]:
                y_incr = -1
            y_end = end[1] + y_incr

            for i, j in zip(
                range(x_start, x_end, x_incr), range(y_start, y_end, y_incr)
            ):
                point = (i, j)
                line_points.append(point)

    unique_points = set(line_points)

    num_two_overlaps = 0
    for point in unique_points:
        if line_points.count(point) >= 2:
            num_two_overlaps += 1

    answer = num_two_overlaps

    return answer


if __name__ == "__main__":
    print("\n~~ Day 5 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
