#%% 1. es como para hacer una especie de indice (#%%)
"""
Created on Fri Oct  4 21:05:35 2024
Para comentar se usa (""" """) y todo lo que este dentro estara comentado
@author: Marcell Gonzalez Try
Clase: Desarrollo de interfaces 04/10/2024
          
"""

#%%2. Importaciones
import numpy as np
#NumPy (Numerical Python) es una biblioteca de Python que se utiliza principalmente para computación numérica.
#%%2. Hola mundo
# Para comentar se usa Ctrl + 1 y te comenta la linea
# print("Hola mundo")

#%% 3.pedir informacion

# nombre = input("Cuál es tu nombre? ")
# edad = int(input("Cuál es tu edad? ") )
# if edad > 25 : 
#     print = ("Hola te llamas",nombre,"y tienes",edad,"lo que significa que eres un poco viejo")
# else:
#     print = ("Hola te llamas",nombre,"y tienes",edad,"lo que significa que eres un poco joven") 
#%% 4. Chequeo de errores
# nombre = input("Cual es tu nombre? ")
# if nombre.isdigit():
#     print("Error, mete un string")
#     exit()
    
# #verificar un numero
# try:
#     edad = int(input("Cual es tu edad? "))
# except ValueError:
#     print("Mete un numero")
#     exit()
###############################################################################
                        # Variables inmodificables #
###############################################################################
"""
int, str, tuplas, float, bool.
"""
# 4.1 int
# a = 10
# b = 10
# print(id(a), id(b)) La direccion en memoria es igual porque tiene precargado el mismo valor en este caso 10
# a = 10
# b = 5
# print(id(a), id(b)) # Sera distinto debido a que los valores son distintos por ende la direccion de memoria es distinta

#4.2 string son iguales que los int 
#siempre que pedimos algo por pantalla la terminal lo procesara como un string 
#si queremos procesarlo luego tenemos que cambiarlo al tipo de variable que queramos


# #4.3 Tuplas son listas inmutables las creamos y no las podemos modificar, aqui los indices empiezan por 0
# """
    
# # """
# # tupla = (1,2,3)
# # # print(tupla) 
# # # # para sacar una posicion sera tupla[0] y imprimira la primera posicion
# # # # para añadir otro valor en la tupla se haria lo siguiente 
# # tupla = tupla + (4,)
# # print(tupla)
# # # # Nos emprimira dos tuplas distintas si lo comprobamos en terminal
# # #Acceder a los elementos
# # E2 = tupla[1]

# # def calc_suma(a,b):
# #     suma = a + b
# #     resta = a - b
# #     return suma,resta

# resultado = calc_suma(10,5)
# a,b,c,d = tupla

# 4.4 Listas 
# creacion
# lista = [1,2,3,4]
# lista.append(5)
# for elemento in lista:
#     print(elemento)
# E0 = print(lista[0])
# Lista anidadas 
# Creacion
# lista_anidada = [1,2,3, [4,5, [6,7]]]
# lista.append(1) #añade un valor
# lista.extend([2,3,4]) #
# lista.sort() 


#Como hacer el ejercicio de ayer

#Matriz 2*2

#Para crearla de dentro hacia afuera es la forma correcta
#10 filas y 2 columnas
# rapido
# n_filas1, n_columnas1 = 4, 2
# n_filas2, n_columnas2 = 2, 2
# n_filas3, n_columnas3 = 4, 3
# M = [] #inicializamos la matriz
# c = 1
#forma1
# for i in range(n_filas1):
#     filai1 = []
#     for j in range(n_columnas1):
#         filai1.append(c)
#         c += 1
#     M.append(filai1)
###############################################################################ç

#forma bonita (Estudiar)
# M = [[0 for _ in range(n_columnas1)]
#      for _ in range(n_filas1)]
# for i in range(n_filas1):
#     for j in range(n_columnas1):
#         M[i][j] = [[0 for _ in range(n_columnas2)]
#              for _ in range(n_filas2)]  
#         for ii in range(n_filas2):
#             for jj in range(n_columnas2):
#                 M[i][j][ii][jj] = [[0 for _ in range(n_columnas3)]
#                      for _ in range(n_filas3)] 
#                 c=1
#                 for iii in range(n_filas3):
#                     for jjj in range (n_columnas3):
#                         M[i][j][ii][jj][iii][jjj]
#                         c =+1

