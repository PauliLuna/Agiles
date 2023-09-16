import random

palabrasAdivinar = ["giacomo","fideos", "ravioles"]

class Ahorcado():

    def __init__(self):
        self.vidas = 7
        self.palabraAdivinar = random.choice(palabrasAdivinar)
        self.letrasAdivinadas = []
        self.letrasIncorrectas = []
        self.palabrasIncorrectas = []
    
    def cantidad(self,palabra):
        return len(palabra)

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
            self.vidas =  self.vidas-1
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
    
    def verificar_repeticion_letra(self,letra):
        if letra in self.letrasIncorrectas or letra in self.letrasAdivinadas:
            return True
        else:
            return False