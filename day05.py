def move_crates(state, move: tuple[int, int, int]):
    num, src, dest = move
    for _ in range(num):
        state[dest].append(state[src][-1])
        del state[src][-1]


def main_p1():
    with open("input_05") as file:
        data = [line for line in file.read().strip().split('\n')]

    state_str = data[:8]
    state_str = [line + "                               " for line in state_str]
    data = data[10:]
    data = [line.split(' ') for line in data]
    data = [(int(line[1]), int(line[3]), int(line[5])) for line in data]

    state = list(range(10))
    state[0] = []
    state[1] = [line[1] for line in state_str]
    state[2] = [line[5] for line in state_str]
    state[3] = [line[9] for line in state_str]
    state[4] = [line[13] for line in state_str]
    state[5] = [line[17] for line in state_str]
    state[6] = [line[21] for line in state_str]
    state[7] = [line[25] for line in state_str]
    state[8] = [line[29] for line in state_str]
    state[9] = [line[33] for line in state_str]

    state = [[crate for crate in stack if crate != ' '] for stack in state]
    state = [list(reversed(stack)) for stack in state]

    for move in data:
        move_crates(state, move)

    tops = ""
    for stack in state[1:]:
        tops += str(stack[-1])

    print(tops)


def move_crates_pt2(state, move):
    num, src, dest = move
    help_list = []
    for _ in range(num):
        help_list.append(state[src][-1])
        del state[src][-1]
    help_list.reverse()
    for crate in help_list:
        state[dest].append(crate)


def main_p2():
    with open("input_05") as file:
        data = [line for line in file.read().strip().split('\n')]

    state_str = data[:8]
    state_str = [line + "                               " for line in state_str]
    data = data[10:]
    data = [line.split(' ') for line in data]
    data = [(int(line[1]), int(line[3]), int(line[5])) for line in data]

    state = list(range(10))
    state[0] = []
    state[1] = [line[1] for line in state_str]
    state[2] = [line[5] for line in state_str]
    state[3] = [line[9] for line in state_str]
    state[4] = [line[13] for line in state_str]
    state[5] = [line[17] for line in state_str]
    state[6] = [line[21] for line in state_str]
    state[7] = [line[25] for line in state_str]
    state[8] = [line[29] for line in state_str]
    state[9] = [line[33] for line in state_str]

    state = [[crate for crate in stack if crate != ' '] for stack in state]
    state = [list(reversed(stack)) for stack in state]

    for move in data:
        move_crates_pt2(state, move)

    tops = ""
    for stack in state[1:]:
        tops += str(stack[-1])

    print(tops)


if __name__ == '__main__':
    main_p1()
    main_p2()
