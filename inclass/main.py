import unittest
from fib import*
from pytest import*
import coverage

class TestCase(unittest.TestCase):
  #tests on volume
  def test_case_1(self):
    self.assertEqual ((fib_fn(4)), 3)
  def test_case_2(self):
    self.assertEqual (print(fib_fn("h")),None)
  def test_case_3(self):
    self.assertEqual (factorial_fn(2), 2)

def test_fib():
  assert (fib_fn(2)) == 1



if __name__ == '__main__':unittest.main()
test_fib()
