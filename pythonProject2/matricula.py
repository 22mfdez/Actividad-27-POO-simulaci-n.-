from curso import Curso
from alumno import Alumno

class Matricula:#clase, entidad, modelo
    def __init__(self, idmatricula, fechamatricula, idalumno, idcurso):#constructor
        self.idmatricula=idmatricula
        self.fechamatricula=fechamatricula
        self.idalumno=idalumno
        self.idcurso=idcurso
    def infoMatricula(self):#método de instancia
        print(f'El alumno/a {self.idalumno}, en el curso {self.idcurso}  se matriculó en la fecha{self.fechamatricula}')

alumno1=Alumno(1, 'Lucía', 'Luchi@gmail.com')
estudio1=Curso(1,'Veterinaria',504,4)
alumno2=Alumno(2, 'Asunción', 'asungeta@gmail.com')
estudio2=Curso(2,'Química',240,4)
alumno=Matricula(1, '01/12/2022', alumno1.nombre, estudio1.nombre)
alumno3=Matricula(2, '24/11/2022', alumno2.nombre, estudio1.nombre)
alumno4=Matricula(2, '15/11/2022', alumno2.nombre, estudio2.nombre)
alumno.infoMatricula()
alumno3.infoMatricula()
alumno4.infoMatricula()
