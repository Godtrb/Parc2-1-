import tkinter as tk

class Persona:
    def __init__(self, dpi, nombre, edad):
        self.personas[dpi]={
            'nombre': nombre,
            'edad': edad,
        }


class Candidata(Persona):
    def __init__(self, dpi, nombre, edad, municipio, institucion):
        self.Candidatos[dpi]={
            'nombre': nombre,
            'edad': edad,
            'municipio': municipio,
            'institucion': institucion,
            'calificaciones': []
        }

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def promedio(self):
        if not self.calificaciones:
            return 0
        for calificacion in self.calificaciones:
            total = calificacion.total + calificacion
        return total / len(self.calificaciones)


class Jurado(Persona):
    def __init__(self, dpi, nombre, edad, especialidad,metodo):
        self.Candidatos[dpi]={
            'nombre': nombre,
            'edad': edad,
            'especialidad': especialidad,
            'metodo': metodo
        }



class Calificacion:
    def __init__(self, cultura, proyeccion, entrevista):
        self.calificaciones={
            'cultura': cultura,
            'proyeccion': proyeccion,
            'entrevista': entrevista
        }

    def total(self):
        return (self.cultura + self.proyeccion + self.entrevista) / 3


class Concurso:
    def __init__(self):
        self.candidatas = []
        self.jurados = []

    def registrar_candidata(self, candidata):
        self.candidatas.append(candidata)

    def registrar_jurado(self, jurado):
        self.jurados.append(jurado)

    def ranking(self):
        ranking = sorted(self.candidatas, key=lambda c: c.promedio(), reverse=True)
        return ranking