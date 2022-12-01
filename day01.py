def main():
    with open("input_01") as file:
        current_sum = 0
        max_sum = 0
        for line in file.readlines():
            line = line[:-1]
            if not line:
                max_sum = max(current_sum, max_sum)
                current_sum = 0
            else:
                current_sum += int(line)

    print(max_sum)


if __name__ == '__main__':
    main()
