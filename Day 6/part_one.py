from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    initial_state = [
        int(x) for x in [line.strip() for line in read_file("input")][0].split(",")
    ]

    day_count = 80
    state = initial_state

    print(f"Initial State: {state_as_string(state)}")
    for day in range(1, day_count + 1):
        new_state = []
        add_new_count = 0
        for fish in state:
            new_timer, did_reproduce = simulate_day(fish)
            if did_reproduce:
                add_new_count += 1
            new_state.append(new_timer)

        for _ in range(add_new_count):
            new_state.append(8)

        state = new_state

        print(f"After {day:2d} Days: {state_as_string(new_state)}")

    answer = len(new_state)

    return answer


def simulate_day(timer):
    if timer > 0:
        timer -= 1
        did_reproduce = False
    else:
        timer = 6
        did_reproduce = True

    return timer, did_reproduce


def state_as_string(state):
    return ",".join(map(str, state))


if __name__ == "__main__":
    print("\n~~ Day 6 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