#Hacer con numpy
# MatrizNumpy = np.arange(1, n_filas1*n_columnas1 + 1) # Arange: para crear el vector tienes que ponerle un +1 para no saltarnos la primera iteracion
# MatrizNumpy = np.reshape(MatrizNumpy, (n_filas1, n_columnas1)) #Reshape reordenarlos como yo quiero

# MatrizAntigua = np.arange(1,n_filas1*n_columnas1 * n_filas2*n_columnas2 * n_filas3*n_columnas3 + 1 ) #linea 1
# MatrizAntigua = np.reshape(MatrizAntigua,(n_filas1, n_columnas1, n_filas2, n_columnas2, n_filas3, n_columnas3)) #linea2

#Hacerlo en 1 linea
#Revisar
#MatrizAntigua = np.arange(1,n_filas1*n_columnas1 * n_filas2*n_columnas2 * n_filas3*n_columnas3 + 1 ).reshape(MatrizAntigua,(n_filas1, n_columnas1, n_filas2, n_columnas2, n_filas3, n_columnas3))#linea 1

#Diccionario
# diccionario = {"Nombre" : "Marcell" , "edad": 20 }
# print(diccionario["Nombre"])
# es modificable
# diccionario["Gusto"] = "escuchar musica"
# diccionario = {"Nombre":"Marcell", "edad" : 20, "estudios": ["SMR","ESO"]}
# si queremos sacar un segundo valor de un diccionario se haria asi " print(diccionario.get("estudios")[1])"

# Claves = diccionario.keys()
#para imprimir lo que esta dentro se seguira lo siguiente (print(diccionario[estudios][0]))
#Los diccionarios sirven para hacer base de datos

# empleados = {
#     "empleado1": {"nombre": "Marcell", "Nota": -2}, #print(empleados["empleado1"]["Nota"]) para imprimir la nota
#     "empleado2": {"nombre": "Javi", "Nota": 1.5}
# }


# Conjuntos

# conjunto1 = {1, 2, 3} # set es conjunto
# conjunto2 = {3, 4, 5}
# interseccion = conjunto1.intersection(conjunto2)

# Booleanos se usan en sentencias condicionales 
# booleano = 5 > 3 
# hacer un condicional que clasifique un paquete de amazon
# 3 tipos de paquetes uno enviado urgente otro priroidad media y otro almacenar el paquete urgente si la fecha de entrega es < 2 dias y coste mayor de 100,
# 2 fecha entrega >=2 dias y coste > 100, 3 >=2 y coste >=100 o  fecha entrega <2 y  coste < 1


# if dias_restantes < 2 and coste >100:
#     return 'Urgente'
# elif dias_restantes >=2 and coste >100:
#     return 'Media'
# else: 
#     return 'Almacenar'

# fecha_entrega
#para calcularel cuadrado de algo se usa doble ** ejemplo radio**2
# Condicionales
# x = 20
# if x >10:
#     print(f"{x} es mayor que 10") #Se pone una f adelante porque formatea el texto, preguntarle a chatgpt
#     # ademas esto hace que imprima el valor de x
    
# elif x == 10:
#     print(f"{x} es igual que 10")
# else:
#     print(f"{x} es menor que 10")
# en una sola linea
# x = 5
# print(f"{x} es > que 5" if x>5 else f"{x} es menor o igual que 5")
# Condicionales y listas 
# colores = ["rojo", "azul" , "verde" , "amarillo"]
# color = "rojo"
# if color in colores:
#     print(f"El color {color} esta dentro de la lista {colores}")
# else:
#     print(f"El color {color} no esta dentro de la lista {colores}")

# colores = ["rojo", "rojo" , "rojo" , "amarillo"]

# contador_rojo = colores.count("rojo") 

# print(f"La palabra rojo aparece {contador_rojo} veces ")

# en una linea

