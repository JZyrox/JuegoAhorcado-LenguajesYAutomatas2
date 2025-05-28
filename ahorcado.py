import random

def dibujar_ahorcado(intentos):
    """Dibuja el estado del ahorcado según los intentos fallidos"""
    etapas = [r"""
          +---+
          |   |
              |
              |
              |
              |
        =========
        """, r"""
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """, r"""
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """, r"""
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """, r"""
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """, r"""
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        """, r"""
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        """]
    print(etapas[intentos])

def obtener_palabra():
    """Selecciona una palabra aleatoria de la lista"""
    palabras = ["PYTHON", "PROGRAMACION", "AHORCADO", "COMPUTADORA", 
               "ALGORITMO", "VARIABLE", "FUNCION", "DESARROLLO"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    """Muestra la palabra con las letras adivinadas"""
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso

def jugar():
    """Función principal del juego"""
    palabra = obtener_palabra()
    letras_adivinadas = set()
    letras_intentadas = set()
    intentos_fallidos = 0
    max_intentos = 6
    
    print("\n¡Bienvenido al juego del ahorcado!")
    print(f"Adivina la palabra. Tienes {max_intentos} intentos.")
    
    while True:
        # Mostrar estado actual del juego
        dibujar_ahorcado(intentos_fallidos)
        print("\n" + mostrar_progreso(palabra, letras_adivinadas))
        
        if letras_intentadas:
            print(f"\nLetras intentadas: {' '.join(sorted(letras_intentadas))}")
        
        # Verificar si ganó
        if all(letra in letras_adivinadas for letra in palabra):
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            break
            
        # Verificar si perdió
        if intentos_fallidos >= max_intentos:
            print(f"\n¡Oh no! Has perdido. La palabra era: {palabra}")
            break
            
        # Obtener entrada del usuario
        while True:
            letra = input("\nIngresa una letra: ").upper()
            if len(letra) != 1:
                print("Por favor ingresa exactamente una letra.")
            elif not letra.isalpha():
                print("Por favor ingresa una letra válida (A-Z).")
            elif letra in letras_intentadas:
                print("Ya has intentado esa letra. Prueba con otra.")
            else:
                break
        
        letras_intentadas.add(letra)
        
        # Verificar si la letra está en la palabra
        if letra in palabra:
            letras_adivinadas.add(letra)
            print(f"¡Correcto! La letra '{letra}' está en la palabra.")
        else:
            intentos_fallidos += 1
            print(f"Incorrecto. La letra '{letra}' no está en la palabra.")
            print(f"Te quedan {max_intentos - intentos_fallidos} intentos.")
    
    # Preguntar si quiere jugar de nuevo
    while True:
        opcion = input("\n¿Quieres jugar de nuevo? (S/N): ").upper()
        if opcion in ['S', 'N']:
            break
        print("Por favor ingresa 'S' para sí o 'N' para no.")
    
    if opcion == 'S':
        jugar()
    else:
        print("\n¡Gracias por jugar!")

# Iniciar el juego
if __name__ == "__main__":
    jugar()