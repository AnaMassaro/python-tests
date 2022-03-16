import unittest
from calculator import function_sum

class TestCalculator(unittest.TestCase):
  def test_sum_5_and_5_returns_10(self):
    self.assertEqual(function_sum(5, 5), 10)
   
  def test_sum_negative_and_5_returns_0(self):
    self.assertEqual(function_sum(-5, 5), 0)

  def test_sum_multiple_entries(self):
    x_y_outputs = (
      (10, 10, 20),
      (5, 5, 10),
      (1.5, 1.5, 3.0),
      (-5, 5, 0),
      (100, 100, 200),
    )

    for x_y_output in x_y_outputs:
      with self.subTest(x_y_output=x_y_output):
        x, y, output = x_y_output
        self.assertEqual(function_sum(x, y), output)

  def test_x_is_not_int_or_float_returns_assertion(self):
    with self.assertRaises(AssertionError):
      function_sum('a', 11)

  def test_y_is_not_int_or_float_returns_assertion(self):
    with self.assertRaises(AssertionError):
      function_sum(11, '11')
      
unittest.main(verbosity=2)