#   print(f"La palabra rojo aparece {colores.count('rojo')} veces")


#switch-case --> match-case
# animal = "perro"
# match animal:
#     case = "gato":

# diccionario = {"Sebastian": 19, 
#                "Daniel": 21,
#                "Javier": 19,
#                "Manu": 26,
#                "Ana" : 30
#                }
# for persona in diccionario:
#     if diccionario[persona]>= 18:
#         print(f"{persona} es mayor de edad")
#     else:
#         print(f"{persona} es menor de edad")
#         #Ten cuidado con el orden
# #Si pones el else detras junto al for el else pertenecera al for y no al if siempre poner las cosas al mismo nivel

# ### all (y)y any (or) 
# x, y ,z = 5, 10, 15
# if all([x>0, y > 0, z > 0]):
#     print(f"Todos son mayores que 0")
# else:
#     print(f"Todos son menores que 0")
# if any([x > 0 ,y > 0 , z > 0]):
#     print(f"Al menos uno es positivo")
# %%4. Bucles

# frutas = ['manzana', 'cereza', 'platano' ]
# for fruta in frutas:
#     print(f"mi fruta es {fruta}")
# diccionario = {'d': 1, 'a':3, 'Sebastian': 4}
# for c in diccionario: #c = clave llaves
#     print(f"la clave es {c}")
# for valores in diccionario.values():  # valores = valores 
#     print(f"los valores son {valores}")   
    
# diccionario2={'Sebastian': {'Coche' : 'chevrolet'},
#               'Javier': {'Coche' : 'mercedes'},
#               'Manu': {'Coche' : 'Honda'}
#               }
# for nombre, detalles in diccionario2.items():
#     print(f"El coche de {nombre} es {detalles['Coche']}")

# diccionario2={'Sebastian': {'Coche' : {'Marca':'chevrolet', 'kms':100000}},
#               'Javier': {'Coche' : {'Marca':'mercedes', 'kms':200000}},
#               'Manu': {'Coche' : {'Marca':'honda', 'kms':300000}},
#               }

# for clave in diccionario2:
#     print(f"los kms del coche de {clave} son {diccionario2[clave]['Coche']['kms']}")
# for clave in diccionario:
#     print(f"la clave es {diccionario[clave]}")
# #Imprimir todo lo del diccionario
# n = [1,2,3,4,5]
# for numero in n:
#     if numero == 4:
#         continue
#     print(numero)
    


# Instrucciones especiales --> Break, continue

# lista = [x**2 for x in range (1, 6)]
# print(lista)

#diccionario que tuviera como clave un cuadrado de un numero 
#diccionario = {x: x**2 for x in range (1, 6)}

#Funcion zip python
# nombres = ["Sebastian" , "Javier" , "Manu"]
# edades = [19, 19, 26]
# for n, e in zip(nombres, edades):
#     print(f"la edad de {n} es {e} años")

# como funciona range
            # x     y  z
# for i in range(1 , 10 ,3): #x es donde empieza, y es donde termina, z es donde suma hasta llegar a y
#     print(i)
###############################################################################
                        # Variables modificables #
###############################################################################
#%% 5. Funciones en python
# def nombre (parametros):
#     """
#     Descripcion de lo que hace el metodo 
    
#     Explicacion Entradas: 
#                         -
#                         -
#                 Salidas:
#                         -
#                         -
#     """
    
#     # Chequeo de errores

# def saludar(nombre=None):
#     if nombre is None:
#         print(f"No hay argumento valido, hola desconocido")
#     else:
#         print(f"hola {nombre}") 

# saludar()
# saludar("Marcell")
    
# #importar una funcion de otra clase, lo guardas y ahora lo haces asi
# import funcionessuma as f
# a = 1
# b = 3
# print(f.suma(a, b)) 
# %% 6. Progamacion orientada a objetos

# class Coche:
    
#     def __init__(self, marca, modelo, color, cv):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.cv = cv
    
#     def describirCoche(self):
#        #estos mensajes antes no imprimian porque el return solo devolvia el mensaje mas
#        #no la instruccion al poner un print al lado podemos llamar al metodo de manera correcta
#         return print(f"Mi coche es un {self.marca} {self.modelo} de color {self.color} con {self.cv} CV")
    
