# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.2

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random

'''
Enunciado:
Alumno: Crear la función "contar"

Utilice la función "lista_aleatoria" creada antes 
para generar una lista de 5 números en
un rango de 1 a 6 inclusive

lista_numeros = lista_aleatoria(inicio, fin, cantidad)

Generar una una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista (también pasada por parámetro)

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior

#Función lista_aleatoria creada en profundizacion_1.py

def lista_aleatoria(inicio = 1, fin = 6, cantidad = 5):     #Defino los parámetros inicio, fin y cantidad
    lista = []                                  #Creo la lista vacía donde se guardarán los números aleatorios
    for i in range(cantidad):                   #Creo el bucle para que se repita la cantidad de num aleatorios
        num = random.randint(inicio,fin)        #Creo el número aleatorio
        lista.append(num)                       #Agrego el número aleatorio a la lista
    return lista                                #Retorno la variable lista con sus elementos agregados

# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar

def contar (lista, num):        #Defino los parámetros a pasar por la función: la lista y el num que deseo 
                                #saber cuántas veces se repite
    num_repetido = lista.count(num)     #Creo la variable que almacenara la cantidad de veces que se repite
                                        #el número       
    return num_repetido                 #Retorno la variable num repetido


def contar_2(lista, num):       #Defino otra función, que no utilice el método nativo .count
    rep = 0
    for x in lista:
        if x == 3:
            rep += 1
        else:
            pass
    return rep

# lista_1 = lista_aleatoria()       #Pruebo si funciona
# print(lista_1)
# opcion_2 = contar(lista_1,3)
# print(opcion_2)                   #Funciona el método opcional pero, como se ve, gasto muchas más líneas

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive

    # lista_numeros = lista_aleatoria(...)

    #Defino la variable que me almacenará la lista de números aleatorios que voy a generar

    lista_numeros = lista_aleatoria()

    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":

    # print(lista_numeros)

    print("La lista aleatoria de números generada es:")
    print(lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    # cantidad_tres = contar(lista_numeros, 3)

    #Defino la variable que almacenará la cantidad de veces que se repite el número 3

    cantidad_tres = contar(lista_numeros, 3)
    # print(cantidad_tres)

    print("El número 3 se repite", cantidad_tres, "veces en la lista de números aleatoria generada")
    print("terminamos")
