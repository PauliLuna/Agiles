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
        self.gano = 0
    
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
                if self.arriesgoPalabra(input):
                    return True
                else:
                    return False

    def validaEntrada(self,input):
    # Usamos una expresión regular para verificar si la cadena contiene solo letras
        patron = r'^[a-zA-Z]+$'
        return bool(re.match(patron,input))
    
    def arriesgoLetra(self, letra):
        repite = self.verificar_repeticion_letra(letra)
        if not repite:
            if letra in self.palabraAdivinar:
                self.letrasAdivinadas.append(letra)
                print("Letra correcta!")
                if "_" in self.imprimo_palabra():
                    self.gano = 0
                else:
                    self.gano = 1
                return True
            else:
                self.descontar_vida()
                self.letrasIncorrectas.append(letra)
                print("Letra incorrecta. Perdiste 1 vida")
                return False

    def verificar_repeticion_letra(self,letra):
        if letra in self.letrasIncorrectas or letra in self.letrasAdivinadas:
            print("La letra {} ya fué ingresada!".format(letra))
            return True
        else:
            return False

    def arriesgoPalabra(self, word):
        repite = self.verificar_repeticion(word)
        if not repite:
            if word == self.palabraAdivinar:
                self.gano= 1
                return True
            else:
                self.descontar_vida()
                self.gano= 0
                self.palabrasIncorrectas.append(word)
                print("La palabra ingresada es incorrecta! Perdiste 1 vida")
                return False

    def descontar_vida(self):
        if not self.vidas==0:
            self.vidas -=1
            return self.vidas
        else:
            return 0

    def verificar_repeticion(self,A):
        if A in self.palabrasIncorrectas:
            print("La palabra {} ya fue ingresada!".format(A))
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
    
    def imprimo_palabra_ganadora(self, palabra):
        palabra_mostrar = ""
        for letra in palabra:
            palabra_mostrar += letra+" "
        return palabra_mostrar

# JUEGO
if __name__ == '__main__':
    while True:
        juegoActual = Ahorcado()
        juegoActual.jugador = juegoActual.obtener_nombre()
        print("¡Bienvenido {}! --> Vamos a jugar!".format(juegoActual.jugador))
        op = juegoActual.menu_opcion()
        if op == "1":
            print("-----Bienvenido al nivel FACIL-----")
            print ("           Mucha suerte!")
            print("Vidas: {}".format(juegoActual.vidas))
            print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
            print(juegoActual.imprimo_palabra())
            print("")
            while juegoActual.vidas > 0 and juegoActual.gano !=1:
                ingreso = input("Ingresa una letra o palabra: ").lower()
                juegoActual.juega(ingreso)
                print("Vidas: {}".format(juegoActual.vidas))
                print("")
                print(juegoActual.imprimo_palabra())

            if juegoActual.gano==1:
                print("La palabra ingresada es correcta!")
                print(juegoActual.imprimo_palabra_ganadora(ingreso))
                print(" ")
                print("GANASTE!")
                print(" ")

            else:
                print("Agotaste todas las vidas!")
                print(" ")
                print("---GAME OVER----")
                print(" ")
            print("")
            
        if op == "2":
            print("-----Bienvenido al nivel MEDIO-----")
            print ("           Mucha suerte!")
            print("Vidas: {}".format(juegoActual.vidas))
            print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
            print(juegoActual.imprimo_palabra())
            print("")
            while juegoActual.vidas > 0 and juegoActual.gano !=1:
                ingreso = input("Ingresa una letra o palabra: ").lower()
                juegoActual.juega(ingreso)
                print("Vidas: {}".format(juegoActual.vidas))
                print("")
                print(juegoActual.imprimo_palabra())

            if juegoActual.gano==1:
                print("La palabra ingresada es correcta!")
                print(juegoActual.imprimo_palabra_ganadora(ingreso))
                print(" ")
                print("GANASTE!")
                print(" ")

            else:
                print("Agotaste todas las vidas!")
            print("")


        if op == "3":
            print("-----Bienvenido al nivel DIFICIL-----")
            print ("           Mucha suerte!")
            print("Vidas: {}".format(juegoActual.vidas))
            print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
            print(juegoActual.imprimo_palabra())
            print("")
            while juegoActual.vidas > 0 and juegoActual.gano !=1:
                ingreso = input("Ingresa una letra o palabra: ").lower()
                juegoActual.juega(ingreso)
                print("Vidas: {}".format(juegoActual.vidas))
                print("")
                print(juegoActual.imprimo_palabra())

            if juegoActual.gano==1:
                print("La palabra ingresada es correcta!")
                print(juegoActual.imprimo_palabra_ganadora(ingreso))
                print(" ")
                print("GANASTE!")
                print(" ")

            else:
                print("Agotaste todas las vidas!")
            print("")
        






## NOTAS:
# En Python, cuando importas un módulo, todas las declaraciones en ese módulo se ejecutan una vez,
#  incluyendo las declaraciones que no están dentro de funciones o clases.
#  En este caso, la línea juegoActual.obtener_nombre() se ejecuta inmediatamente cuando se importa el módulo
#  ahorcado.py, antes de que se ejecuten las pruebas en el archivo test_TDD.py.
# Para solucionar esto, puedes mover la línea juegoActual.obtener_nombre()
#  dentro de una función o un bloque if __name__ == '__main__':
