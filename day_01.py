from common.get_input import get_int_array


puzzle_input = get_int_array('input_files/01.txt')


def part_1(puzzle_input):
    for i in puzzle_input:
        remaining = puzzle_input[puzzle_input.index(i) + 1:]
        for j in remaining:
            if (i+j == 2020):
                return(i*j)


print(f'part 1 answer: {part_1(puzzle_input)}')


def part_2(puzzle_input):
    for i in puzzle_input:
        for j in puzzle_input[puzzle_input.index(i) + 1:]:
            for k in puzzle_input[puzzle_input.index(j) + 1:]:
                if (i+j+k == 2020):
                    return(i*j*k)


print(f'part 2 answer: {part_2(puzzle_input)}')
