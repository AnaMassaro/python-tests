def function_sum(x, y):
  """Sum x and y
  
  >>> function_sum(10, 20)
  30

  >>> function_sum(-10, 20)
  10

  >>> function_sum('10', 20)
  Traceback (most recent call last):
  ...
  AssertionError: y must be int or float
  """
  assert isinstance(x, (int, float)), 'x must be int or float'
  assert isinstance(y, (int, float)), 'y must be int or float'
  return x + y

def function_subtract(x, y):
  """Subtract x and y

  >>> function_subtract('10' ,5)
  Traceback (most recent call last):
  ...
  AssertionError: y must be int or float
  """
  assert isinstance(x, (int, float)), 'x must be int or float'
  assert isinstance(y, (int, float)), 'y must be int or float'

  return x - y


if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)