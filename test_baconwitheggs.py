"""
TDD - Test driven development (Desenvolvimendo dirigido a tests)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
"""
import unittest
from baconwitheggs import bacon_with_eggs

class TestBaconComOvos(unittest.TestCase):
  def test_bacon_with_eggs_raise_assertion_error_if_not_receiving_int(self):
    with self.assertRaises(AssertionError):
      bacon_with_eggs('')

  def test_bacon_with_eggs_returns_bacon_with_eggs_if_input_is_multiple_of_3_and_5(self):
    inputs = (15, 30, 45, 60)
    output = 'Bacon with eggs'

    for input in inputs:
      with self.subTest(input=input, output=output):
        self.assertEqual(
          bacon_with_eggs(input), 
          output,
          msg=f'{input} did not return "{output}"'
        )
    
  def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
    inputs = (1, 2, 4, 7, 8)
    output = 'Go hungry'

    for input in inputs:
      with self.subTest(input=input, output=output):
        self.assertEqual(
          bacon_with_eggs(input), 
          output,
          msg=f'{input} did not return "{output}"'
        )

  def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
    inputs = (3, 6, 9, 12, 18, 21)
    output = 'Bacon'

    for input in inputs:
      with self.subTest(input=input, output=output):
        self.assertEqual(
          bacon_with_eggs(input), 
          output,
          msg=f'{input} did not return "{output}"'
        )

  def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
    inputs = (5, 10, 25, 35)
    output = 'Eggs'

    for input in inputs:
      with self.subTest(input=input, output=output):
        self.assertEqual(
          bacon_with_eggs(input), 
          output,
          msg=f'{input} did not return "{input}"'
        )

unittest.main(verbosity=2)