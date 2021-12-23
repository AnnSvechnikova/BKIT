# Здесь должна быть реализация декоратора
def print_result(func):
    def decorated_func(args=None):
        print(func.__name__)
        if args:
            res = func(args)
        else:
            res = func()
        if isinstance(res, dict):
            for k, v in res.items():
                print('{} = {}'.format(k, v))
        elif isinstance(res, list):
            for i in res:
                print(i)
        else:
            print(res)
        return res
    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == "__main__":
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()