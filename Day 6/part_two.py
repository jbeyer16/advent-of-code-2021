from pathlib import Path
from collections import defaultdict


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    initial_state = [line.strip() for line in read_file("input")][0].split(",")

    day_count = 256

    state = State(initial_state)

    print(f"Initial State: {','.join(initial_state)}")
    for day in range(1, day_count + 1):
        state.update()

    answer = state.sum()

    return answer


class State:
    def __init__(self, seed=None):
        self.state = {str(i): 0 for i in range(8 + 1)}

        if seed is not None:
            for fish in seed:
                self.state[fish] += 1

    def sum(self):
        sum = 0

        for count in self.state.values():
            sum += count

        return sum

    def update(self):
        new_state = State()
        for timer, count in self.state.items():
            new_timer = int(timer) - 1

            if new_timer == -1:
                new_state.state["8"] = count
                new_state.state["6"] += count
            else:
                new_state.state[str(new_timer)] += count
        self.state = new_state.state


if __name__ == "__main__":
    print("\n~~ Day 6 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
