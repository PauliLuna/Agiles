import unittest

def suma(a, b):
    return a + b

class SumaTest(unittest.TestCase):
    def test_suma_ceros(self):
        esperado = 0
        actual = suma(0,0)
        self.assertEqual(actual, esperado)


    def test_suma_enteros(self):
        esperado = 3
        actual = suma(1, 2)
        self.assertEqual(actual, esperado)

    def test_suma_negativos(self):
        esperado = -3
        actual = suma(-1, -2)
        self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()