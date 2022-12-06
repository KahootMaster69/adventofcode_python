def main_p1():
    with open("input_06") as file:
        input_stream = file.readline().strip()

    for i in range(len(input_stream)):
        if len(set(input_stream[i - 4:i])) == 4:
            print(i)
            break


def main_p2():
    pass


if __name__ == '__main__':
    main_p1()
    main_p2()
