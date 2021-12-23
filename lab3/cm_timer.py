from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.begin = None

    def __enter__(self):
        self.begin = time()

    def __exit__(self, exp_type, exp_value, traceback):
        print('time: {}'.format(time() - self.begin))


@contextmanager
def cm_timer_2():
    begin = time()
    yield
    print('time: {}'.format(time() - begin))


if __name__ == "__main__":
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)

