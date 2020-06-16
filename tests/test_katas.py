import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(3, 4), 7)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 9), 45)

    def test_power(self):
        self.assertEqual(katas.power(3, 3), 27)

    def test_factorial(self):
        self.assertEqual(katas.factorial(4), 24)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(6), 5)


if __name__ == '__main__':
    unittest.main()