#     def caballos(self):
#         return print(f"El coche tiene {self.cv} cv")
        
#     def cambiarColor(self, n_color):
#          self.color = n_color
# mi_coche = Coche("Honda", "Civic", "Azul", 140)  
# mi_coche.caballos()
# mi_coche.cambiarColor("rojo")
# mi_coche.describirCoche()

# # Herencia
# # Clase Padre --> Animal
# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre
        
#     def hablar(self):
#         return f"{self.nombre} hace x sonido"

# #Clase Hija --> Perro
# class Perro(Animal):
    
#     def hablar (self):
#         return f"{self.nombre} hace Guau"
#     def raza(self, raza):
#         self.raza = raza
#         return f"la raza de {self.nombre} es {self.raza}"

# mi_perro = Animal("Indio")
# print(mi_perro.hablar())
# mi_perro2 = Perro("Indio")
# print(mi_perro2.hablar())
# print(mi_perro2.raza())
    
#Composicion no existe el obeto

# class Tipo_motor:
#     def __init__(self,CV):
#         self.CV = CV

# class Coche:
#     def __init__(self, marca, modelo, CV):
#         self.marca = marca
#         self.modelo = modelo
#         self.CV = Tipo_motor(CV)
#     def detalles(self): 
#         return f"Es un {self.marca} modelo {self.modelo} con {self.CV.CV} CV" #Se hace un self.cv.cv por la composicion que hicimos con la clase motor y coche
    
# Coche1 = Coche("Ford", "SuperDuty", 400)
# print(Coche1.detalles())

#Agregacion 

# class Profesor:
#     def __init__(self, nombre):
#         self.nombre = nombre
        
# class Instituto :
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.profesores = []
        
#     def añadir_profesores (self,profesor):
#         self.profesores.append(profesor)
        
#     def mostrar_profesores(self):
#         for profesor in self.profesores:
#             print (profesor.nombre)

# #Se crea el instituto esta clase agrega a los profesores
# Instituto = Instituto ("Las Salinas - Tarde")
# profe1 = Profesor("Dani")
# profe2 = Profesor("Vicente")
# profe3 = Profesor("Manu")

# Instituto.añadir_profesores(profe1)
# Instituto.añadir_profesores(profe2)
# Instituto.añadir_profesores(profe3)

# Instituto.mostrar_profesores()


# Clases abstractas
#Tenemos que importar el modulo 
# from abc import ABC, abstractmethod
# #Clase padre
# class Animal (ABC):
    
#     @abstractmethod
#     def sonido(self):
#         pass #pasa al metodo de cada clase hija
        
#     def come(self):
#         return f"El animal esta comiendo"
# #Clases hijas    
# class Perro(Animal):
    
#     def info(self, nombre):
#         self.nombre = nombre
#         return f"El animal se llama {self.nombre}"
#     def sonido(self):
#         return f"Guau"         

# class Gato(Animal):
#     def saltar(self):
#         return f"el gato salta"
#     def Sonido(self):
#         return f"el gato hace Miau"

# perro = Perro()
# print(perro.sonido())
# print(perro.info("Indio"))


# %% 7. Variables y locales
#Variable global se define al principio y va a ser asi durante todo el programa
# x = 'global' #al estar fuera del codigo pasa a ser global
# # def ejemplo():
# #     x='local'
# #     print(x)
# # ejemplo() #Imprimira Local ya que dentro del metodo x tiene otro valor
# # print(x) #Imprimira el valor de la global



#CAMBIAR VARIABLE GLOBAL:
# x = 'Global'

# def cambiar_var_global():
#     global x
#     x = 'Global modificada'
#     print(x)

# cambiar_var_global()
# print (x)

#Modificar variable local

# def externa():
#     x = 'Externa'
    
#     def interna(): #Interna se encuentra dentro de externa 
#         nonlocal x 
#         x = 'Modificada Externa'
#         print (x)    
#     interna()
    
# externa()

