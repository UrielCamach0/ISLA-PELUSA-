class Jugador:
    def __init__(self):
        self.vidas = 5
        self.llave_encontrada = False
        self.celdas_exploradas = set()
    
    def esta_vivo(self):
        return self.vidas > 0 and not self.llave_encontrada
    
    def estado(self):
        return f"Vidas: {self.vidas} | {'Llave encontrada' if self.llave_encontrada else 'Buscando llave...'}"