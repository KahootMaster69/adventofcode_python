def priority(elem: str) -> int:
    if elem.islower():
        return bytes(elem, 'utf8')[0] - bytes("a", 'utf8')[0] + 1
    return priority(elem.lower()) + 26


def main_p1():
    with open("input_03") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [(set(line[:int(len(line) / 2)]), set(line[int(len(line) / 2):])) for line in data]
    data = [elem for a, b in data for elem in a.intersection(b)]
    data = [priority(elem) for elem in data]
    print(sum(data))


def main_p2():
    with open("input_03") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [data[n:n + 3] for n in range(0, len(data), 3)]
    data = [(set(elf) for elf in group) for group in data]
    data = [item for a, b, c in data for item in a.intersection(b, c)]
    data = [priority(item) for item in data]
    print(sum(data))


if __name__ == '__main__':
    main_p1()
    main_p2()