#%% 8. Extraer y pedir informacion de ficheros, tratarla y devolverla 
# Modulo pandas ---> tratar, leer, escribir etc
# import pandas as pd
# Leer
# archivo = pd.read_csv('empleados.csv')
# print (f"Los datos de los empleados son: ", archivo)
# print(" ")
# print (f" Los nombres son: ", archivo['nombre']) #Acceder a columnas
# primer_empleado = archivo.loc [0]#Acceder a filas
# print(primer_empleado)
# print(" ")
# Acceder a un valor en concreto {SALARIO TERCER EMPLEADO}
# salario_tercer_empleado = archivo.loc[2, 'salario_mensual']
# print(f"El salario del tercer empleado es: {salario_tercer_empleado}")
# 2. Pedir informacion por pantalla y cargarla 
# nueva_fila = {
#     'nombre': 'Javier',
#     'edad': 19,
#     'id': 105,
#     'horas_trabajadas' : 20,
#     'tarifa_hora' : 20,
#     'salario_mensual' : None
#      }
# #Añadir --> append
# # df = archivo.append(nueva_fila)
# # print(df)
# nueva_fila_df = pd.DataFrame([nueva_fila])
# archivo = pd.concat([archivo, nueva_fila_df], ignore_index=True)
# #ignore_index=True: Esto asegura que se reinicien los índices, ya que estás añadiendo una nueva fila.
# print(archivo)
# Cargar informacion --> Pidiendosela al usuario
# from tkinter import Tk
# import pandas as pd
# from tkinter.filedialog import askopenfilename

# #Tk().withdraw()  

# #Pedimos al usuario que seleccione el archivo ".csv"

# file_path = askopenfilename(
#     title = 'Selecciona un archivo .csv',
#     filetypes = [("CSV files ",  "*.csv"), ("All files" , "*.*")])
    
# if file_path:
#     # Leer
#     df = pd.read_csv(file_path)
    
    
    
# else:
#     print("No has seleccionado ningun archivo")


# # 3. Crear un archivo y grabarlo
# import pandas as pd
# from tkinter import Tk
# from tkinter.filedialog import askdirectory
# import os # gestiona directorios en cualquier sistema operativo
# nombre_archivo = 'Empleados2.csv'
# #crear diccionario
# data = {
#         'nombre' : ['Sebastian' , 'Javier' , 'Manu' , 'Ivan'],
#         'edad' : [19,19,26,20],
#         'salario' : [None, 1650, 1799, 4000]}
# # Convertir a dataframe
# df = pd.DataFrame(data)
# # Seleccionar carpeta
# carpeta_select = askdirectory(title='Selecciona directorio')
# # Verificar seleccion
# if carpeta_select:
#     file_path = os.path.join(carpeta_select, nombre_archivo )
#     # Guardamos DataFrame
#     df.to_csv(file_path, index=False)
# %% 9. Conexion a Bases de Datos 
"""Relacionales ----> MYSQLO/POSTGRESQL"""
# # pip install mysql-connector-python
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd

# # Que necesitamos para una bdd: el host, database, user, password, port 

# # Funcion para conectar
# def connect_BD(host, database, user, password, port):
#     try:
#         connection = mysql.connector.connect(
#             host = host,
#             database = database,
#             user = user,
#             password = password,
#             port = port
#             )
#         if connection.is_connected():
#             print(f"La conexion ha sido realizada {database}")
#             return connection
#     except Error as e:
#             print(f"Error al conectarse: {e}")
#             return None

# # Funcion para leer    
# def read_BD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         # Peticion, Convertir la lista de columnas en cadena
#         columnas_str = ','.join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
#         # Ejecutamos la peticion
#         cursor.execute(query)
#         # Resultados 
#         resultados = cursor.fetchall()
#         # Obtener 
#         columna_resultado = [i[0] for i in cursor.description]
#         # Nos creamos el DataFrame
#         df = pd.DataFrame(resultados, columns = columna_resultado)
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
#         return None
        
