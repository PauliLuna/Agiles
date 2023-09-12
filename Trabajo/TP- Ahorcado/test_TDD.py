import unittest
from ahorcado import Ahorcado

juego = Ahorcado("giacomo")

class ArriesgarPalabraTest(unittest.TestCase):
    

    def test_adivino_palabra(self):
        esperado = True
        actual = juego.arriesgoPalabra("giacomo")
        self.assertEqual(actual, esperado)

    def test_pierdo_palabra(self):
        esperado = False 
        actual = juego.arriesgoPalabra("nogiacomo")
        self.assertEqual(actual, esperado)


class Vidas(unittest.TestCase):
    def test_pierdo_primer_vida(self):
            esperado = 6 
            actual = juego.vidas_Actuales()
            self.assertEqual(actual, esperado)
    
    def test_pierdo_segunda_vida(self):
            esperado = 5
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

class RepetirPalabras(unittest.TestCase):
     def test_no_repetir_palabras(self):
        esperado = False 
        actual = verificar_repeticion("giacomo")
        self.assertEqual(actual, esperado)

     def test_repetir_palabras(self):
        esperado = True 
        actual = verificar_repeticion("tirabuzones")
        self.assertEqual(actual, esperado)

# class RegistrarPalabra(unittest.TestCase):
#      def test_agrego(self):
#           esperado = 
#           actual = agrego


class CantidadLetras(unittest.TestCase):
     def test_cantidad(self):
          esperado = 7
          actual = cantidad("giacomo")
          self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()