# Simulador de chatbot para gestión de vacaciones
# Trabajo Práctico Integrador - Organización Empresarial

import pandas as pd

# El archivo Excel debe estar en la misma carpeta que este archivo .py
# Columnas esperadas: Legajo, Nombre, Dias_Disponibles
archivo_excel = "empleados.xlsx"

try:
    empleados = pd.read_excel(archivo_excel)
except FileNotFoundError:
    print("No se encontró el archivo empleados.xlsx.")
    print("Verificá que el archivo esté en la misma carpeta que chatbot_vacaciones.py.")
    exit()

estado = "Inicio"

print("Bienvenido al chatbot de gestión de vacaciones")

while estado != "Fin":

    if estado == "Inicio":
        estado = "Esperando Legajo"

    elif estado == "Esperando Legajo":
        legajo = input("Ingrese su número de legajo: ")

        if not legajo.isdigit():
            print("Debe ingresar un legajo numérico.")
        else:
            legajo = int(legajo)
            empleado = empleados[empleados["Legajo"] == legajo]

            if empleado.empty:
                print("El legajo ingresado no existe. Por favor, vuelva a intentarlo.")
            else:
                estado = "Validando Empleado"

    elif estado == "Validando Empleado":
        nombre = empleado.iloc[0]["Nombre"]
        dias_disponibles = int(empleado.iloc[0]["Dias_Disponibles"])

        print(f"Empleado encontrado: {nombre}")
        estado = "Mostrando Saldo"

    elif estado == "Mostrando Saldo":
        print(f"Días disponibles: {dias_disponibles}")
        estado = "Esperando Solicitud"

    elif estado == "Esperando Solicitud":
        solicitud = input("Ingrese la cantidad de días que desea solicitar: ")

        if not solicitud.isdigit():
            print("Debe ingresar un número válido.")
        else:
            solicitud = int(solicitud)

            if solicitud <= 0:
                print("La cantidad ingresada debe ser mayor que cero.")
            else:
                estado = "Evaluando Solicitud"

    elif estado == "Evaluando Solicitud":
        if solicitud <= dias_disponibles:
            nuevo_saldo = dias_disponibles - solicitud

            empleados.loc[empleados["Legajo"] == legajo, "Dias_Disponibles"] = nuevo_saldo
            empleados.to_excel(archivo_excel, index=False)

            print("Solicitud aprobada.")
            print(f"Nuevo saldo disponible: {nuevo_saldo} días.")
            estado = "Solicitud Aprobada"
        else:
            print("Solicitud rechazada. Saldo insuficiente.")
            print(f"Usted cuenta con {dias_disponibles} días disponibles.")
            estado = "Solicitud Rechazada"

    elif estado == "Solicitud Aprobada":
        estado = "Fin"

    elif estado == "Solicitud Rechazada":
        estado = "Fin"

print("Gracias por utilizar el sistema de gestión de vacaciones.")