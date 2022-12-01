def main():
    with open("input_01") as file:
        current_sum = 0
        max_sums = [0, 0, 0]
        for line in file.readlines():
            line = line[:-1]
            if not line:
                if current_sum > max_sums[0]:
                    max_sums[0] = current_sum
                    max_sums.sort()
                current_sum = 0
            else:
                current_sum += int(line)

    print(sum(max_sums))


if __name__ == '__main__':
    main()
