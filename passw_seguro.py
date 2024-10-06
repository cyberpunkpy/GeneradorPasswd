import random
import string

def generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos):
    caracteres = ''
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de carácter."

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = int(input("¿Cuántos caracteres tendrá la contraseña? "))
    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    contrasena = generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos)
    print(f"Tu contraseña generada es: {contrasena}")

if __name__ == "__main__":
    main()
