import os
import sys


def get_int_array(file_name):
    inp = open(os.path.join(sys.path[0], file_name), 'r').read().splitlines()
    return [int(i) for i in inp]


def get_str_array(file_name):
    inp = open(os.path.join(sys.path[0], file_name), 'r').read().splitlines()
    return inp
