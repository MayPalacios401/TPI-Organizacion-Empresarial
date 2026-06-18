#Cargar empleados desde el CSV
def cargar_empleados():
    empleados = [] #Lista para almacenar los empleados
    with open("base_datos/empleados.csv", "r", encoding="utf-8") as archivo: #Encoding para que lea las tildes
        lineas = archivo.readlines() #Leemos todas las líneas del archivo y las guardamos en una lista
        for linea in lineas[1:]:  #Salteamos el encabezado
            partes = linea.strip().split(",") #Creamos una lista con los valores de cada línea.
            # Creamos un diccionario para cada empleado y lo agregamos a la lista empleados
            empleado = {
                "legajo": int(partes[0]),
                "nombre": partes[1],
                "dias_disponibles": int(partes[2]),
                "estado": partes[3]
            }
            empleados.append(empleado)
    return empleados



#Buscar empleado por legajo

def buscar_empleado(legajo, empleados):
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            return empleado
    return None #Si al terminar el bucle no se encuentra el empleado, se devuelve None para indicar que no se encontró.



#Solicitar legajo y validar
def solicitar_legajo():
    while True:
        try:
            legajo = int(input(" Por favor, ingrese su número de legajo: "))
            return legajo
        except ValueError:
            print(" El valor ingresado no es válido. Por favor, ingrese solo números.")


# Función 4: Solicitar días y validar
def solicitar_dias():
    while True:
        try:
            dias = int(input(" ¿Cuántos días desea solicitar? "))
            if dias <= 0:
                print(" La cantidad de días debe ser mayor a cero.")
            else:
                return dias
        except ValueError:
            print(" El valor ingresado no es válido. Por favor, ingrese solo números.")



# Función 5: Actualizar saldo en la lista
def actualizar_saldo(legajo, dias, empleados):
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            empleado["dias_disponibles"] -= dias
            return



# Función principal - flujo del bot

def ejecutar_bot():
    print("=" * 50)
    print("\n Bienvenido al sistema de gestión de vacaciones de TechSolutions S.A.")
    print("=" * 50)

    empleados = cargar_empleados() #Cargamos todos los empleados del CSV en memoria

    # Estado 1: Solicitar legajo
    legajo = solicitar_legajo() #Llamamos a la función para solicitar el legajo y validarlo

    # Gateway 1: ¿Existe el empleado?
    empleado = buscar_empleado(legajo, empleados) #Buscamos el empleado en la lista de empleados cargada desde el CSV

    #Camino infeliz 1: empleado no encontrado
    if empleado is None:
        print("\n El legajo ingresado no fue encontrado en el sistema.")
        print("\n Por favor, verifique el número e intente nuevamente.")
        print("\n Proceso finalizado.")
        return

    # Mostrar datos del empleado
    print(f" Empleado encontrado: {empleado['nombre']}")
    print(f" Usted tiene {empleado['dias_disponibles']} días de vacaciones disponibles.")

    # Caso especial: saldo en cero. Informamos al usuario y finalizamos el proceso antes de preguntar por los días solicitados.
    if empleado["dias_disponibles"] == 0:
        print("\n No tiene días disponibles. Consulte con Recursos Humanos.")
        print("\n Proceso finalizado.")
        return

    # Estado 2: Solicitar días
    dias_solicitados = solicitar_dias()

    # Gateway 2: ¿Tiene días suficientes?
    if dias_solicitados <= empleado["dias_disponibles"]:
        #Camino feliz: los días solicitados están dentro del saldo disponible.
        actualizar_saldo(legajo, dias_solicitados, empleados) #Descontamos los días
        print(f"\n Su solicitud de {dias_solicitados} días ha sido APROBADA.")
        print(f"\n Su nuevo saldo es de {empleado['dias_disponibles']} días disponibles.")
        print("\n ¡Que disfrute sus vacaciones!")
    else:
        #Camino infeliz 2: los días solicitados superan el saldo disponible.
        print(f"\nSu solicitud no puede ser procesada.")
        print(f"\nUsted solicitó {dias_solicitados} días pero solo dispone de {empleado['dias_disponibles']}.")
        print("\nPor favor, ingrese una cantidad válida.")

    print("=" * 50)
    print("\nGracias por utilizar el sistema de TechSolutions S.A.")
    print("=" * 50)


ejecutar_bot()
