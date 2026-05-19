class Paciente:
    def __init__(self,idPaciente,nombre,edad,genero,historialMedico):
        self.id_paciente=idPaciente
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.historial_medico=historialMedico

    def mostrarDatos(self):
        return f"""
ID: {self.id_paciente}
Nombre: {self.nombre}
Edad: {self.edad}
Genero: {self.genero}
Historial: {self.historial_medico}
"""

class consulta:
    def __init__(self, idConsulta, idPaciente, fecha, sintomas, diagnostico, tratamiento):
        self.id_consutla= idConsulta
        self.id_paciente=idPaciente
        self.fecha=fecha
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.tratamiento=tratamiento

    def generarReceta(self):
        return f"""
Diagnostico: {self.diagnostico}

Tratamiento:
{self.tratamiento}
"""