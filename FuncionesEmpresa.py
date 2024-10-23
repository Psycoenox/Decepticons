# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:27:12 2024
Aqui dentro estaran las funciones de la empresa
@author: Marcell
"""
#Funcion importada para poder salir del programa
import sys as sys

#Lista para almacenar empleados
empleados = []

#Clase Padre
class Empleados():
    def __init__(self, nombre, edad, id_empleado):
        self.nombre = nombre
        self.edad = edad
        self.id_empleado = id_empleado
#Clase Hija
class EmpleadoAsalariado(Empleados):
    def salarioMensual(self, salarioMensual):
        return f"Su salario mensualmente es de {self.salarioMensual}"
#Clase Hija    
class EmpleadoHora(Empleados):
    def salarioHora(self, salarioHora):
        return f"Su salario por hora es de {self.salarioHora}"
    
    
    
#Metodo para agregar empleado
def agregar_empleado():
    print("Agregar Empleado")
    nombre = input("Nombre del empleado: ")
    edad = input("Edad del empleado: ")
    id_empleado = input("ID empleado: ")
    
    
    tipoEmpleado = input("Tipo de empleado(1. Asalariado / 2. Por hora): ")
    
    #definir el tipo de empleado que quieras que sea --> 1 si es Asalariado, 2 si es por hora
    if tipoEmpleado == "1" :
        print(f"Empleado Asalariado")
        salarioMensual = float(input(f"Ingrese el salario mensual: "))
        empleado = EmpleadoAsalariado(nombre, edad, id_empleado)
        empleado.salarioMensual = salarioMensual
        empleados.append(empleado)
        print(f"Empleado {nombre} agregado como asalariado con un salario mensual de {salarioMensual}")
    
    elif tipoEmpleado == "2":
        print(f"Empleado Por Hora")
        salarioHora = float(input(f"Ingrese el salario por hora: "))
        horas_trabajadas = float(input(f"Ingrese el numero de horas trabajadas en el mes: "))
        empleado = EmpleadoHora(nombre, edad, id_empleado)
        empleado.salarioHora = salarioHora
        empleado.horasTrabajadas = horas_trabajadas
        empleados.append(empleado)
        print(f"Empleado {nombre} agregado como Por Horas con un salario de {salarioHora} por Hora")
    
    else:
        print(f"Tipo de empleado no valido. Intentalo de nuevo")
        
#Metodo para calcular el costo de los empleados      
def calcular_costos_empleados():
    print("Calcular el costo total de los empleados seleccionado.")

    costo_total = 0

    for empleado in empleados:
        #Verifica si el objeto empleado es una instancia de la clase EmpleadoAsalariado
        if isinstance(empleado, EmpleadoAsalariado):
            costo_total += empleado.salarioMensual
        #Verifica si el objeto empleado es una instancia de la clase EmpleadoHora
        elif isinstance(empleado, EmpleadoHora):
            costo_total += empleado.salarioHora * empleado.horasTrabajadas

        print(f"El costo total de los empleados es {costo_total}")

#Metodo para listar los empleados
def listar_empleados():
    print("Listar empleados seleccionado.")
    if not empleados:
        print(f"No hay empleados registrados")
    else:
        print(f"Lista de empleados")
        for empleado in empleados:
            print(f"ID: {empleado.id_empleado}, Nombre: {empleado.nombre}, Edad: {empleado.edad}  ")
            #Verifica si el objeto empleado es una instancia de la clase EmpleadoAsalariado
            if isinstance(empleado, EmpleadoAsalariado):
                print(f"   Tipo: Asalariado, Salario Mensual: {empleado.salarioMensual}")
             #Verifica si el objeto empleado es una instancia de la clase EmpleadoHora
            elif isinstance(empleado, EmpleadoHora):
                print(f"   Tipo: Por Hora, Salario por Hora: {empleado.salarioHora}")

#Metodo para salir
def salir():
    print("Saliendo del programa...")
    sys.exit()
    
#Metodo para llamar al menu
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar empleado")
        print("2. Calcular costo de los empleados")
        print("3. Listar empleados")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        # Diccionario de opciones
        opciones = {
            "1": agregar_empleado,
            "2": calcular_costos_empleados,
            "3": listar_empleados,
            "4": salir
        }
        
        # Ejecutar la opción seleccionada
        funcion = opciones.get(opcion)
        if funcion:
            funcion()
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()




