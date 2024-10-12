[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Andres Felipe Florez Henao
ID:  000540643
---

- **Título del Proyecto:** Colegio
- **Descripción Detallada:**
    
    Este problema consiste en que uno pueda llevar la actividad académica de los estudiantes en un colegio y tambien registrar los nuevos que lleguen cada año; esto es importante debido a que siempre se necesita llevar un soporte del estatus de los estudiantes dentro de la institución educativa en caso de querer actualizar datos como notas o tambien la consulta de estas, ademas, cada año llegan nuevos estudiantes y la institucion debe estar en la . El programa se va a encontrar en el archivo "Datos.py" en la carpeta "src" y tambien se recomienda ingresar al archivo "user guide", ahi se encuentra toda la informacion necesaria para que el usuario ejecute de manera adecuada el programa
    
- **Alcance:**

    el programa guardará el primer nombre, edad, ID institucional, periodo, notas y el grado de cada estudiante; el usuario podrá buscar tanto la información del estudiante por su ID o ver el estatus de todos los estudiantes en general, esto es necesario para los casos en que un estudiante desee revisar sus notas o sus datos en el sistema del colegio
- **Estructuras de Datos Utilizadas:**

    listas para llevar las notas del estudiante, diccionarios dentro de un diccionario que serviran para llevar los datos del estudiante.
- **Diagrama de Flujo o Pseudocódigo:**

        INICIO
        Variable control = Verdadero
        Mientras control sea Verdadero:
            imprimir mensaje de bienvenida y menú de opciones
            leer opción del usuario
            limpiar pantalla usando "system('cls')"

            Si opción es 1:
                Leer id del estudiante
                Llamar a función añadir_notas(id)       
                
                 // esta funcion sirve para agregar una nota de un estudiante por medio de un id

            sino si opción es 2:
                Leer nombre del nuevo estudiante
                Leer id del nuevo estudiante
                Leer edad del nuevo estudiante
                Leer periodo del nuevo estudiante
                Crear lista vacía notas
                Leer grado del nuevo estudiante
                Llamar a función registrar_estudiante(nombre, id, edad, periodo, notas, grado) 
                // esta funcion sirve para agregar un estudiante al diccionario por medio de un id

                Imprimir "Estudiante Registrado exitosamente"

            Sino si opción es 3:
                Imprimir diccionario estudiantes

            Sino si opción es 4:
                Leer id del estudiante que desea revisar
                Llamar a función buscar_estudiante(id)
                Imprimir valor retornado por buscar_estudiante

            Sino si opción es 5:
                Asignar control = Falso
                Imprimir "gracias, vuelva pronto"
                Terminar bucle
        FIN