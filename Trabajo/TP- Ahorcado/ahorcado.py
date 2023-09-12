palabras = ["tirabuzones"]
palabrasAdivinar = "giacomo"


class Ahorcado():

    def __init__(self, palabrasAdivinar):
        self.vidas = 7
        self.palabraAdivinar = palabrasAdivinar

    def arriesgoPalabra(A):
        repite = Ahorcado.verificar_repeticion(A)
        if not repite:
            if A == Ahorcado.palabraAdivinar:
                return True
            else:
                Ahorcado.descontar_vida()
                palabras.append(A)
                return False
        
    def descontar_vida():
        if Ahorcado.vidas_Actuales()==0:
            return 0
        else:
            Ahorcado.vidas =  Ahorcado.vidas_Actuales()-1
            return Ahorcado.vidas

    def vidas_Actuales():
        return Ahorcado.vidas

    def verificar_repeticion(A):
        if A in palabras:
            return True
        else:
            return False 

    def cantidad(palabra):
        return len(palabra)