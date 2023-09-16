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


class ArriesgoLetra(unittest.TestCase):
     def test_adivino_letra(self):
          esperado = True
          actual = juego.arriesgoLetra("a")
          self.assertEqual(actual, esperado)

     def test_pierdo_letra(self):
        esperado = False 
        actual = juego.arriesgoPalabra("x")
        self.assertEqual(actual, esperado)

class RepetirLetras(unittest.TestCase):
     def test_no_repetir_letra(self):
          juego.letrasAdivinadas = ["g", "a"]
          juego.letrasIncorrectas = ["w"]
          esperado = False
          actual = juego.verificar_repeticion_letra("z")
          self.assertEqual(actual, esperado)
    
     def test_repetir_letra_adivinada(self):
          juego.letrasAdivinadas = ["g", "a"]
          juego.letrasIncorrectas = ["w"]
          esperado = True
          actual = juego.verificar_repeticion_letra("a")
          self.assertEqual(actual, esperado)
    
     def test_repetir_letra_incorrecta(self):
          juego.letrasAdivinadas = ["g", "a"]
          juego.letrasIncorrectas = ["w"]
          esperado = True
          actual = juego.verificar_repeticion_letra("w")
          self.assertEqual(actual, esperado)
    

class CantidadLetras(unittest.TestCase):
     def test_cantidad(self):
          esperado = 7
          actual = juego.cantidad("giacomo")
          self.assertEqual(actual, esperado)
    
     def test_cantidad_2(self):
          esperado = 9
          actual = juego.cantidad("telefonos")
          self.assertEqual(actual, esperado)
    
class ImprimoPalabra(unittest.TestCase):
     def test_imprimo(self):
            juego.palabraAdivinar = "giacomo"
            juego.letrasAdivinadas = ["a", "o"]
            esperado = "_ _ a _ o _ o"
            actual = juego.imprimo_palabra()
            self.assertEqual(actual, esperado)
    

# Para correr los tests
if __name__ == '__main__':
    unittest.main()