class Contacto:
    _id_counter = 1

    def __init__(self, id,nombre, telefono, email):    
        self.id = Contacto._id_counter
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        Contacto._id_counter += 1

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Telefono: {self.telefono}, E-Mail: {self.email} '   
