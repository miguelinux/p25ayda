

def seleccion(lista):
    for i in range(0, len(lista) - 1):
        min = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[min]:
                min = j

        lista[i], lista[min] = lista[min], lista[i]


nums = [98, 34, 1, 3, 31, 29, 22, 100, 14]

print(f"nums antes de ordenar: {nums}");

seleccion(nums)

print(f"nums despues de ordenar {nums}")