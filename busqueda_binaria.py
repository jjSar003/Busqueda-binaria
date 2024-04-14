def busqueda(lista, num, inicio, fin):
    """Esta funcion hace una busqueda binaria mediante la recursividad.
    Si el valor no esta dentro de la lista retorna -1, de lo contrario retorna
    la posicion del numero."""
    if inicio > fin:
        return -1
    
    medio = inicio + (fin - inicio) // 2
    if lista[medio] == num:
        return medio
    elif lista[medio] < num:
        inicio = medio + 1
        return busqueda(lista, num, inicio, fin)
    else:
        fin = medio - 1
        return busqueda(lista, num, inicio, fin)

#Creacion de la lista que contiene los numeros para la busqueda binaria
numeros = [2, 4, 6, 8, 20, 22, 28, 30, 36, 38, 54, 58, 64, 76, 82, 84, 86, 92, 94, 100]

#Se le resta 1 a la longitud de la lista para poder utilizar los indices 
fin = len(numeros) - 1
#Se designa el numero a buscar
num_objetivo = 2
#Se llama a la funcion que realiza la busqueda binaria y se almacena el retorno
resultado = busqueda(numeros, num_objetivo, 0, fin)
#Se muestra por pantalla el resultado de la busqueda 
if resultado != -1:
    print(f"El numero esta en la posicion {resultado}")
else:
    print("El numero no esta en la lista")