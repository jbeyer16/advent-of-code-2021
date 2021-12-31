from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = [chunk.strip() for chunk in read_file("input")]

    # get the unique caves that can be visited
    caves = set()
    for line in lines:
        for cave in line.split('-'):
            caves.add(cave)

    # crate a mapping for each cave
    cave_mapping = {}
    for cave in caves:
        cave_mapping[cave] = []
        for line in lines:
            options = line.split('-')
            if cave in options:
                for option in options:
                    if option != cave:
                        cave_mapping[cave].append(option)


    all_paths = []

    traverse_path('start', cave_mapping, all_paths)

    for path in all_paths:
        print(path)

    answer = len(all_paths)

    return answer

def is_path_done(path):
    current_cave = path[-1]

    if current_cave == 'end' or (len(path) >1 and current_cave == 'start'):
        return True

    num_duplicated = 0
    for cave in set(path):
        if cave == cave.upper():
            continue

        if path.count(cave) >= 3:
            return True
        elif path.count(cave) == 2:
            num_duplicated += 1
            if num_duplicated > 1:
                return True
    
    return False

def traverse_path(current_cave, mapping, all_paths, current_path=[]):
    temp_path = current_path + [current_cave]

    if is_path_done(temp_path):
        if current_cave == 'end':
            all_paths.append(temp_path)
        return None
    else:
        for cave in mapping[current_cave]:
            traverse_path(cave, mapping, all_paths, temp_path)


if __name__ == "__main__":
    print("\n~~ Day 12 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
