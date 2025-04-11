def es_palindromo(palabra: str) -> bool:
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]


# Ejemplos de uso
palabras = ["reconocer", "oso", "Python", "anilina", "radar", "Hola"]

for palabra in palabras:
    if es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")
