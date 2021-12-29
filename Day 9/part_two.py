from pathlib import Path
import copy


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def make_basin(rows, cols):
    basin = []
    for row in range(rows):
        new_col = []
        for col in range(cols):
            new_col.append(False)

        basin.append(new_col)

    return basin


def main():
    height_map = [
        [int(c) for c in string]
        for string in [line.strip() for line in read_file("input")]
    ]

    num_cols = len(height_map[0])
    num_rows = len(height_map)

    low_points = []
    for row in range(num_rows):
        for col in range(num_cols):
            point = height_map[row][col]
            if is_low_point(point, height_map, row, col):
                low_points.append((row, col))
            else:
                continue
    basin_sizes = []
    # print(f"Low points are {low_points}")
    for point in low_points:
        basin_sum = 0

        new_basin = make_basin(num_rows, num_cols)

        # start at each low point and recursively uncover its region
        # search_region(visited=reference, position=point)
        searched_basin = explore_basin(
            basin=new_basin, height_map=height_map, point=point
        )

        for a in searched_basin:
            basin_sum += sum(a)

        basin_sizes.append(basin_sum)
        print(f"Point {point} is {basin_sum}")

    three_largest = sorted(basin_sizes)[-3:]

    answer = 1
    for number in three_largest:
        answer *= number

    return answer


def explore_basin(basin, height_map, point, to_check=[]):
    # basin is T/F of if its a basin
    # map is the height values
    # point is the location

    basin = update_reference(basin, point)

    new_points = explore_adjacent_heights(point, height_map, basin)

    to_check = list(set([*to_check, *new_points]))

    # print(f"\nChecked {point}.  To Check: {to_check}")
    for a in basin:
        # print(a)
        pass

    if len(to_check) == 0:
        return basin
    else:
        new_point = to_check.pop()
        return explore_basin(basin, height_map, new_point, to_check)


def search_region(visited, position, to_check=[]):
    visited = update_reference(visited, position)

    adjacent = explore_adjacent(position, visited)

    to_check = list(set([*to_check, *adjacent]))

    print(f"\nChecked {position}.  To Check: {to_check}")
    for a in visited:
        print(a)

    if len(to_check) == 0:
        return True
    else:
        new_point = to_check.pop()
        return search_region(visited, new_point, to_check)


def update_reference(visited, position):
    visited[position[0]][position[1]] = True
    return visited


def explore_adjacent_heights(position, height_map, visited):
    new_to_check = []
    # check above
    if position[0] != 0:
        new_position = (position[0] - 1, position[1])

        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            if height_map[new_position[0]][new_position[1]] < 9:
                new_to_check.append(new_position)

    # check below
    try:
        new_position = (position[0] + 1, position[1])
        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            if height_map[new_position[0]][new_position[1]] < 9:
                new_to_check.append(new_position)
    except IndexError:
        pass

    # check right
    try:
        new_position = (position[0], position[1] + 1)
        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            if height_map[new_position[0]][new_position[1]] < 9:
                new_to_check.append(new_position)
    except IndexError:
        pass

    # check left
    if position[1] != 0:
        new_position = (position[0], position[1] - 1)
        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            if height_map[new_position[0]][new_position[1]] < 9:
                new_to_check.append(new_position)

    return new_to_check


def explore_adjacent(position, visited):
    new_to_check = []
    # check above
    if position[0] != 0:
        new_position = (position[0] - 1, position[1])

        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            new_to_check.append(new_position)

    # check below
    try:
        new_position = (position[0] + 1, position[1])
        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            new_to_check.append(new_position)
    except IndexError:
        pass

    # check right
    try:
        new_position = (position[0], position[1] + 1)
        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            new_to_check.append(new_position)
    except IndexError:
        right_lower = True

    # check left
    if position[1] != 0:
        new_position = (position[0], position[1] - 1)
        has_been_checked = visited[new_position[0]][new_position[1]]
        if not has_been_checked:
            new_to_check.append(new_position)

    return new_to_check


def is_low_point(point, height_map, row, col):
    # check above
    try:
        if row == 0:
            above_lower = True
        else:
            adjacent_value = height_map[row - 1][col]
            if adjacent_value > point:
                above_lower = True
            else:
                above_lower = False
    except IndexError:
        above_lower = True

    # check below
    try:
        adjacent_value = height_map[row + 1][col]
        if adjacent_value > point:
            below_lower = True
        else:
            below_lower = False
    except IndexError:
        below_lower = True

    # check right
    try:
        adjacent_value = height_map[row][col + 1]
        if adjacent_value > point:
            right_lower = True
        else:
            right_lower = False
    except IndexError:
        right_lower = True

    # check left
    try:
        if col == 0:
            left_lower = True
        else:
            adjacent_value = height_map[row][col - 1]
            if adjacent_value > point:
                left_lower = True
            else:
                left_lower = False
    except IndexError:
        left_lower = True

    return all([above_lower, below_lower, right_lower, left_lower])


if __name__ == "__main__":
    print("\n~~ Day 9 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
