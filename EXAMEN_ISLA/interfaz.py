def mostrar_menu_principal():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")

def mostrar_instrucciones():
    print("\n=== INSTRUCCIONES ===")
    print("1. El objetivo es encontrar la llave (L) en la isla de 6x6")
    print("2. Cada movimiento consume una acción")
    print("3. Objetos:")
    print("   - Roca (R): No tiene efecto")
    print("   - Fruta (F): +1 vida")
    print("   - Serpiente (S)/Escorpión (E): -1 vida")
    print("   - Cocodrilo (C): Pierdes inmediatamente")
    print("4. Comienzas con 5 vidas")
    print("5. ¡Buena suerte!\n")

def obtener_coordenadas():
    try:
        x = int(input("Ingresa la coordenada X (0-5): "))
        y = int(input("Ingresa la coordenada Y (0-5): "))
        return x, y
    except ValueError:
        print("Por favor ingresa números válidos.")
        return None, None