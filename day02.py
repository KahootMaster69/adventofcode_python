def main():
    with open("input_02") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [(line[0], line[2]) for line in data]
    score = 0
    matchups = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3, ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}
    for matchup in data:
        score += matchups[matchup]

    print(score)


if __name__ == '__main__':
    main()
