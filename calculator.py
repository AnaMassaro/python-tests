def function_sum(x, y):
  """Soma x e y
  
  >>> soma(10, 20)
  30

  >>> soma(-10, 20)
  10

  >>> soma('10', 20)
  Traceback (most recent call last):
  ...
  AssertionError: y must be int or float
  """
  assert isinstance(x, (int, float)), 'x must be int or float'
  assert isinstance(y, (int, float)), 'y must be int or float'
  return x + y

def function_subtract(x, y):
  """Subtrai x e y

  >>> subtrai('10' ,5)
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