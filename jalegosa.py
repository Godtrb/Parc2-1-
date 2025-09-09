import tkinter as tk
from tkinter import messagebox

CRITERIOS = ["cultura", "proyección", "entrevista"]
MUNICIPIOS = ["Almolonga", "Cabricán", "Cajolá", "Cantel", "Colomba", "Concepción Chiquirichapa",
              "El Palmar", "Flores Costa Cuca", "Génova", "Huitán", "La Esperanza", "Olintepeque", "Palestina de Los Altos",
              "Quetzaltenango", "San Francisco La Unión", "San Martín Sacatepéquez", "San Mateo", "San Miguel Sigüilá",
              "Sibilia", "Zunil"]
DATOS_RUTA_CANDIDATAS = "candidatas.txt"
DATOS_RUTA_JURADOS = "jurados.txt"
VALORES_PUNTAJE = [str(i) for i in range(0,11)]

class Persona:
    def __init__(self, dpi, nombre: str, edad: int):
        self.nombre = nombre.strip()
        self.edad = edad


    def mostrar_info(self):
        return  f"{self.nombre} - {self.edad}"

class Candidata(Persona):
    def __init__(self, dpi, nombre, edad, municipio, institución):
        super().__init__(dpi, nombre, edad) #Luis con esto heredamos de la clase padre
        self.municipio = municipio
        self.institucion = institución
        self.calificacion = []

    def agregar_calificacion(self, calificacion):
        self.calificacion.append(calificacion)

    def promedio(self):
        if not self.calificaciones:
            return  0
        for calificacion in self.calificaciones
            total = calificacion.total + calificacion
        return total / len(self.calificaciones)

class Jurado(Persona):
    def __init__(self, dpi, nombre, edad, especialidad, metodo):
        super().__init__(dpi, nombre, edad)
        self.especialidad = especialidad
        self.metodo = metodo


class ReinasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reinas de Independencia Xelafer 2025")
        self.ventana.geometry("500x300")
        self.ventana.config(bg="royal blue")

        self.menu()

        tk.Label(
            self.ventana,text="♕ BIENVENIDO ♕",
            font=("Goudy Old Style", 20, "bold"), bg="Royal blue", fg="red4", justify="center").pack(pady=10)
        tk.Label(
            self.ventana,text=" Sistema de Inscripción y Evaluación de Reinas de Independencia 2025 - Quetzaltenango",
            font=("Goudy Old Style", 20, "bold"), bg="Royal blue", fg="white", justify="center").pack(pady=10)
        try:
            self.foto = tk.PhotoImage(file="xelafer2025.gif")
            tk.Label(self.ventana, image=self.foto, bg="white smoke").pack(pady=1)
        except Exception as e:
            print("No se pudo cargar la imagen:", e)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana, bg="royal blue", fg="white", font=("Helvetica", 12))
        opciones = tk.Menu(barra, tearoff=0, bg="royal blue", fg="red4", font=("Helvetica", 12) )
        opciones.add_command(label="Registrar Reina", command=self.registrar_Reina)
        opciones.add_command(label="Registrar Jurado", command=self.registrar_Jurado)
        opciones.add_command(label="Registrar Calificación", command=self.registrar_calificacion)
        opciones.add_command(label="Listado de Reinas", command=self.listar_Reinas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones )
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