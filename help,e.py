import tkinter as tk
from idlelib.tree import wheel_event

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



class ReinasApp:
        def __init__(self):
            self.ventana = tk.Tk()
            self.ventana.title("Reinas Quetzaltenango 2025")
            self.ventana.geometry("500x300")
            self.ventana.config(bg="tomato")

            self.menu()

            tk.Label(
                self.ventana,
                text="Sistema de Inscripción y Evaluación de Reinas de Independencia 2025 - Quetzaltenango",
                font=("Arial", 12, "bold"),
                justify="center"
            ).pack(pady=50)

            self.ventana.mainloop()

        def menu(self):
            barra = tk.Menu(self.ventana)
            opciones = tk.Menu(barra, tearoff=0)
            opciones.add_command(label="Registrar Reina", command=self.registrar_Reina)
            opciones.add_command(label="Registrar Jurado", command=self.registrar_Jurado)
            opciones.add_command(label="Registrar Jurado", command=self.registrar_calificacion)
            opciones.add_command(label="Registrar Evaluacion", command=self.listar_Reinas)
            opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
            opciones.add_separator()
            opciones.add_command(label="Salir", command=self.ventana.quit)
            barra.add_cascade(label="Opciones", menu=opciones)
            self.ventana.config(menu=barra)

        def registrar_Reina(self):
            print("Se abrió la ventana: Registrar Reina")
            tk.Toplevel(self.ventana).title("Registrar Reina")

        def registrar_Jurado(self):
            print("Se abrió la ventana: Registro Jurado")
            tk.Toplevel(self.ventana).title("Registrar Jurado")

        def registrar_calificacion(self):
            print("Se abrió la ventana: Registrar Calificación")
            tk.Toplevel(self.ventana).title("Registrar Calificación")

        def listar_Reinas(self):
            print("Se abrió la ventana: Listar Reinas")
            tk.Toplevel(self.ventana).title("Listado de Reinas")

        def ver_ranking(self):
            print("Se abrió la ventana: Ranking Final")
            tk.Toplevel(self.ventana).title("Ranking Final")

if __name__ == "__main__":
        ReinasApp()