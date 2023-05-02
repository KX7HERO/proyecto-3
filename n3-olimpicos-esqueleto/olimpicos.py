# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:54:09 2023

@author: josep
"""

def cargar_atletas(nombre_archivo):
    """Recibe el nombre de un archivo CSV con la información de los atletas
    y retorna una lista de diccionarios con los datos de cada atleta.

    Parámetros:
    nombre_archivo: una cadena con el nombre del archivo CSV.

    Retorno:
    una lista de diccionarios con las llaves: nombre, genero, edad, pais,
    anio, evento y medalla.
    """
    # Crear una lista vacía para almacenar los atletas
    lista_atletas = []
    # Abrir el archivo en modo lectura
    with open(nombre_archivo) as archivo:
        # Leer las líneas del archivo
        lineas = archivo.readlines()
        # Saltar la primera línea que contiene los nombres de las columnas
        lineas = lineas[1:]
        # Recorrer cada línea del archivo
        for linea in lineas:
            # Eliminar el salto de línea al final
            linea = linea.strip()
            # Separar los valores por comas
            valores = linea.split(",")
            # Crear un diccionario con los datos del atleta
            atleta = {
                "nombre": valores[0],
                "genero": valores[1],
                "edad": int(valores[2]),
                "pais": valores[3],
                "anio": int(valores[4]),
                "evento": valores[5],
                "medalla": valores[6]
            }
            # Agregar el diccionario a la lista de atletas
            lista_atletas.append(atleta)
    # Retornar la lista de atletas
    return lista_atletas

# Función 2: consultar_atletas_por_anio
def consultar_atletas_por_anio(lista_atletas, anio):
    """Recibe una lista de diccionarios con la información de los atletas
    y un año de interés, y retorna un diccionario con los eventos deportivos
    como llaves y las listas de nombres de los atletas como valores.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    anio: un entero con el año de interés.

    Retorno:
    un diccionario con los eventos deportivos como llaves y las listas de
    nombres de los atletas como valores.
    """
    # Crear un diccionario vacío para almacenar los eventos y los atletas
    eventos_atletas = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el año del atleta coincide con el año dado
        if atleta["anio"] == anio:
            # Obtener el evento y el nombre del atleta
            evento = atleta["evento"]
            nombre = atleta["nombre"]
            # Verificar si el evento ya está en el diccionario
            if evento in eventos_atletas:
                # Agregar el nombre del atleta a la lista del evento
                eventos_atletas[evento].append(nombre)
            else:
                # Crear una nueva lista con el nombre del atleta para el evento
                eventos_atletas[evento] = [nombre]
    # Retornar el diccionario de eventos y atletas
    return eventos_atletas

# Función 3: consultar_medallas_por_atleta
def consultar_medallas_por_atleta(lista_atletas, anio_inicio, anio_final, nombre_atleta):
    """Recibe una lista de diccionarios con la información de los atletas,
    un periodo de tiempo definido por dos años, y el nombre de un atleta,
    y retorna una lista de diccionarios que representan las medallas obtenidas por el atleta en ese periodo.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    anio_inicio: un entero con el año inicial del periodo.
    anio_final: un entero con el año final del periodo.
    nombre_atleta: una cadena con el nombre del atleta.

    Retorno:
    una lista de diccionarios con las llaves: anio, evento y medalla.
    """
    # Crear una lista vacía para almacenar las medallas
    lista_medallas = []
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el nombre y el año del atleta coinciden con los dados
        if atleta["nombre"] == nombre_atleta and anio_inicio <= atleta["anio"] <= anio_final:
            # Obtener el año, el evento y la medalla del atleta
            anio = atleta["anio"]
            evento = atleta["evento"]
            medalla = atleta["medalla"]
            # Crear un diccionario con los datos de la medalla
            medalla = {
                "anio": anio,
                "evento": evento,
                "medalla": medalla
            }
            # Agregar el diccionario a la lista de medallas
            lista_medallas.append(medalla)
    # Retornar la lista de medallas
    return lista_medallas
    
def consultar_atletas_por_pais(lista_atletas, pais):
    """Recibe una lista de diccionarios con la información de los atletas
    y un país de interés, y retorna una lista de diccionarios con la información
    de los atletas del país dado.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    pais: una cadena con el nombre del país.

    Retorno:
    una lista de diccionarios con las llaves: nombre, evento y anio.
    """
    # Crear una lista vacía para almacenar los atletas del país
    lista_atletas_pais = []
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el país del atleta coincide con el país dado
        if atleta["pais"] == pais:
            # Obtener el nombre, el evento y el año del atleta
            nombre = atleta["nombre"]
            evento = atleta["evento"]
            anio = atleta["anio"]
            # Crear un diccionario con los datos del atleta
            atleta_pais = {
                "nombre": nombre,
                "evento": evento,
                "anio": anio
            }
            # Agregar el diccionario a la lista de atletas del país
            lista_atletas_pais.append(atleta_pais)
    # Retornar la lista de atletas del país
    return lista_atletas_pais

def consultar_pais_con_mas_medallistas(lista_atletas):
    """Recibe una lista de diccionarios con la información de los atletas
    y retorna un diccionario con el nombre del país que ha tenido más medallistas
    y la cantidad de medallistas.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.

    Retorno:
    un diccionario con el nombre del país como llave y la cantidad de medallistas como valor.
    """
    # Crear un diccionario vacío para almacenar los países y sus medallistas
    paises_medallistas = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el atleta ganó alguna medalla
        if atleta["medalla"] != "na":
            # Obtener el país y el nombre del atleta
            pais = atleta["pais"]
            nombre = atleta["nombre"]
            # Verificar si el país ya está en el diccionario
            if pais in paises_medallistas:
                # Verificar si el nombre del atleta ya está en la lista del país
                if nombre not in paises_medallistas[pais]:
                    # Agregar el nombre del atleta a la lista del país
                    paises_medallistas[pais].append(nombre)
            else:
                # Crear una nueva lista con el nombre del atleta para el país
                paises_medallistas[pais] = [nombre]
    # Crear un diccionario vacío para almacenar el país con más medallistas
    pais_maximo = {}
    # Inicializar una variable para guardar el máximo número de medallistas
    maximo = 0
    # Recorrer cada país y su lista de medallistas en el diccionario
    for pais, medallistas in paises_medallistas.items():
        # Obtener la cantidad de medallistas del país
        cantidad = len(medallistas)
        # Verificar si la cantidad es mayor que el máximo actual
        if cantidad > maximo:
            # Actualizar el máximo y el diccionario del país máximo
            maximo = cantidad
            pais_maximo = {pais: cantidad}
        # Verificar si la cantidad es igual al máximo actual
        elif cantidad == maximo:
            # Agregar el país al diccionario del país máximo
            pais_maximo[pais] = cantidad
    # Retornar el diccionario del país máximo
    return pais_maximo


def consultar_atletas_por_evento_y_medalla(lista_atletas, evento):
    """Recibe una lista de diccionarios con la información de los atletas
    y un evento de interés, y retorna una lista de cadenas con los nombres
    de los atletas que han ganado alguna medalla en el evento.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    evento: una cadena con el nombre del evento.

    Retorno:
    una lista de cadenas con los nombres de los atletas medallistas.
    """
    # Crear una lista vacía para almacenar los nombres de los atletas
    lista_atletas_medallistas = []
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el evento y la medalla del atleta coinciden con el evento dado y no es "na"
        if atleta["evento"] == evento and atleta["medalla"] != "na":
            # Obtener el nombre del atleta
            nombre = atleta["nombre"]
            # Verificar si el nombre del atleta ya está en la lista
            if nombre not in lista_atletas_medallistas:
                # Agregar el nombre del atleta a la lista
                lista_atletas_medallistas.append(nombre)
    # Retornar la lista de nombres de los atletas
    return lista_atletas_medallistas

def consultar_atletas_por_numero_de_medallas(lista_atletas, numero):
    """Recibe una lista de diccionarios con la información de los atletas
    y un número de medallas, y retorna un diccionario con los atletas que han
    ganado una cantidad de medallas superior al número dado.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    numero: un entero con el número de medallas.

    Retorno:
    un diccionario con los nombres de los atletas como llaves y el número de medallas como valores.
    """
    # Crear un diccionario vacío para almacenar los atletas y sus medallas
    atletas_medallas = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el atleta ganó alguna medalla
        if atleta["medalla"] != "na":
            # Obtener el nombre del atleta
            nombre = atleta["nombre"]
            # Verificar si el nombre del atleta ya está en el diccionario
            if nombre in atletas_medallas:
                # Incrementar el número de medallas del atleta en uno
                atletas_medallas[nombre] += 1
            else:
                # Inicializar el número de medallas del atleta en uno
                atletas_medallas[nombre] = 1
    # Crear un diccionario vacío para almacenar los atletas que superan el número dado
    atletas_superiores = {}
    # Recorrer cada atleta y su número de medallas en el diccionario
    for nombre, cantidad in atletas_medallas.items():
        # Verificar si la cantidad es mayor que el número dado
        if cantidad > numero:
            # Agregar el atleta y su cantidad al diccionario de superiores
            atletas_superiores[nombre] = cantidad
    # Retornar el diccionario de superiores
    return atletas_superiores

# Función 8: consultar_atleta_estrella
def consultar_atleta_estrella(lista_atletas):
    """Recibe una lista de diccionarios con la información de los atletas
    y retorna un diccionario con el nombre del atleta que ha obtenido el mayor
    número de medallas en todos los tiempos y la cantidad de medallas.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.

    Retorno:
    un diccionario con el nombre del atleta como llave y la cantidad de medallas como valor.
    """
    # Crear un diccionario vacío para almacenar los atletas y sus medallas
    atletas_medallas = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el atleta ganó alguna medalla
        if atleta["medalla"] != "na":
            # Obtener el nombre del atleta
            nombre = atleta["nombre"]
            # Verificar si el nombre del atleta ya está en el diccionario
            if nombre in atletas_medallas:
                # Incrementar el número de medallas del atleta en uno
                atletas_medallas[nombre] += 1
            else:
                # Inicializar el número de medallas del atleta en uno
                atletas_medallas[nombre] = 1
    # Crear un diccionario vacío para almacenar el atleta estrella
    atleta_maximo = {}
    # Inicializar una variable para guardar el máximo número de medallas
    maximo = 0
    # Recorrer cada atleta y su número de medallas en el diccionario
    for nombre, cantidad in atletas_medallas.items():
        # Verificar si la cantidad es mayor que el máximo actual
        if cantidad > maximo:
            # Actualizar el máximo y el diccionario del atleta máximo
            maximo = cantidad
            atleta_maximo = {nombre: cantidad}
        # Verificar si la cantidad es igual al máximo actual
        elif cantidad == maximo:
            # Agregar el atleta al diccionario del atleta máximo
            atleta_maximo[nombre] = cantidad
    # Retornar el diccionario del atleta máximo
    return atleta_maximo

# Función 9: 
def consultar_pais_con_mejor_desempenio_en_evento(lista_atletas, evento):
    """Recibe una lista de diccionarios con la información de los atletas
    y el nombre de un evento, y retorna un diccionario con el nombre del país que ha tenido mejor desempeño en dicho evento y una lista con las medallas obtenidas.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    evento: una cadena con el nombre del evento.

    Retorno:
    un diccionario con el nombre del país como llave y una lista con las medallas obtenidas como valor.
    """
    # Crear un diccionario vacío para almacenar los países y sus medallas en el evento
    paises_medallas = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el evento y la medalla del atleta coinciden con el evento dado y no es "na"
        if atleta["evento"] == evento and atleta["medalla"] != "na":
            # Obtener el país y la medalla del atleta
            pais = atleta["pais"]
            medalla = atleta["medalla"]
            # Verificar si el país ya está en el diccionario
            if pais in paises_medallas:
                # Agregar la medalla a la lista del país
                paises_medallas[pais].append(medalla)
            else:
                # Crear una nueva lista con la medalla para el país
                paises_medallas[pais] = [medalla]
    # Crear un diccionario vacío para almacenar el país con mejor desempeño en el evento
    pais_maximo = {}
    # Inicializar una variable para guardar el valor máximo de las medallas
    maximo = 0
    # Recorrer cada país y su lista de medallas en el diccionario
    for pais, medallas in paises_medallas.items():
        # Obtener el valor de las medallas del país
        valor = calcular_valor_medallas(medallas)
        # Verificar si el valor es mayor que el máximo actual
        if valor > maximo:
            # Actualizar el máximo y el diccionario del país máximo
            maximo = valor
            pais_maximo = {pais: medallas}
        # Verificar si el valor es igual al máximo actual
        elif valor == maximo:
            # Agregar el país al diccionario del país máximo
            pais_maximo[pais] = medallas
    # Retornar el diccionario del país máximo
    return pais_maximo

# Función auxiliar para calcular el valor de las medallas
def calcular_valor_medallas(medallas):
    """Recibe una lista de cadenas con las medallas obtenidas por un país
    y retorna un número que representa el valor de las medallas según los siguientes criterios:
    - Una medalla de oro vale 3 puntos.
    - Una medalla de plata vale 2 puntos.
    - Una medalla de bronce vale 1 punto.

    Parámetros:
    medallas: una lista de cadenas con las medallas obtenidas por un país.

    Retorno:
    un número que representa el valor de las medallas.
    """
    # Inicializar una variable para guardar el valor de las medallas
    valor = 0
    # Recorrer cada medalla en la lista
    for medalla in medallas:
        # Verificar el tipo de medalla y sumar su valor al total
        if medalla == "oro":
            valor += 3
        elif medalla == "plata":
            valor += 2
        elif medalla == "bronce":
            valor += 1
    # Retornar el valor de las medallas
    return valor

def consultar_atleta_todoterreno(lista_atletas):
    """Recibe una lista de diccionarios con la información de los atletas
    y retorna una cadena con el nombre del atleta que ha participado en más eventos
    diferentes en todos los tiempos.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.

    Retorno:
    una cadena con el nombre del atleta todoterreno.
    """
    # Crear un diccionario vacío para almacenar los atletas y sus eventos
    atletas_eventos = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Obtener el nombre y el evento del atleta
        nombre = atleta["nombre"]
        evento = atleta["evento"]
        # Verificar si el nombre del atleta ya está en el diccionario
        if nombre in atletas_eventos:
            # Verificar si el evento ya está en la lista del atleta
            if evento not in atletas_eventos[nombre]:
                # Agregar el evento a la lista del atleta
                atletas_eventos[nombre].append(evento)
        else:
            # Crear una nueva lista con el evento para el atleta
            atletas_eventos[nombre] = [evento]
    # Crear una variable para almacenar el nombre del atleta todoterreno
    atleta_todoterreno = ""
    # Inicializar una variable para guardar el máximo número de eventos
    maximo = 0
    # Recorrer cada atleta y su lista de eventos en el diccionario
    for nombre, eventos in atletas_eventos.items():
        # Obtener la cantidad de eventos del atleta
        cantidad = len(eventos)
        # Verificar si la cantidad es mayor que el máximo actual
        if cantidad > maximo:
            # Actualizar el máximo y el nombre del atleta todoterreno
            maximo = cantidad
            atleta_todoterreno = nombre
        # Verificar si la cantidad es igual al máximo actual
        elif cantidad == maximo:
            # Concatenar el nombre del atleta al nombre del atleta todoterreno
            atleta_todoterreno += ", " + nombre
    # Retornar el nombre del atleta todoterreno
    return atleta_todoterreno

def consultar_medallistas_por_pais_y_genero(lista_atletas, pais, genero):
    """Recibe una lista de diccionarios con la información de los atletas,
    el nombre de un país y un género, y retorna un diccionario con los medallistas
    de dicho país y género. Las llaves del diccionario son los nombres de cada 
    atleta medallista, y los valores son listas de diccionarios que representan 
    las medallas de dicho deportista.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.
    pais: una cadena con el nombre del país.
    genero: una cadena con el género ("m" o "f").

    Retorno:
    un diccionario con los medallistas por país y género.
    """

    # Crear un diccionario vacío para almacenar los medallistas por país y género
    medallistas_pais_genero = {}
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Verificar si el país, el género y la medalla del atleta coinciden con los dados y no es "na"
        if atleta["pais"] == pais and atleta["genero"] == genero and atleta["medalla"] != "na":
            # Obtener el nombre, el año, el evento y la medalla del atleta
            nombre = atleta["nombre"]
            anio = atleta["anio"]
            evento = atleta["evento"]
            medalla = atleta["medalla"]
            # Crear un diccionario con los datos de la medalla
            medalla = {
                "anio": anio,
                "evento": evento,
                "medalla": medalla
            }
            # Verificar si el nombre del atleta ya está en el diccionario
            if nombre in medallistas_pais_genero:
                # Agregar el diccionario de la medalla a la lista del atleta
                medallistas_pais_genero[nombre].append(medalla)
            else:
                # Crear una nueva lista con el diccionario de la medalla para el atleta
                medallistas_pais_genero[nombre] = [medalla]
    # Retornar el diccionario de medallistas por país y género
    return medallistas_pais_genero
    

def consultar_porcentaje_medallistas(lista_atletas):
    """Recibe una lista de diccionarios con la información de los atletas
    y retorna el porcentaje de atletas que ganaron alguna medalla en todos los tiempos,
    con dos decimales de aproximación.

    Parámetros:
    lista_atletas: una lista de diccionarios con los datos de los atletas.

    Retorno:
    un número que representa el porcentaje de medallistas.
    """
    # Crear una lista vacía para almacenar los nombres de los atletas
    lista_atletas = []
    # Crear una lista vacía para almacenar los nombres de los medallistas
    lista_medallistas = []
    # Recorrer cada atleta en la lista
    for atleta in lista_atletas:
        # Obtener el nombre y la medalla del atleta
        nombre = atleta["nombre"]
        medalla = atleta["medalla"]
        # Verificar si el nombre del atleta no está en la lista de atletas
        if nombre not in lista_atletas:
            # Agregar el nombre del atleta a la lista de atletas
            lista_atletas.append(nombre)
        # Verificar si el atleta ganó alguna medalla
        if medalla != "na":
            # Verificar si el nombre del atleta no está en la lista de medallistas
            if nombre not in lista_medallistas:
                # Agregar el nombre del atleta a la lista de medallistas
                lista_medallistas.append(nombre)
    # Calcular el número total de atletas
    total_atletas = len(lista_atletas)
    # Calcular el número total de medallistas
    total_medallistas = len(lista_medallistas)
    # Calcular el porcentaje de medallistas
    porcentaje = (total_medallistas / total_atletas) * 100
    # Redondear el porcentaje a dos decimales
    porcentaje = round(porcentaje, 2)
    # Retornar el porcentaje
    return porcentaje