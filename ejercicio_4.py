# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
# def generar_invitados():

#Definimos la función que solicite el nombre de tres invitados

def generar_invitados(cant_invitados):   #El argumento de la función es la cantidad de invitados
    lista = []                  #Creo la lista vacía que contendra los nombres de los invitados
    for i in range(cant_invitados):      #Creo un bucle para que se repita la solicitud del nombre del invitado segun la cant de invitados
        nombre = str(input("Ingrese el nombre del invitado: "))     #Solicito el nombre del invitado
        lista.append(nombre)    #Agrego a cada nombre ingresado a la lista creada
    return lista                #Retorno la variable lista con  los nombres agregados

# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Crear la función "generar_invitados"

    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:

    # lista_invitados = generar_invitados()

    lista_invitados = generar_invitados(3)

    # Imprimir en pantalla "lista_invitados":

    print("La lista de invitados es:")
    print(lista_invitados)

    print("terminamos")
