palabrasAdivinar = "giacomo"

class Ahorcado():

    def __init__(self):
        self.vidas = 7
        self.palabraAdivinar = palabrasAdivinar
        self.letrasAdivinadas = []
        self.letrasIncorrectas = []
        self.palabrasIncorrectas = []
    
    def vidas_Actuales(self):
        return self.vidas

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

    def cantidad(self,palabra):
        return len(palabra)