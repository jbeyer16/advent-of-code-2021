from pathlib import Path


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

    steps = 10
    print(f"Template: {template}")
    for i in range(steps):
        template = run_step(template, rules)
        print(f"After step {i+1}: {len(template)}")

    # scoring
    letters = set(template)
    letter_counts = []
    for letter in letters:
        letter_counts.append((letter, template.count(letter)))

    answer = max(letter_counts, key=lambda x: x[1])[1] - min(letter_counts, key=lambda x: x[1])[1]    
    return answer

def run_step(polymer, rules):
    inserts = []
    for pair in zip(polymer, polymer[1:]):
        pair = ''.join(pair)
        if pair in rules:
            new_element = rules[pair]
            insert_string = new_element
        else:
            insert_string = ''
        
        inserts.append(insert_string)
    
    # need one blank to end it
    inserts.append('')

    new_polymer = ''
    for p, i in zip(polymer, inserts):
        new_polymer += p
        new_polymer += i

    return new_polymer

if __name__ == "__main__":
    print("\n~~ Day 14 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
