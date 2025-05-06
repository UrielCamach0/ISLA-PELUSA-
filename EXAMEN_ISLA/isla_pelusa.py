import random
from jugador import Jugador
from objetos import Roca, Fruta, Serpiente, Escorpion, Cocodrilo, Llave

class JuegoIsla:
    TAMANO_ISLA = 6
    
    def __init__(self):
        self.resetear_juego()
    
    def resetear_juego(self):
        self.jugador = Jugador()
        self.crear_isla()
        self.colocar_objetos()
    
    def crear_isla(self):
        self.isla = [[None for _ in range(self.TAMANO_ISLA)] for _ in range(self.TAMANO_ISLA)]
    
    def colocar_objetos(self):
        # Colocar objetos obligatorios
        self.colocar_objeto_unico(Cocodrilo())
        self.colocar_objeto_unico(Llave())
        
        # Colocar cantidad mínima de cada objeto
        for _ in range(3):
            self.colocar_objeto(Fruta())
            self.colocar_objeto(Roca())
        
        for _ in range(2):
            self.colocar_objeto(Serpiente())
            self.colocar_objeto(Escorpion())
        
        # Llenar el resto con objetos aleatorios
        objetos_extra = [Fruta(), Roca(), Serpiente(), Escorpion()]
        celdas_vacias = sum(1 for fila in self.isla for celda in fila if celda is None)
        
        for _ in range(celdas_vacias):
            self.colocar_objeto(random.choice(objetos_extra))
    
    def colocar_objeto_unico(self, objeto):
        while True:
            x, y = random.randint(0, self.TAMANO_ISLA-1), random.randint(0, self.TAMANO_ISLA-1)
            if self.isla[x][y] is None:
                self.isla[x][y] = objeto
                break
    
    def colocar_objeto(self, objeto):
        celdas_vacias = [(i, j) for i in range(self.TAMANO_ISLA) 
                         for j in range(self.TAMANO_ISLA) if self.isla[i][j] is None]
        if celdas_vacias:
            x, y = random.choice(celdas_vacias)
            self.isla[x][y] = objeto
    
    def mostrar_isla(self, mostrar_todo=False):
        print("\nMapa de la Isla:")
        print("   " + " ".join(str(i) for i in range(self.TAMANO_ISLA)))
        for i in range(self.TAMANO_ISLA):
            print(f"{i} |", end=" ")
            for j in range(self.TAMANO_ISLA):
                if mostrar_todo or (i, j) in self.jugador.celdas_exploradas:
                    print(self.isla[i][j], end=" ")
                else:
                    print("?", end=" ")
            print()
        print()
    
    def explorar_celda(self, x, y):
        if not (0 <= x < self.TAMANO_ISLA and 0 <= y < self.TAMANO_ISLA):
            return "Coordenadas inválidas. Intenta de nuevo."
        
        if (x, y) in self.jugador.celdas_exploradas:
            return "Ya exploraste esta celda. Elige otra."
        
        self.jugador.celdas_exploradas.add((x, y))
        objeto = self.isla[x][y]
        mensaje = objeto.afectar_jugador(self.jugador)
        
        if isinstance(objeto, Cocodrilo) or isinstance(objeto, Llave):
            self.mostrar_isla(mostrar_todo=True)
        
        return mensaje
    
    def jugar(self):
        self.mostrar_bienvenida()
        
        while self.jugador.esta_vivo() and not self.jugador.llave_encontrada:
            self.mostrar_isla()
            print(self.jugador.estado())
            
            try:
                x = int(input("Ingresa la coordenada X (0-5): "))
                y = int(input("Ingresa la coordenada Y (0-5): "))
                print(self.explorar_celda(x, y))
            except ValueError:
                print("Por favor ingresa números válidos.")
            
            if not self.jugador.esta_vivo():
                print("\n¡Has perdido todas tus vidas! Game Over.")
            elif self.jugador.llave_encontrada:
                print("\n¡Felicidades! Has encontrado la llave y escapado de la isla.")
        
        self.preguntar_reinicio()
    
    def mostrar_bienvenida(self):
        print("¡Bienvenido a la Isla Desierta!")
        print("Encuentra la llave para escapar, pero cuidado con los peligros.")
        print("Objetos: R=Roca, F=Fruta, S=Serpiente, E=Escorpión, C=Cocodrilo, L=Llave\n")
    
    def preguntar_reinicio(self):
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo == 's':
            self.resetear_juego()
            self.jugar()