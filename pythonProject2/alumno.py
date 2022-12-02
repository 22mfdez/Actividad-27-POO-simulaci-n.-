class Alumno:
    def __init__ (self, id , nombre,  email):#constructor
        self.id=id#almacenar en la instancia el parámetro
        self.nombre=nombre
        self.email=email
    def info(self):
        print(f'Nombre: {self.nombre}, email: {self.email}')

alumno1=Alumno(1, 'Lucia', 'Luchi@gmail.com')
alumno2=Alumno(2, 'Asunción', 'asungeta@gmail.com')
alumno1.info()
alumno2.info()

