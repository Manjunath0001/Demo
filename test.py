import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestFactorial(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()

