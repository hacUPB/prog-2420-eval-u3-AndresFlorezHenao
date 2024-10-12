from os import system
estudiantes={'pepe':{'nombre':'pepe', 'id':123, 'edad':12, 'periodo':1, 'Notas': [], 'grado' :3},
            'ana':{'nombre':'ana', 'id':456, 'edad':12, 'periodo':1, 'Notas': [], 'grado':5},
            'jeronimo':{'nombre':'jeronimo', 'id':789, 'edad':12, 'periodo':1, 'Notas': [], 'grado':3}
}
def añadir_notas(id:int):
    cont=1
    while cont==1:
        estudiante=buscar_estudiante(id)
        print("Bienvenido/a al directorio de", estudiante) 
        nota=float(input("ingrese una nota de 0 a 5: "))
        if nota<0 or nota>5:
            print("nota no valida")
            cont=cont
        else:
            for estudiante, di in estudiantes.items():
                if di['id'] == id:
                    y={di['Notas'].append(nota)}
                    print("nota registrada correctmente")
                    cont=cont-1
                    return nota
        
#Funcion para buscar un estudiante
def buscar_estudiante(id:int):
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
    estudiantes[nombre] = {
        'nombre': nombre,
        'id':id,
        'edad':edad,
        'periodo': periodo,
        'Notas': notas,
        'grado': grado
    }
    return
# Función para imprimir cada estudiante en renglones separados
def imprimir_estudiantes(estudiantes):
    for nombre, detalles in estudiantes.items():
        print(f"Estudiante: {nombre}")
        for atributo, valor in detalles.items():
            print(f"  {atributo}: {valor}")
        print()
        
def main():
    control=True #Variable de control para crear una lista en bucle
    while control==True:
        print(("bienvenido al colegio los angeles tunja, ¿Que opcion desea realizar?"
               "\n 1. Ingresar nota \n 2. ingresar nuevo estudiante"
               "\n 3. ver directorio de estudiantes \n 4. buscar estudiante \n 5. salir")) #entrega unas opciones para preguntar que desea el usuario
        opcion=int(input("ingrese su opción: ")) #el usuario ingresa su opcion
        system("cls")
        if opcion==1:
            id=int(input("ingrese el id del estudiante al que desea ingresar una nota: "))#aqui el usuario ingresa el ID del estudiante que desee revisar
            añadir_notas(id)
        elif opcion==2:
            nombre=input("ingrese el nombre del nuevo estudiante: ")
            id=int(input("ingrese el id del nuevo estudiante: ")) #aqui el usuario ingresa el ID del estudiante que desee revisar
            edad=input("ingrese la edad del nuevo estudiante: ")
            periodo=int(input("ingrese el periodo del nuevo estudiante:"))
            notas=[]
            grado=int(input("ingrese el grado del nuevo estudiante: "))
            registrar_estudiante(nombre, id, edad, periodo, notas, grado)
            print("Estudiante Registrado exitosamente")
        elif opcion==3:
            imprimir_estudiantes(estudiantes)
        elif opcion==4:
            id=int(input("ingrese el id del estudiante que desea revisar: "))
            buscar_estudiante(id)
        elif opcion==5:
            control=False
            print("sesion cerrada correctamente.\n vuelva pronto")
            break
if __name__ == "__main__":
    main()
