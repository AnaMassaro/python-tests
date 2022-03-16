from calculator import function_sum

""" print(function_sum(10, 20))
print(function_sum(-10, 20))
print(function_sum(1.5, 2.5)) """

try:
  print(function_sum('15',15))
except AssertionError as e:
  print(f'Invalid account: {e}')

print('Invalid account', function_sum(25, 25))