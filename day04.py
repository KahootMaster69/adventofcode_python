def main_p1():
    with open("input_04") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [(line.split(',')[0], line.split(',')[1]) for line in data]
    data = [(set(range(int(e1.split('-')[0]), int(e1.split('-')[1]) + 1)),
             set(range(int(e2.split('-')[0]), int(e2.split('-')[1]) + 1))) for e1, e2 in data]
    data = [(e1, e2) for e1, e2 in data if e1.intersection(e2) == e1 or e2.intersection(e1) == e2]
    print(len(data))


def main_p2():
    with open("input_04") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [(line.split(',')[0], line.split(',')[1]) for line in data]
    data = [(set(range(int(e1.split('-')[0]), int(e1.split('-')[1]) + 1)),
             set(range(int(e2.split('-')[0]), int(e2.split('-')[1]) + 1))) for e1, e2 in data]
    data = [(e1, e2) for e1, e2 in data if e1.intersection(e2)]
    print(len(data))


if __name__ == '__main__':
    main_p1()
    main_p2()
