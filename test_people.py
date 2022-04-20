"""
class People:
  __init__
    name str
    last_name str
    data bool (Initial as false)

  API:
    get_all_data -> method
      OK
      404

      (get_data is true if get data successfully)
"""
import unittest
from unittest.mock import patch
from People import People

class TestPeople(unittest.TestCase):
  # setUp - Esse método é executado sempre antes de cada teste
  def setUp(self):
    self.p1 = People('Ana', 'Julia')
    self.p2 = People('Maria', 'Miranda')

  def test_people_attr_name_correct_value(self):
    self.assertEqual(self.p1.name, 'Ana')
    self.assertEqual(self.p2.name, 'Maria')

  def test_people_attr_name_is_str(self):
    self.assertIsInstance(self.p1.name, str)
    self.assertIsInstance(self.p2.name, str)

  def test_people_attr_last_name_correct_value(self):
    self.assertEqual(self.p1.last_name, 'Julia')
    self.assertEqual(self.p2.last_name, 'Miranda')

  def test_people_attr_last_name_is_str(self):
    self.assertIsInstance(self.p1.last_name, str)
    self.assertIsInstance(self.p2.last_name, str)

  def test_people_attr_data_initial_false(self):
    self.assertFalse(self.p1.data)
    self.assertFalse(self.p2.data)

  def test_get_all_data_OK(self):
    with patch('requests.get') as fake_request:
      fake_request.return_value.ok = True

      self.assertEqual(self.p1.get_all_data(), 'CONNECTED')
      self.assertTrue(self.p1.data)

      self.assertEqual(self.p2.get_all_data(), 'CONNECTED')
      self.assertTrue(self.p2.data)

  def test_get_all_data_FAILURE_404(self):
    with patch('requests.get') as fake_request:
      fake_request.return_value.ok = False

      self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
      self.assertFalse(self.p1.data)

      self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
      self.assertFalse(self.p2.data)

  def test_get_all_data_sequential_success_and_failure(self):
    with patch('requests.get') as fake_request:
      fake_request.return_value.ok = True

      self.assertEqual(self.p1.get_all_data(), 'CONNECTED')
      self.assertTrue(self.p1.data)

      self.assertEqual(self.p2.get_all_data(), 'CONNECTED')
      self.assertTrue(self.p2.data)

      fake_request.return_value.ok = False

      self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
      self.assertFalse(self.p1.data)

      self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
      self.assertFalse(self.p2.data)

if __name__ == '__main__':
  unittest.main(verbosity=2)


