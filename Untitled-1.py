def jugar_adivinador():
    low, high = 1, 100
    intentos = 0
    print("piensa en un numero entre 1 y 100, y yo intentare adivinarlo.")
    while low <= high:
        guess = (low + high) // 2
        intentos += 1
        respuesta = input(f"¿Tu número es {guess}? (responde 'mayor', 'menor' o 'correcto'): ").strip().lower()
        if respuesta == 'correcto':
            print(f"¡He adivinado tu número {guess} en {intentos} intentos!")
            return
        elif respuesta == 'mayor':
            low = guess + 1
        elif respuesta == 'menor':
            high = guess - 1
        else:
            print("Respuesta no válida. Por favor, responde 'mayor', 'menor' o 'correcto'.")
            intentos -= 1  
            print("no he podido adivinar el numero.")
if __name__ == "__main__":    jugar_adivinador()
