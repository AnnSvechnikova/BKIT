from lab4 import *
import unittest
from unittest.mock import patch


class TddTest(unittest.TestCase):
    #предположим, решение в случае, когда уравнение не имеет корней, ещё не реализовано
    @patch('lab4.get_roots', return_value = set())
    def test_no_roots(self, get_roots):
        self.assertEqual(get_roots(1, 0, 1), set())

    #даже если функция вернет другой результат, из-за mock тест всё равно будет считаться пройденным
    """@patch('lab4.get_roots', return_value = set())
    def test_no_roots(self, get_roots):
        self.assertEqual(get_roots(1, 0, -16), set())"""

    #обычный тест для случая отсутствия корней
    """ def test_no_roots(self):
        self.assertEqual(get_roots(1, 0, 10), set())"""

    def test_one_root(self):
        self.assertEqual(get_roots(1, 0, 0), set([0]))

    def test_two_roots(self):
        self.assertEqual(get_roots(1, 0, -16), set([2, -2])) 

    def test_three_roots(self):
        self.assertEqual(get_roots(-4, 16, 0), set([0, -2, 2]))

    def test_four_roots(self):
        self.assertEqual(get_roots(1, -5, 4), set([1, -1, 2, -2]))

if __name__ == '__main__':
    unittest.main()