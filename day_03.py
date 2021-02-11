from common.get_input import get_twoD_array

puzzle_input = get_twoD_array('input_files/03')


def print_twoD_arr(arr):
    for row in arr:
        print(row)


# double the array
def extend_array(arr):
    new_arr = []
    for row in arr:
        new_arr.append(row * 2)
    return new_arr


def part_one(inp):
    count = 0
    x = y = 0

    while(y+1 < len(inp)):
        y += 1
        x += 3

        if x > len(inp[0]):
            inp = extend_array(inp)

        if inp[y][x] == '#':
            count += 1

    return count


print(f'part_1: {part_one(puzzle_input)}')


def no_of_trees_for_slope(inp, x_inc, y_inc):
    count = 0
    x = y = 0

    while((y + y_inc) < len(inp)):
        y += y_inc
        x += x_inc

        if x + x_inc > len(inp[0]):
            inp = extend_array(inp)

        if inp[y][x] == '#':
            count += 1

    return count


def part_two(inp, slopes):
    count = []

    for i in slopes:
        count.append(no_of_trees_for_slope(inp, i[0], i[1]))

    answer = 1
    for val in count:
        answer *= val

    return answer


list_of_slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(f'part_2: {part_two(puzzle_input,list_of_slopes)}')
