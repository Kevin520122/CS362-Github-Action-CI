import unittest
from calculator import add, subtract, multiply, divide


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(subtract(1, 1), 0)

    def test_multiply_1(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_divide_1(self):
        self.assertEqual(divide(18, 3), 6)


if __name__ == '__main__':
    unittest.main()
