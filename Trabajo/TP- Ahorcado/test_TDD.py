import unittest
from ahorcado import Ahorcado

# Creo una instancia del Ahorcado
juego = Ahorcado()
juego.palabraAdivinar = "giacomo"
juego.palabrasIncorrectas.append("tirabuzones")

class Vidas(unittest.TestCase):
    def test_pierdo_primer_vida(self):
            juego.vidas=7
            esperado = 6 
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)
    
    def test_pierdo_segunda_vida(self):
            juego.vidas=6
            esperado = 5
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

class ArriesgarPalabraTest(unittest.TestCase):

    def test_adivino_palabra(self):
        esperado = True
        actual = juego.arriesgoPalabra("giacomo")
        print(actual)
        self.assertEqual(actual, esperado)

    def test_pierdo_palabra(self):
        esperado = False 
        actual = juego.arriesgoPalabra("nogiacomo")
        self.assertEqual(actual, esperado)

class RepetirPalabras(unittest.TestCase):
     def test_no_repetir_palabras(self):
        esperado = False 
        actual = juego.verificar_repeticion("giacomo2")
        self.assertEqual(actual, esperado)

     def test_repetir_palabras(self):
        esperado = True 
        actual = juego.verificar_repeticion("tirabuzones")
        self.assertEqual(actual, esperado)


# class RegistrarPalabra(unittest.TestCase):
#      def test_agrego(self):
#           esperado = 
#           actual = agrego


class CantidadLetras(unittest.TestCase):
     def test_cantidad(self):
          esperado = 7
          actual = juego.cantidad("giacomo")
          self.assertEqual(actual, esperado)



if __name__ == '__main__':
    unittest.main()