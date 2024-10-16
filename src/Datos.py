from os import system
estudiantes={'pepe':{'nombre':'pepe', 'id':123, 'edad':12, 'periodo':1, 'Notas': [], 'grado' :3}, 
            'ana':{'nombre':'ana', 'id':456, 'edad':12, 'periodo':1, 'Notas': [], 'grado':5},
            'jeronimo':{'nombre':'jeronimo', 'id':789, 'edad':12, 'periodo':1, 'Notas': [], 'grado':3}
}
def añadir_notas(id:int):
    """
    Esta función toma un parametro y añade una notas de punto flotante a una lista
    dentro de un diccionaro que se encuentra dentro de un diccionario. La funcion 
    usa un bucle while el cual se encarga de hacer valida una nota para ingresarla al 
    sistema, luego de verificar la nota ingresada la funcion guarda la nota en la
    lista que se encuentra en el subdiccionario del estudiante elegido.

    Parámetros:
    id -- parámetro
    
    """
    cont=1          
    while cont == 1:
        estudiante=buscar_estudiante(id)
        print("Bienvenido/a al directorio de", estudiante) 
        nota=float(input("ingrese una nota de 0 a 5: "))
        if nota < 0 or nota>  5:
            print("nota no valida")
            cont = cont
        else:
            for estudiante, di in estudiantes.items():
                if di['id'] == id:
                    y={di['Notas'].append(nota)}
                    print("nota registrada correctmente")
                    cont = cont-1
                    return nota
        
#Funcion para buscar un estudiante
def buscar_estudiante(id:int):
    """
    Esta función toma un parametro y busca la informacion de un estudiante con su id

    Parámetros:
    id -- parámetro
    
    """
    for estudiante,di in estudiantes.items():
        if di['id'] == id:
            print(
    f"Los datos del estudiante son:\n"
    f" Nombre: {di['nombre']},\n"
    f" id: {di['id']},\n"
    f" Edad: {di['edad']},\n"
    f" periodo: {di['periodo']},\n"
    f" Notas: {di['Notas']},\n"
    f" Grado: {di['grado']}"
)
            return estudiante
    print(f"Persona con id '{id}' no encontrada.")

#Funcion para registrar un estudiante
def registrar_estudiante(nombre, id, edad, periodo, notas, grado):
    """
    Esta función toma seis parametros y crea un nuevo subdiccionario en el
    diccionario general con la informacion suministrada por el usuario los 
    cuales son los parametros

    Parámetros:
    nombre -- parámetro 1
    id -- parámetro 2
    edad -- parámetro 3
    periodo -- parámetro 4
    notas -- parámetro 5
    grado -- parametro 6
    
    """
    estudiantes[nombre] = {
        'nombre': nombre,
        'id': id,
        'edad': edad,
        'periodo': periodo,
        'Notas': notas,
        'grado': grado
    }
    return
# Función para imprimir cada estudiante en renglones separados
def imprimir_estudiantes(estudiantes):
    """
    Esta función toma un parametro y esta funcin lo que busca es imprimir de manera
    ordenada la informacion de los estudiantes para que le sea mas sencillo de
    entender al usuario

    Parámetros:
    estudiantes -- parámetro
    """
    for nombre, detalles in estudiantes.items():
        print(f"Estudiante: {nombre}")
        for atributo, valor in detalles.items():
            print(f"{atributo}: {valor}")
        print()
        
def main():
     #Variable de control para crear una lista en bucle
    control=True
    
     #bucle while para generar un menú en bucle
    while control:
        
        #entrega unas opciones para preguntar que desea el usuario
        print(("bienvenido al colegio los angeles tunja, ¿Que opcion desea realizar?"
               "\n 1. Ingresar nota \n 2. ingresar nuevo estudiante"
               "\n 3. ver directorio de estudiantes \n 4. buscar estudiante \n 5. salir")) 
        opcion=int(input("ingrese su opción: ")) #el usuario ingresa su opcion
        system("cls") #Borra de la terminal lo anterior
        
        #condicionales para accreder a las funciones del programa
        if opcion == 1:
            
            #el usuario ingresa el parametro de la funcion (ID)
            id=int(input("ingrese el id del estudiante al que desea ingresar una nota: "))
            añadir_notas(id) #ejecuta funcion
        elif opcion == 2:
            
            #Datos para agregar estudiante siendo parametros de la funcion 
            nombre=input("ingrese el nombre del nuevo estudiante: ")
            id=int(input("ingrese el id del nuevo estudiante: "))
            edad=input("ingrese la edad del nuevo estudiante: ")
            periodo=int(input("ingrese el periodo del nuevo estudiante:"))
            notas=[]
            grado=int(input("ingrese el grado del nuevo estudiante: "))
            registrar_estudiante(nombre, id, edad, periodo, notas, grado) #ejecuta funcion
            print("Estudiante Registrado exitosamente")
        elif opcion == 3:
            imprimir_estudiantes(estudiantes) #ejecuta funcion
        elif opcion == 4:
            
            #ingresa el Id (parametro de la funcion)
            id=int(input("ingrese el id del estudiante que desea revisar: "))
            buscar_estudiante(id) #ejecuta funcion
        #finalizacion del menu bucle con la opcion 5
        elif opcion == 5:
            control = False
            print("sesion cerrada correctamente.\nvuelva pronto")
            break
if __name__ == "__main__":
    main()
