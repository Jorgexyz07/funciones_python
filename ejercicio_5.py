# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada

#Copiamos y pegamos la función creada en ejercicio_4 (generar_invitados)

def generar_invitados(cant_invitados):   #El argumento de la función es la cantidad de invitados
    lista = []                  #Creo la lista vacía que contendra los nombres de los invitados
    for i in range(cant_invitados):      #Creo un bucle para que se repita la solicitud del nombre del invitado segun la cant de invitados
        nombre = str(input("Ingrese el nombre del invitado: "))     #Solicito el nombre del invitado
        lista.append(nombre)    #Agrego a cada nombre ingresado a la lista creada
    return lista                #Retorno la variable lista con  los nombres agregados

# --------------------------------

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada

#Copiamos y pegamos la función del ejercicio_3

def ordenar(lista):
    ordenada = sorted(lista)    #Creo la variable que me guardará la lista ordenada
    return ordenada             #Retorno la variable ordenada con la lista ordenada

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    # lista_invitados = generar_invitados()

    #Genero la lista de invitados con la función generar_invitados

    lista_invitados = generar_invitados(3)

    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    # lista_invidatos_ordenada = ordenar(lista_invitados)

    #Ordeno la lista generada con la función ordenar

    lista_invitados_ordenada = ordenar(lista_invitados)

    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("La lista de invitados ordenada es: ")
    print(lista_invitados_ordenada)     

    print("terminamos")
