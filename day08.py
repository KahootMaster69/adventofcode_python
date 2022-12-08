def main_p1():
    with open("input_08") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [[int(tree) for tree in line] for line in data]
    visible = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(data) - 1 or j == len(row) - 1:
                visible += 1
            elif max(row[:j]) < tree:
                visible += 1
            elif max(row[j + 1:]) < tree:
                visible += 1
            elif max([row[j] for row in data[:i]]) < tree:
                visible += 1
            elif max([row[j] for row in data[i + 1:]]) < tree:
                visible += 1

    print(visible)


def get_score(grid, row_index, col_index) -> int:
    row = grid[row_index]
    col = [row[col_index] for row in grid]
    max_height = grid[row_index][col_index]
    score = 1

    if row_index == 0 or col_index == 0 or row_index == len(grid) - 1 or col_index == len(row) - 1:
        return 0

    view = reversed(row[:col_index])
    count = 0
    for tree in view:
        if tree <= max_height:
            count += 1
        if tree >= max_height:
            break
    score *= count

    view = row[col_index + 1:]
    count = 0
    for tree in view:
        if tree <= max_height:
            count += 1
        if tree >= max_height:
            break
    score *= count

    view = reversed(col[:row_index])
    count = 0
    for tree in view:
        if tree <= max_height:
            count += 1
        if tree >= max_height:
            break
    score *= count

    view = col[row_index + 1:]
    count = 0
    for tree in view:
        if tree <= max_height:
            count += 1
        if tree >= max_height:
            break
    score *= count

    return score


def main_p2():
    with open("input_08") as file:
        data = [line for line in file.read().strip().split('\n')]

    data = [[int(tree) for tree in line] for line in data]
    max_score = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            max_score = max(max_score, get_score(data, i, j))

    print(max_score)


if __name__ == '__main__':
    main_p1()
    main_p2()
