import contacto

contactos = []

#opcion (C) Crear Nuevo Contacto
def crearContacto():  
    print("\n*** Crear Nuevo Contacto ***")  
    nombre = input("\nIngrese Nombre de Contacto: ")
    telefono = input("Ingrese Telefono de Contacto: ")
    email = input("Ingrese E-Mail de Contacto: ") 
    
    nuevoContato = contacto.Contacto(id, nombre, telefono, email)
    contactos.append(nuevoContato) 
    print(f'Contacto, {nombre} creado exitosamente!!')  


#opcion (R) Leer Lista de Contactos
def leerContactos():    
    print("=== LISTA DE CONTACTOS ===")
    if contactos:
        for c in contactos:
            print(c)
    else:
        print("No hay contactos registrados...")    


# #opcion (U) Actualizar Contacto
def actualizarContacto(contactos):
    print("\n*** Actualizar Contacto ***")
    idContacto = int(input("Ingrese ID de Contacto para Actualizar: "))
    
    for c in contactos:
        if c.id == idContacto:
            nombre = input("\nIngrese Nombre de Contacto: ")
            telefono = input("Ingrese Telefono de Contacto: ")
            email = input("Ingrese E-Mail de Contacto: ")

            if nombre:
                c.nombre = nombre
            if telefono:
                c.telefono = telefono
            if email:
                c.email = email

            print(f"Contacto {nombre} actualizado con éxito.")
            return
        
    print(f"Contacto con ID {idContacto} no encontrado.")  



#opcion (D) Eliminar contacto por ID
def eliminarContacto(contactos):
    print("*** Eliminar Contacto ***")
    idContacto = int(input("\nIngrese ID de Contacto para Eliminar: "))

    for i, c in enumerate(contactos):
        if c.id == idContacto:
            contactos.pop(i)
            print(f"Contacto con ID {c.id} eliminado con éxito.")
        return
            
    print(f"Contacto con ID {idContacto} no encontrado.")        


#menu principal
def menu():
    while True:
        print("\n*** AGENDA DE CONTACTOS ***")
        print("\n(C) Crear Nuevo Contacto")
        print("(R) Leer Lista de Contactos")
        print("(U) Actualizar Contacto")
        print("(D) Eliminar Contacto")
        print("(X) Salir.")

        opcion = input("\nIngrese la opcion: ")

        match (opcion.upper()):
            case "C":                 
                crearContacto()
            case "R":                
                leerContactos()
            case "U":                              
                leerContactos()                
                actualizarContacto(contactos)
            case "D":
                leerContactos()  
                eliminarContacto(contactos)
            case "X":
                print("\nFin del Programa...") 
                break
            case _:
                print("\nIngrese una Opcion Valida !!")                   

menu()  