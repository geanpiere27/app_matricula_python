"""
- registrar alumnos. 
- generar fichas de matriuclas.
- mostar la lista de todos los matriculados. 
- filtrar matriculas por programa de estudio.
"""

# lista_alumnos=[]
# Inicio  del problema
# Necesito poner mas alumnos sin necesidad de crear tantas variables
# Posible solucion del problema crear con while un ciclo
# nombre=input("Ingrese el nombre del alumno:")
# apellido=input("Ingrese el apellido del alumno:")
# lista_alumnos.append(nombre)
# lista_alumnos.append(apellido)
# alumno={}
# Fin del problema
# Deseo mostrar un  
# print(lista_alumnos)

# Inicializar lista de alumnos
#lista_alumnos = []

# Función para registrar alumnos
#def registrar_alumno():
#    Id = len(lista_alumnos)+1
#    cui = int(input("Ingrese su numero de DNI: "))
#    nombre = input("Ingrese el nombre del alumno: ")
#    apellido = input("Ingrese el apellido del alumno: ")
#    programa = input("Ingrese el programa de estudio del alumno: ")
#    numero_celular = int(input("Ingrese sun numero de celular: "))
#    email = input("ingrese su correo electronico: ")
#    ciclo_academico = input("Ingrese su ciclo academico: ")
#    alumno = {
#        "Id": Id,
#        "cui": cui,
#        "nombre": nombre,
#        "apellido": apellido,
#        "programa": programa,
#        "numero_celular": numero_celular,
#        "email": email,
#        "ciclo_academico": ciclo_academico 
#    }
    
#    lista_alumnos.append(alumno)
#    print("Alumno registrado exitosamente.")

# Función para mostrar lista de alumnos
#def mostrar_alumnos():
#    print("Lista de alumnos:")
#    for i, alumno in enumerate(lista_alumnos):
#        print(f"{i+1}. {alumno['nombre']} {alumno['apellido']} - {alumno['programa']}")

# Función para filtrar alumnos por programa de estudio
#def filtrar_alumnos():
#    programa = input("Ingrese el programa de estudio para filtrar: ")
#    alumnos_filtrados = [alumno for alumno in lista_alumnos if alumno['programa'] == programa]
    
#    if alumnos_filtrados:
#        print("Alumnos filtrados:")
#        for i, alumno in enumerate(alumnos_filtrados):
#            print(f"{i+1}. {alumno['nombre']} {alumno['apellido']}")
#    else:
#        print("No se encontraron alumnos con ese programa de estudio.")

# Menú principal
#while True:
#    print("\nMenú")
#    print("1. Registrar alumno")
#    print("2. Mostrar lista de alumnos")
#    print("3. Filtrar alumnos por programa de estudio")
#    print("4. Salir")
    
#    opcion = input("Ingrese su opción: ")
    
#    if opcion == "1":
#        registrar_alumno()
#    elif opcion == "2":
#        mostrar_alumnos()
#    elif opcion == "3":
#        filtrar_alumnos()
#    elif opcion == "4":
#        print("Hasta luego.")
#        break
#    else:
#        print("Opción inválida. Por favor, intente de nuevo.")

# Este código te permite:

#1. Registrar alumnos de manera dinámica.
#2. Mostrar la lista de todos los alumnos.
#3. Filtrar alumnos por programa de estudio.
#4. Salir del programa.

##  TAREA HECHA EN CLASES

lista_alumnos= []

def mensaje_opciones():
    menu_opciones="""
    ------BIENVENIDO AL SISTEMA------
    ---Registra tu alumno---
    1. Escribe (s) si deseas agregar un nuevo alumno 
    2. Escribe (n) si deseas salir del sistema
    Escribe la accion que deseas realizar: """
    return menu_opciones

def ingreso_datos_alumnos():
    Id = len(lista_alumnos)+1
    cui = int(input("Ingrese su numero de DNI: "))
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    programa = input("Ingrese el programa de estudio del alumno: ")
    numero_celular = int(input("Ingrese sun numero de celular: "))
    email = input("ingrese su correo electronico: ")
    ciclo_academico = input("Ingrese su ciclo academico: ")
    guardar_datos_alumnos(Id,cui,nombre,apellido,programa,numero_celular,email,ciclo_academico)

def guardar_datos_alumnos(Id,cui,nombre,apellido,programa,numero_celular,email,ciclo_academico):
    alumno = {
        "Id": Id,
        "cui": cui,
        "nombre": nombre,
        "apellido": apellido,
        "programa": programa,
        "numero_celular": numero_celular,
        "email": email,
        "ciclo_academico": ciclo_academico 
    }
    lista_alumnos.append(alumno)

while "true":
    menu_opciones=input(mensaje_opciones())
    if menu_opciones.lower() == "n":
        print("Saliendo del sistema")
        break
    elif menu_opciones.lower() == "s":
        ingreso_datos_alumnos()
    else:
        print("Opcion erronea")

print(lista_alumnos)

        
         