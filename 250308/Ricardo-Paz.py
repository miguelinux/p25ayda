import math


def perimetro_poligono(lados, longitud):
    return lados * longitud


def area_poligono_regular(lados, longitud):
    angulo = math.pi / lados
    apotema = longitud / (2 * math.tan(angulo))
    return (perimetro_poligono(lados, longitud) * apotema) / 2


def area_poligono_irregular(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Siguiente vértice (circular)
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


def main():
    tipo = input("El polígono es regular o irregular? (r/i): ").strip().lower()

    if tipo == "r":
        lados = int(input("Número de lados: "))
        longitud = float(input("Longitud de cada lado: "))
        print(f"Perímetro: {perimetro_poligono(lados, longitud):.2f}")
        print(f"Área: {area_poligono_regular(lados, longitud):.2f}")

    elif tipo == "i":
        n = int(input("Número de vértices: "))
        vertices = []
        for i in range(n):
            x, y = map(float, input(f"Coordenadas del vértice {i + 1} (x y): ").split())
            vertices.append((x, y))
        print(f"Área del polígono irregular: {area_poligono_irregular(vertices):.2f}")

    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()
