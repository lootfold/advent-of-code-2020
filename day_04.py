import os
import re
import sys


class Passport:
    def __init__(self, str_inp):
        key_val_pairs = self._get_key_val_from(str_inp)
        self.byr = key_val_pairs['byr']
        self.iyr = key_val_pairs['iyr']
        self.eyr = key_val_pairs['eyr']
        self.hgt = key_val_pairs['hgt']
        self.hcl = key_val_pairs['hcl']
        self.ecl = key_val_pairs['ecl']
        self.pid = key_val_pairs['pid']
        # self.cid = key_val_pairs[self.Key.CID]

    def is_valid_str_inp(keys_to_verify, str_inp):
        for k in keys_to_verify:
            if k not in str_inp:
                return False
        return True

    def _get_key_val_from(self, str_inp):
        key_val = str_inp.split(' ')
        pairs = {}
        for i in key_val:
            key, value = i.split(':')
            pairs[key] = value

        return pairs

    def _is_valid_range(self, min, max, value):
        value = int(value)
        if value >= min and value <= max:
            return True
        else:
            return False

    def _is_valid_byr(self):
        return self._is_valid_range(1920, 2002, self.byr)

    def _is_valid_iyr(self):
        return self._is_valid_range(2010, 2020, self.iyr)

    def _is_valid_eyr(self):
        return self._is_valid_range(2020, 2030, self.eyr)

    def _is_valid_hgt(self):
        if re.compile(r'^[0-9]{3}cm$|^[0-9]{2}in$').match(self.hgt) == None:
            return False
        if 'in' in self.hgt:
            return self._is_valid_range(59, 76, int(self.hgt[0:2]))
        elif 'cm' in self.hgt:
            return self._is_valid_range(150, 193, int(self.hgt[0:3]))

    def _is_valid_hcl(self):
        if re.compile(r'^#[0-9a-f]{6}').match(self.hcl):
            return True
        else:
            return False

    def _is_valid_ecl(self):
        valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if self.ecl in valid_values:
            return True
        else:
            return False

    def _is_valid_pid(self):
        if re.compile(r'^[0-9]{9}$').match(self.pid):
            return True
        else:
            return False

    def is_valid(self):
        if (
            self._is_valid_byr()
            and self._is_valid_iyr()
            and self._is_valid_eyr()
            and self._is_valid_hcl()
            and self._is_valid_ecl()
            and self._is_valid_hgt()
            and self._is_valid_pid()
        ):
            return True
        else:
            return False


keys_to_validate = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

inp = open(os.path.join(sys.path[0], 'input_files/04'), 'r').read()
inp = inp.replace('\n', ' ')
inp = inp.split('  ')


def part_1():
    count = 0
    for i in inp:
        valid = Passport.is_valid_str_inp(keys_to_validate, i)
        if valid:
            count += 1

    return count


print(f'part 1: {part_1()}')


def part_2():
    count = 0
    for each in inp:
        if Passport.is_valid_str_inp(keys_to_validate, each):
            p = Passport(each)
            if p.is_valid():
                count += 1

    return count


print(f'part 2: {part_2()}')
