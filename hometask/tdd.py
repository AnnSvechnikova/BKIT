from state_bot import get_resp
import unittest

class TddTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_resp("000"), "экскурсия в музей")

    def test2(self):
        self.assertEqual(get_resp("011"), "батутный центр")


if __name__ == '__main__':
    unittest.main()