import unittest
import re

sep= '\n |,'

def suma(string):
    if string == '':
        return 0
    else:
        nros = re.split(sep, string)
        return sum(int(x) for x in nros)
    

class SumaTest(unittest.TestCase):
    def test_vacio(self):
        resultado = suma('')
        print(resultado)
        self.assertEqual(resultado,0)

    def test_2numerosEnter(self):
        resultado = suma("""2   
                         3""")
        self.assertEqual(resultado,5) #ponemos """ """ para hacer referencia al enter

    def test_3numerosComaEnter(self):
        resultado = suma("""1,5
                         6""")
        self.assertEqual(resultado,12)

    def test_4numerosComa(self):
        resultado = suma('7,5,2,1')
        self.assertEqual(resultado,15)

if __name__ == '__main__':
    unittest.main()
