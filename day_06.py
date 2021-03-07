import re

file = open('input_files/06')
input = file.read()
file.close()


def part_1(inp):
    inp = list(re.sub('\n{2}', '|', inp).split('|'))

    count = 0
    for i in inp:
        x = i.replace('\n', '')
        s = set(list(x))
        count += len(s)

    return count


def part_2(inp):
    inp = list(re.sub('\n{2}', '|', inp).split('|'))

    groups = []
    for i in inp:
        x = list(i.split('\n'))
        x = [set(list(y)) for y in x]
        groups.append(x)

    count = 0
    for i in groups:
        common = i[0]
        for j in range(1, len(i)):
            common &= i[j]

        count += len(common)

    return count


print(f'part_1: {part_1(input)}')
print(f'part_2: {part_2(input)}')
