import random
import re
import os

palabrasAdivinar = ["giacomo","fideos", "ravioles"]
abecedario = list("abcdefghijklmnopqrstuvwxyz")


class Ahorcado():
    def __init__(self):
        self.vidas = 7
        self.palabraAdivinar = random.choice(palabrasAdivinar)
        self.letrasAdivinadas = []
        self.letrasIncorrectas = []
        self.palabrasIncorrectas = []
    
    def obtener_nombre(self):
        jugador = input("Bienvenido al juego ahorcado, ¿Cuál es tu nombre? ")
        return jugador
    
    def menu_opcion(self):
        while True:
            print("Opciones de juego:")
            print("1- Nivel 1 (Fácil)")
            print("2- Nivel 2 (Medio)")
            print("3- Nivel 3 (Difícil)")
            opcion = input("Ingrese opción: ")

            if opcion in ["1", "2", "3"]:
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Opción incorrecta. Por favor, ingrese una opción válida (1, 2 o 3).")
        return opcion        

   # def cantidad(self,palabra):
     #   return len(palabra)
    
    def juega(self,input):
       if self.validaEntrada(input):
            if len(input) == 1:
                self.arriesgoLetra(input)
            else:
                self.arriesgoPalabra(input)

    def arriesgoPalabra(self, word):
        repite = self.verificar_repeticion(word)
        if not repite:
            if word == self.palabraAdivinar:
                return True
            else:
                self.descontar_vida()
                self.palabrasIncorrectas.append(word)
                return False
        
    def descontar_vida(self):
        if not self.vidas==0:
            self.vidas -=1
            return self.vidas

    def verificar_repeticion(self,A):
        if A in self.palabrasIncorrectas:
            return True
        else:
            return False
    
    def arriesgoLetra(self, letra):
        repite = self.verificar_repeticion_letra(letra)
        if not repite:
            if letra in self.palabraAdivinar:
                self.letrasAdivinadas.append(letra)
                return True
            else:
                self.descontar_vida()
                self.letrasIncorrectas.append(letra)
                return False

    def validaEntrada(self,input):
    # Usamos una expresión regular para verificar si la cadena contiene solo letras
        patron = r'^[a-zA-Z]+$'
        return bool(re.match(patron,input))
    
    def verificar_repeticion_letra(self,letra):
        if letra in self.letrasIncorrectas or letra in self.letrasAdivinadas:
            return True
        else:
            return False
        
    def imprimo_palabra(self):
        palabra_mostrar = ""
        for letra in self.palabraAdivinar:
            if letra in self.letrasAdivinadas:
                palabra_mostrar += letra+" "
            else:
                palabra_mostrar += "_ "
        return palabra_mostrar

# JUEGO
if __name__ == '__main__':
    juegoActual = Ahorcado()
    juegoActual.jugador = juegoActual.obtener_nombre()
    print("Bienvenido {}. Vamos a jugar!".format(juegoActual.jugador))
    juegoActual.menu_opcion()
    print(juegoActual.imprimo_palabra())


## NOTAS:
# En Python, cuando importas un módulo, todas las declaraciones en ese módulo se ejecutan una vez,
#  incluyendo las declaraciones que no están dentro de funciones o clases.
#  En este caso, la línea juegoActual.obtener_nombre() se ejecuta inmediatamente cuando se importa el módulo
#  ahorcado.py, antes de que se ejecuten las pruebas en el archivo test_TDD.py.
# Para solucionar esto, puedes mover la línea juegoActual.obtener_nombre()
#  dentro de una función o un bloque if __name__ == '__main__':
