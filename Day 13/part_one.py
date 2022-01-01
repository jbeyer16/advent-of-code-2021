from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = [chunk.strip() for chunk in read_file("input")]

    coords = []
    folds = []

    for line in lines:
        if 'fold' in line:
            instructions = line.split(' ')[2]
            axis, value = instructions.split('=')
            folds.append((axis, value))
        elif line != '':
            coords_str = line.split(',')
            coord = (int(coords_str[0]), int(coords_str[1]))
            coords.append(coord)

    # go through each fold
    for fold in folds:
        fold_axes = fold[0]
        fold_loc = int(fold[1])

        coord_ind = 0 if fold_axes == 'x' else 1

        print(f"Folding along {fold_axes}={fold_loc}")
        # collect the new coords based on the fold
        new_coords = []
        
        # go through all the coords
        for coord in coords:
            print(f"Folding {coord}")
            new_coord = list(coord)
            if coord[coord_ind] > fold_loc:
                dist_from_fold = coord[coord_ind] - fold_loc
                
                new_coord[coord_ind] -= 2 * dist_from_fold
            print(f"New Coord is {new_coord}")
            new_coords.append(tuple(new_coord))

        coords = set(new_coords)
        break
    
    answer = len(coords)
    return answer


if __name__ == "__main__":
    print("\n~~ Day 13 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
