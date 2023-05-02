import olimpicos as olim

def ejecutar_cargar_atletas() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    los atletas y los carga.
    Retorno: list
        La lista de atletas con la información del archivo.
    """
    # Crear una variable para almacenar la lista de atletas
    atletas = None
    # Pedir al usuario que ingrese el nombre del archivo
    archivo = input("Por favor ingrese el nombre del archivo CSV con los atletas: ")
    # Llamar a la función del módulo olim que carga los atletas desde el archivo
    atletas = olim.cargar_atletas(archivo)
    # Verificar si la lista de atletas está vacía
    if len(atletas) == 0:
        # Mostrar un mensaje de error
        print("El archivo seleccionado no es válido. No se pudieron cargar los atletas olímpicos")
    else:
        # Mostrar un mensaje de éxito con el número de atletas cargados
        print("Se cargaron", len(atletas), "atletas a partir del archivo.")
    # Retornar la lista de atletas
    return atletas

def ejecutar_atletas_por_anio(atletas: list) -> None:
    """ Ejecuta la opción de buscar los atletas de un año dado
    """
    # Solicitar al usuario que ingrese el año de su interés
    anio = int(input("Ingrese el año de su interés: "))
    # Llamar a la función consultar_atletas_por_anio del módulo olim
    eventos_atletas = olim.consultar_atletas_por_anio(atletas, anio)
    # Verificar si el diccionario de eventos y atletas está vacío
    if not eventos_atletas:
        # Imprimir un mensaje indicando que no hay atletas para el año dado
        print("No hay atletas registrados para el año", anio)
    else:
        # Imprimir un mensaje indicando el número de eventos para el año dado
        print("Hay", len(eventos_atletas), "eventos registrados para el año", anio)
        # Recorrer cada evento y su lista de atletas en el diccionario
        for evento, lista in eventos_atletas.items():
            # Imprimir el nombre del evento y el número de atletas
            print(evento, ":", len(lista), "atletas")
            # Recorrer cada atleta en la lista
            for atleta in lista:
                # Imprimir el nombre del atleta
                print("-", atleta)
                
def ejecutar_medallas_en_rango(atletas: list) -> None:
    """ Ejecuta la opción de buscar las medallas de un atleta
    en un rango específico de años 
    """ 
    
    # Solicitar al usuario que ingrese el nombre del atleta de su interés
    nombre = input("Ingrese el nombre del atleta de su interés: ")
    # Solicitar al usuario que ingrese el límite inferior del rango
    anio_menor = int(input("Ingrese el límite inferior del rango: "))
    # Solicitar al usuario que ingrese el límite superior del rango
    anio_mayor = int(input("Ingrese el límite superior del rango: "))
    # Llamar a la función consultar_medallas_en_rango del módulo olim
    medallas = olim.consultar_medallas_en_rango(atletas, anio_menor, anio_mayor, nombre)
    # Verificar si la lista de medallas está vacía
    if not medallas:
        # Imprimir un mensaje indicando que no hay medallas para el atleta en el rango dado
        print("No hay medallas registradas para", nombre, "entre los años", anio_menor, "y", anio_mayor)
    else:
        # Imprimir un mensaje indicando el número de medallas para el atleta en el rango dado
        print(nombre, "obtuvo", len(medallas), "medallas entre los años", anio_menor, "y", anio_mayor)
        # Recorrer cada medalla en la lista
        for medalla in medallas:
            # Imprimir el año, el evento y la medalla obtenidos
            print("-", medalla["anio"], "-", medalla["evento"], "-", medalla["medalla"])
            
def ejecutar_atletas_por_pais(atletas: list) -> None:
    """ Ejecuta la opción de buscar los atletas de un país específico
    """
        
    # Solicitar al usuario que ingrese el nombre del país de su interés
    pais = input("Ingrese el nombre del país de su interés: ")
    # Llamar a la función consultar_atletas_por_pais del módulo olim
    atletas_pais = olim.consultar_atletas_por_pais(atletas, pais)
    # Verificar si la lista de atletas del país está vacía
    if not atletas_pais:
        # Imprimir un mensaje indicando que no hay atletas para el país dado
        print("No hay atletas registrados para el país", pais)
    else:
        # Imprimir un mensaje indicando el número de atletas para el país dado
        print("Hay", len(atletas_pais), "atletas registrados para el país", pais)
        # Recorrer cada atleta en la lista
        for atleta in atletas_pais:
            # Imprimir el nombre, el evento y el año del atleta
            print("-", atleta["nombre"], "-", atleta["evento"], "-", atleta["anio"])

def ejecutar_pais_con_mas_atletas(atletas: list) -> None:
    """ Ejecuta la opción de buscar el país con más atletas
    """
    
    # Llamar a la función consultar_pais_con_mas_atletas del módulo olim
    pais_maximo = olim.consultar_pais_con_mas_atletas(atletas)
    # Verificar si el diccionario del país máximo está vacío
    if not pais_maximo:
        # Imprimir un mensaje indicando que no hay datos disponibles
        print("No hay datos disponibles para esta consulta")
    else:
        # Imprimir un mensaje indicando el país o los países con más atletas
        print("El país o los países con más atletas son:")
        # Recorrer cada país y su número de atletas en el diccionario
        for pais, cantidad in pais_maximo.items():
            # Imprimir el nombre del país y la cantidad de atletas
            print("-", pais, ":", cantidad, "atletas")

def ejecutar_medallistas_por_evento(atletas: list) -> None:
    """ Ejecuta la opción de buscar los medallistas de un evento dado
    """
    
    # Pedir al usuario el evento de su interés
    evento = input("Ingrese el evento de su interés: ")

    # Llamar a la función del módulo olim que busca los medallistas de ese evento
    medallistas = olim.buscar_medallistas_por_evento(atletas, evento)

    # Verificar si hay medallistas para ese evento
    if medallistas:
        # Imprimir un mensaje indicando el evento y el número de medallistas
        print("Los medallistas del evento", evento, "son", len(medallistas), ":")
        
        # Recorrer cada medallista en la lista
        for medallista in medallistas:
            # Imprimir el nombre, el país y la medalla del medallista
            print("-", medallista["nombre"], "-", medallista["pais"], "-", medallista["medalla"])
    else:
        # Imprimir un mensaje indicando que no hay medallistas para ese evento
        print("No hay medallistas para el evento", evento)# Pedir al usuario el evento de su interés
    

def ejecutar_atletas_con_mas_medallas_que(atletas: list) -> None:
    """ Ejecuta la opción de buscar los atletas que han obtenido 
    una cantidad de medallas superior a un número dado
    """
    
    # Pedir al usuario el mínimo de medallas
    limite = int(input("Ingrese el mínimo de medallas: "))

    # Llamar a la función del módulo olim que busca los atletas con más medallas que el límite
    atletas_destacados = olim.buscar_atletas_con_mas_medallas_que(atletas, limite)

    # Verificar si hay atletas que cumplan con el criterio
    if atletas_destacados:
        # Imprimir un mensaje indicando el número de atletas encontrados
        print("Los atletas que han obtenido más de", limite, "medallas son", len(atletas_destacados), ":")
        
        # Recorrer cada atleta en la lista
        for atleta in atletas_destacados:
            # Imprimir el nombre y el número de medallas del atleta
            print("-", atleta["nombre"], "-", atleta["medallas"])
    else:
        # Imprimir un mensaje indicando que no hay atletas que cumplan con el criterio
        print("No hay atletas que hayan obtenido más de", limite, "medallas")# Pedir al usuario el mínimo de medallas
    limite = int(input("Ingrese el mínimo de medallas: "))

    # Llamar a la función del módulo olim que busca los atletas con más medallas que el límite
    atletas_destacados = olim.buscar_atletas_con_mas_medallas_que(atletas, limite)

    # Verificar si hay atletas que cumplan con el criterio
    if atletas_destacados:
        # Imprimir un mensaje indicando el número de atletas encontrados
        print("Los atletas que han obtenido más de", limite, "medallas son", len(atletas_destacados), ":")
        
        # Recorrer cada atleta en la lista
        for atleta in atletas_destacados:
            # Imprimir el nombre y el número de medallas del atleta
            print("-", atleta["nombre"], "-", atleta["medallas"])
    else:
        # Imprimir un mensaje indicando que no hay atletas que cumplan con el criterio
        print("No hay atletas que hayan obtenido más de", limite, "medallas")

def ejecutar_atleta_estrella(atletas: list) -> None:
    """ Ejecuta la opción de buscar el atleta con
    más medallas de todos los tiempos
    """
    # Llamar a la función del módulo olim que busca el atleta con más medallas de todos los tiempos
    atleta_estrella = olim.buscar_atleta_estrella(atletas)

    # Verificar si hay un atleta estrella
    if atleta_estrella:
        # Imprimir un mensaje indicando el nombre y el número de medallas del atleta estrella
        print("El atleta con más medallas de todos los tiempos es", atleta_estrella["nombre"], "con", atleta_estrella["medallas"], "medallas")
    else:
        # Imprimir un mensaje indicando que no hay un atleta estrella
        print("No hay un atleta con más medallas de todos los tiempos")    

    
def ejecutar_mejor_pais_en_un_evento(atletas: list) -> None:
    """ Ejecuta la opción de buscar el país con mejor
    desempeño en un evento en específico
    """
    
    # Pedir al usuario el evento de su interés
    evento = input("Ingrese el evento de su interés: ")

    # Llamar a la función del módulo olim que busca el país con mejor desempeño en ese evento
    pais_ganador = olim.buscar_mejor_pais_en_un_evento(atletas, evento)

    # Verificar si hay un país ganador para ese evento
    if pais_ganador:
        # Imprimir un mensaje indicando el evento y el país ganador
        print("El país con mejor desempeño en el evento", evento, "es", pais_ganador)
    else:
        # Imprimir un mensaje indicando que no hay un país ganador para ese evento
        print("No hay un país con mejor desempeño en el evento", evento)
    
def ejecutar_todoterreno(atletas: list) -> None:
    """ Ejecuta la opción de buscar el atleta más todoterreno
    de todos los tiempos
    """
    
    # Llamar a la función del módulo olim que busca el atleta más todoterreno de todos los tiempos
    atleta_todoterreno = olim.buscar_atleta_todoterreno(atletas)

    # Verificar si hay un atleta todoterreno
    if atleta_todoterreno:
        # Imprimir un mensaje indicando el nombre y los eventos del atleta todoterreno
        print("El atleta más todoterreno de todos los tiempos es", atleta_todoterreno["nombre"], "que ha participado en", atleta_todoterreno["eventos"], "eventos")
    else:
        # Imprimir un mensaje indicando que no hay un atleta todoterreno
        print("No hay un atleta más todoterreno de todos los tiempos")
    
def ejecutar_medallistas_por_nacion_y_genero(atletas: list) -> None:
    """ Ejecuta la opción de buscar los medallistas de un país
    y género específicos
    """
    
    # Pedir al usuario el país y el género de su interés
    pais = input("Ingrese el país de su interés: ")
    genero = input("Ingrese el género de su interés (m o f): ")

    # Llamar a la función del módulo olim que busca los medallistas de ese país y género
    medallistas = olim.buscar_medallistas_por_nacion_y_genero(atletas, pais, genero)

    # Verificar si hay medallistas para ese país y género
    if medallistas:
        # Imprimir un mensaje indicando el país, el género y el número de medallistas
        print("Los medallistas del país", pais, "y del género", genero, "son", len(medallistas), ":")
        
        # Recorrer cada medallista en la lista
        for medallista in medallistas:
            # Imprimir el nombre y la medalla del medallista
            print("-", medallista["nombre"], "-", medallista["medalla"])
    else:
        # Imprimir un mensaje indicando que no hay medallistas para ese país y género
        print("No hay medallistas del país", pais, "y del género", genero)

def ejecutar_porcentaje_medallistas(atletas: list) -> None:
    """ Ejecuta la opción de calcular el porcentaje de medallistas 
    """
        
    # Llamar a la función del módulo olim que calcula el porcentaje de medallistas
    porcentaje = olim.calcular_porcentaje_medallistas(atletas)

    # Imprimir un mensaje indicando el porcentaje de medallistas
    print("El porcentaje de medallistas sobre el total de atletas es", porcentaje, "%")


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de atletas")
    print("2. Consultar los atletas de un año dado")
    print("3. Consultar las medallas de un atleta en un periodo")
    print("4. Consultar los atletas de un país dado")
    print("5. Consultar el país con más medallistas")
    print("6. Consultar todos los medallistas de un evento dado")
    print("7. Consultar los atletas más populares")
    print("8. Consultar el atleta estrella de todos los tiempos")
    print("9. Consultar el mejor país en un evento")
    print("10. Consultar el atleta Todoterreno")
    print("11. Consultar los medallistas por nación y género")
    print("12. Consultar el porcentaje de atletas que son medallistas")
    print("13. Salir de la aplicación")
	
def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    atletas = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            atletas=ejecutar_cargar_atletas()
        elif opcion_seleccionada == 2:
            ejecutar_atletas_por_anio(atletas)
        elif opcion_seleccionada == 3:
            ejecutar_medallas_en_rango(atletas)
        elif opcion_seleccionada == 4:
            ejecutar_atletas_por_pais(atletas)
        elif opcion_seleccionada == 5:
            ejecutar_pais_con_mas_atletas(atletas)
        elif opcion_seleccionada == 6:
            ejecutar_medallistas_por_evento(atletas)
        elif opcion_seleccionada == 7:
            ejecutar_atletas_con_mas_medallas_que(atletas)
        elif opcion_seleccionada == 8:
            ejecutar_atleta_estrella(atletas)
        elif opcion_seleccionada == 9:
            ejecutar_mejor_pais_en_un_evento(atletas)
        elif opcion_seleccionada == 10:
            ejecutar_todoterreno(atletas)
        elif opcion_seleccionada == 11:
            ejecutar_medallistas_por_nacion_y_genero(atletas)
        elif opcion_seleccionada == 12:
            ejecutar_porcentaje_medallistas(atletas)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

