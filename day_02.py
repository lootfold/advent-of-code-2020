from sys import flags
from common.get_input import get_str_array

puzzle_input = get_str_array('input_files/02')


def part_1(inp):
    valid_passwords = 0
    for x in inp:
        min = int(x.split('-')[0])
        max = int(x.split('-')[1].split(' ')[0])
        letter = x.split(':')[0][-1]
        password = x.split('-')[1].split(' ')[-1]
        # print(f'min: {min}, max: {max}, letter: {letter}, password: {password}')

        count = list(password).count(letter)
        if count >= min and count <= max:
            valid_passwords += 1

    return valid_passwords


def part_2(inp):
    valid_passwords = 0
    for pos1 in inp:
        index1 = int(pos1.split('-')[0])
        index2 = int(pos1.split('-')[1].split(' ')[0])
        letter = pos1.split(':')[0][-1]
        password = pos1.split('-')[1].split(' ')[-1]

        pos1 = password[index1-1] == letter
        pos2 = password[index2-1] == letter

        if (pos1 and pos2 == False) or (pos1 == False and pos2):
            valid_passwords += 1

    return valid_passwords


print(f'part 1: {part_1(puzzle_input)}')
print(f'part 2: {part_2(puzzle_input)}')
