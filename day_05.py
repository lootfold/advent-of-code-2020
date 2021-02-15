from common.get_input import get_str_array

inp = get_str_array('input_files/05')


def get_row(bpass):
    min, max = 0, 127
    x = bpass[0:7]
    for char in x:
        d = int((max-min)/2)
        if char == 'F':
            max = min + d
        elif char == 'B':
            min = min + d + 1
    if min == max:
        return min


def get_col(bpass):
    min, max = 0, 7
    x = bpass[7:]
    for char in x:
        d = int((max-min)/2)
        if char == 'L':
            max = min + d
        elif char == 'R':
            min = min + d + 1
    if min == max:
        return min


def get_seat_id(bpass):
    return get_row(bpass) * 8 + get_col(bpass)


def part_1():
    max = 0
    for i in inp:
        seat_id = get_seat_id(i)
        if max < seat_id:
            max = seat_id
    return max


def part_2():
    seats = []
    for i in inp:
        seats.append(get_seat_id(i))
    seats.sort()
    for i in range(0, len(seats) - 1):
        if seats[i] + 1 != seats[i+1]:
            return seats[i] + 1


print(f'part_1: {part_1()}')
print(f'part_2: {part_2()}')
