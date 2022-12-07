def find_parent(search_name, fs):
    for content in fs.values():
        if type(content) != dict:
            continue
        elif search_name in content.values():
            return content
        else:
            test = find_parent(search_name, content)
            if type(test) == dict:
                return test

    return ""


def get_size(file_object):
    if type(file_object) == int:
        return file_object

    erg = sum((get_size(elem) for elem in file_object.values()))
    # if erg >= 24933642:
    #     print(erg)
    return erg


def sum_sizes(directoy: dict, max_size: int):
    erg = 0
    for key, value in directoy.items():
        size = get_size(value)
        if size <= max_size and type(value) == dict:
            erg += size
        if type(value) == dict:
            erg += sum_sizes(value, max_size)

    return erg


def find_size(directoy: dict, min_size: int):
    erg = 1000000000
    for key, value in directoy.items():
        size = get_size(value)
        if size >= min_size and type(value) == dict:
            erg = min(erg, size)
        if type(value) == dict:
            erg = min(erg, find_size(value, min_size))

    return erg


def main():
    with open("input_07") as file:
        input_data = [line for line in file.read().strip().split('\n')]

    fs = {'/': dict()}
    current_dir: dict = fs['/']
    for line in input_data:
        if line[:4] == '$ cd':
            if line[5:] == '..':
                current_dir = find_parent(current_dir, fs)
            elif line[5:] == '/':
                current_dir = fs['/']
            else:
                current_dir = current_dir[line[5:]]
        elif line[:4] != '$ ls':
            if line[:3] == 'dir':
                name: str = line[4:]
                current_dir.update({name: {}})
            else:
                size, name = tuple(line.split(' '))
                current_dir[name] = int(size)

    print(fs)
    print(sum_sizes(fs, 100000))
    root_size = get_size(fs)
    to_delete = root_size - 40000000
    print(find_size(fs, to_delete))


if __name__ == '__main__':
    test_dict = {'abcd': {}}
    test_dict.update({"nomnom": {}})

    main()
