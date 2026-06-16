estudiantes = [] 

def agregar_estudiante(id, nombre, edad, grupo): 
 estudiante = { 
"id": id, 
"nombre": nombre, 
"edad": edad, 
"grupo": grupo 
} 

 estudiantes.append(estudiante) 
 print("Estudiante agregado correctamente.") 


def mostrar_estudiantes(): 
    if len(estudiantes) == 0: 
        print("No hay estudiantes registrados.") 
    else: 
        for estudiante in estudiantes: 
            print(estudiante)

agregar_estudiante(1, "Ana", 16, "A") 
agregar_estudiante(2, "Luis", 17, "B") 
mostrar_estudiantes()

def buscar_estudiante(id): 
    for estudiante in estudiantes: 
        if estudiante["id"] == id: 
            return estudiante 
    return None

resultado = buscar_estudiante(1) 
if resultado: 
    print("Estudiante encontrado:") 
    print(resultado) 
else: 
    print("Estudiante no encontrado.")