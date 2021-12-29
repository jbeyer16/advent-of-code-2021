from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    # init the grid
    grid = [
        [int(o) for o in row] for row in [row.strip() for row in read_file("input")]
    ]

    num_steps = 100
    # model steps
    total_flashes = 0
    for _ in range(1, num_steps + 1):
        grid, flashes = run_step(grid)

        total_flashes += flashes
        print(f"After {_} step. {flashes} this step. {total_flashes} total.")
        # for r in grid:
        #     print(r)

    answer = total_flashes

    return answer


def run_step(grid):
    # updates a grid due to a step iteration
    # Rules:
    # - each square gets + 1
    # - if > 9, flash adds + 1 to surrounding (all dir)
    # - if flashed, value is now 0, can't be increased any more

    # increase all by 1
    grid = init_step(grid)

    # process any flashes
    grid, flash_count = process_flashes(grid=grid, total_flashes=0)

    return grid, flash_count


def process_flashes(grid, total_flashes):
    # find flash points ( > 9)
    flash_points = find_flash_points(grid)

    if len(flash_points) == 0:
        return grid, total_flashes
    else:
        new_point = flash_points.pop()
        total_flashes += 1

        grid = update_grid_with_flash_at_point(grid, new_point)

        return process_flashes(grid, total_flashes)


def update_grid_with_flash_at_point(grid, point):
    # flash here, so set to 0
    grid[point[0]][point[1]] = 0

    # update around it

    # update above
    if point[0] != 0:
        # directly above
        above_point = (point[0] - 1, point[1])
        set_grid_val(grid, above_point)

        # diagonal right
        try:
            above_right = (point[0] - 1, point[1] + 1)
            set_grid_val(grid, above_right)
        except IndexError:
            pass

        # diagonal left
        if point[1] != 0:
            above_left = (point[0] - 1, point[1] - 1)
            set_grid_val(grid, above_left)

    # update below
    try:
        # directly below
        below_point = (point[0] + 1, point[1])
        set_grid_val(grid, below_point)

        # diagonal right
        try:
            below_right = (point[0] + 1, point[1] + 1)
            set_grid_val(grid, below_right)
        except IndexError:
            pass

        # diagonal left
        if point[1] != 0:
            below_left = (point[0] + 1, point[1] - 1)
            set_grid_val(grid, below_left)
    except IndexError:
        pass

    # update right
    try:
        right_point = (point[0], point[1] + 1)
        set_grid_val(grid, right_point)
    except IndexError:
        pass

    # update left
    if point[1] != 0:
        left_point = (point[0], point[1] - 1)
        set_grid_val(grid, left_point)

    return grid


def find_flash_points(grid):
    points = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] > 9:
                points.append((row, col))
    return points


def init_step(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] += 1

    return grid


def set_grid_val(grid, point):
    current_value = grid[point[0]][point[1]]

    if current_value == 0:
        pass
    elif current_value > 9:
        grid[point[0]][point[1]] = 10
    else:
        grid[point[0]][point[1]] += 1

    return grid


if __name__ == "__main__":
    print("\n~~ Day 11 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
