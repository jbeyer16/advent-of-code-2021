from pathlib import Path
from collections import Counter

def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    lines = [chunk.strip() for chunk in read_file("input")]

    # parse the rules from the template
    lines_i = lines.__iter__()
    template = next(lines_i)

    rules = {}
    for line in lines_i:
        if '->' in line:
            pair, element = line.split('->')
            pair = pair.strip()
            element = element.strip()
            rules[pair] = element

    template_dict = Counter()
    for pair in zip(template, template[1:]):
        pair = ''.join(pair)
        template_dict[pair] += 1

    letter_counts = Counter()
    steps = 40
    print(f"Starting with: {template_dict}")
    for letter in template:
        letter_counts[letter] += 1

    for i in range(steps):
        template_dict, letter_counts = run_step(template_dict, rules, letter_counts)
        print(f"After step {i+1}: {template_dict}")

    print(letter_counts)
    answer = max(letter_counts.items(), key=lambda x: x[1])[1] - min(letter_counts.items(), key=lambda x: x[1])[1]    
    return answer

def run_step(polymer_dict, rules, counts):
    new_polymer_dict = Counter()

    for pair, count in polymer_dict.items():
        pair = ''.join(pair)
        # print(pair)
        if pair in rules:
            element = rules[pair]
            new_pair_1 = pair[0] + element
            new_pair_2 = element + pair[1]

            new_polymer_dict[new_pair_1] += count
            new_polymer_dict[new_pair_2] += count

            counts[element] += count
        else:
            raise NotImplementedError('no match')

    return new_polymer_dict, counts

if __name__ == "__main__":
    print("\n~~ Day 14 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
