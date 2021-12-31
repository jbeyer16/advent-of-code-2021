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
        cave_mapping[cave] = {
            'canRevisit': cave == cave.upper(),
            'adjacent': []
        }
        for line in lines:
            options = line.split('-')
            if cave in options:
                for option in options:
                    if option != cave:
                        cave_mapping[cave]['adjacent'].append(option)


    all_paths = []

    traverse_path('start', cave_mapping, all_paths)

    for path in all_paths:
        print(path)

    answer = len(all_paths)

    return answer

def traverse_path(current_cave, mapping, all_paths, current_path=[]):
    if current_cave in current_path and not mapping[current_cave]['canRevisit']:
        # upcoming cave is already in the path and we can't revisit it
        # path is invalide, don't update our tracker
        return None
    else:
        # assume the cave is visitable
        temp_path = current_path + [current_cave]

    if current_cave == 'end':
        # if this cave is the end, update our tracker
        all_paths.append(temp_path)
    else:
        # otherwise see what options are available
        for cave in mapping[current_cave]['adjacent']:
            # test the next cave
            traverse_path(cave, mapping, all_paths, temp_path)


if __name__ == "__main__":
    print("\n~~ Day 12 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
