from abc import ABC, abstractmethod

class ObjetoIsla(ABC):
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.explorado = False
    
    @abstractmethod
    def afectar_jugador(self, jugador):
        pass
    
    def __str__(self):
        return self.simbolo if self.explorado else "?"

class Roca(ObjetoIsla):
    def __init__(self):
        super().__init__("R")
    
    def afectar_jugador(self, jugador):
        self.explorado = True
        return "Has encontrado una roca. No pasa nada."

class Fruta(ObjetoIsla):
    def __init__(self):
        super().__init__("F")
    
    def afectar_jugador(self, jugador):
        self.explorado = True
        jugador.vidas += 1
        return "¡Encontraste una fruta! +1 vida."

class Serpiente(ObjetoIsla):
    def __init__(self):
        super().__init__("S")
    
    def afectar_jugador(self, jugador):
        self.explorado = True
        jugador.vidas -= 1
        return "¡Una serpiente te ha mordido! -1 vida."

class Escorpion(ObjetoIsla):
    def __init__(self):
        super().__init__("E")
    
    def afectar_jugador(self, jugador):
        self.explorado = True
        jugador.vidas -= 1
        return "¡Un escorpión te ha picado! -1 vida."

class Cocodrilo(ObjetoIsla):
    def __init__(self):
        super().__init__("C")
    
    def afectar_jugador(self, jugador):
        self.explorado = True
        jugador.vidas = 0
        return "¡Un cocodrilo te ha atacado! Game Over."

class Llave(ObjetoIsla):
    def __init__(self):
        super().__init__("L")
    
    def afectar_jugador(self, jugador):
        self.explorado = True
        jugador.llave_encontrada = True
        return "¡Encontraste la llave! Has ganado el juego."