class Curso:#clase, entidad, modelo
    def __init__ (self, id , nombre,  creditos, añosdeestudio):
        self.id=id#almacenar en la instancia el parámetro
        self.nombre=nombre
        self.creditos=creditos
        self.añosdeestudio=añosdeestudio
    def infocurso(self):
        print(f'Nombre: {self.nombre}, creditos obtenidos: {self.creditos} Años que lleva estudiando: {self.añosdeestudio}')

estudio1=Curso(1,'Veterinaria',504,4)
estudio2=Curso(1,'Química',200,4)
estudio1.infocurso()
estudio2.infocurso()