# # Ejecutar
# if __name__ == '__main__':
#     # Parametros de conexion
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = '' # No requiere contraseña 
#     port = 4497
#     tabla = 'family' # Tabla a consultar
#     #Columnas que quieres extraer
#     columnas = ['rfam_acc', 'rfam_id', 'description']
#     limite_filas = 5 #Numero de filas que quieres extraer
#     #Conectar a la BD
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion:
#         # Leer 
#         df_BD = read_BD(connection, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()
        
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd

# # Función para conectar
# def connect_BD(host, database, user, password, port):
#     try:
#         connection = mysql.connector.connect(
#             host=host,
#             database=database,
#             user=user,
#             password=password,
#             port=port
#         )
#         if connection.is_connected():
#             print(f"La conexión ha sido realizada a {database}")
#             return connection
#     except Error as e:
#         print(f"Error al conectarse: {e}")
#         return None

# Función para leer    
# def read_BD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         # Petición, convertir la lista de columnas en cadena
#         columnas_str = ','.join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"  # Espacio corregido en LIMIT
#         # Ejecutamos la petición
#         cursor.execute(query)
#         # Resultados 
#         resultados = cursor.fetchall()
#         # Obtener nombres de las columnas
#         columna_resultado = [i[0] for i in cursor.description]
#         # Nos creamos el DataFrame
#         df = pd.DataFrame(resultados, columns=columna_resultado)  # Corregido a 'columns'
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
#         return None

# # Ejecutar
# if __name__ == '__main__':
#     # Parámetros de conexión
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = ''  # No requiere contraseña 
#     port = 4497
#     tabla = 'family'  # Tabla a consultar
#     # Columnas que quieres extraer
#     columnas = ['rfam_acc', 'rfam_id', 'description']
#     limite_filas = 5  # Número de filas que quieres extraer
#     # Conectar a la BD
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion:
#         # Leer
#         df_BD = read_BD(conexion, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()
# %% 10. Consumo y creacion de APIs
# import requests
# # url
# url = "https://pokeapi.co/api/v2/pokemon?limit=150"
# # Respuesta
# respuesta = requests.get(url)

# lista_pokemon = respuesta.json()["results"]

# for pokemon in lista_pokemon:
#     print(pokemon["name"])        

            
        
# conexion mongodb : mongodb+srv://marcellgonzalezappweb:<db_password>@trydust.7wkgf.mongodb.net/?retryWrites=true&w=majority&appName=Trydust    
"""
Bases de datos No Relacionales
"""
# Importar módulos
# import pymongo as mongo
# import pandas as pd

# # Conexión a MongoDB Atlas
# try:
#     cliente = mongo.MongoClient("mongodb+srv://marcellgonzalezappweb:Marcell2710@trydust.7wkgf.mongodb.net/?retryWrites=true&w=majority")
#     print("Conexión exitosa")
# except Exception as e:
#     print(f"Error en la conexión: {e}")
#     exit()

# # Seleccionar la base de datos y colección
# db = cliente["sample_mflix"]
# coleccion = db["movies"]

# # Realizar la consulta y manejar los posibles errores
# try:
#     resultados = coleccion.find().limit(10)  # Obtener hasta 10 documentos
#     lista_resultados = list(resultados)      # Convertir los resultados a una lista
#     if not lista_resultados:
#         print("No se han encontrado datos")
#     else:
#         print(f"Se han encontrado {len(lista_resultados)} documentos")

#     # Convertir la lista de resultados a un DataFrame de pandas
#     df = pd.DataFrame(lista_resultados)
#     print("DataFrame creado con éxito")
#     print(df.head())  # Mostrar las primeras filas del DataFrame

# except Exception as e:
#     print(f"Error al realizar la consulta: {e}")
# PVGIS
import requests
import json

url = f"https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"

# Parametros
params = {
    'lat' : 38.6759,
    'lon' :  4.159,
    'peakpower' :   1,
    'pvtechchoice' : 'crystSi',
    'loss' : 14,
    'outputformat' : 'json'
    }

#Realizar consulta
respuesta = requests.get(url,params = params)
data = json.loads(respuesta.text)


print(f"La energia estimada diara: {data['outputs']['totals']['fixed']['E_d']} kwh")