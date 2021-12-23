import json
import sys
from field import *
from gen_random import *
from unique import *
from print_result import *
from cm_timer import *

path = "/home/anna/PycharmProjects/lab_python_fp/data_light.json"

with open(path, 'r') as f:
    data = json.load(f)


@print_result
def f1(x):
    return sorted(list(Unique(field(x, "job-name"))), key=str.lower)


@print_result
def f2(x):
    return list(filter(lambda s: s.split()[0].lower() == "программист", x))


@print_result
def f3(x):
    return list(map(lambda s: s + " с опытом Python", x))


@print_result
def f4(x):
    res = list(zip(x, list(gen_random(len(x),100000,200000))))
    return list(map(lambda s: s[0] + ", зарплата " + str(s[1]) + " руб.", res))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
