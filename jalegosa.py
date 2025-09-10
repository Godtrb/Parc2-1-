import os.path
import tkinter as tk
from tkinter import messagebox, ttk


CRITERIOS = ["cultura", "proyección", "entrevista"]
DATOS_RUTA_CANDIDATAS = "candidatas.txt"
DATOS_RUTA_JURADOS = "jurados.txt"
VALORES_CALIFICACION = [str(i) for i in range(0,11)]

class Persona:
    def __init__(self, dpi, nombre, edad):
        self.dpi = dpi
        self.nombre = nombre.strip()
        self.edad = edad

class Candidata(Persona):
    def __init__(self, dpi, nombre, edad, municipio, institucion):
        super().__init__(dpi, nombre, edad) #Luis con esto heredamos de la clase padre
        self._municipio = municipio
        self.institucion = institucion.strip()
        self.calificaciones = []


    def agregar_calificacion(self, calificacion):
        for c in self.calificaciones:
            if c['jurado'] == calificacion['jurado']:
                return False
        self.calificaciones.append(calificacion)
        return True

    def promedio(self):
        if not self.calificaciones:
            return  0
        return sum((c['cultura'] + c['proyeccion'] + c['entrevista'])/3 for c in self.calificaciones)/len(self.calificaciones)

class Jurado(Persona):
    def __init__(self, dpi, nombre, edad, especialidad, metodo):
        super().__init__(dpi, nombre, edad)
        self.especialidad = especialidad
        self.metodo = metodo
        
"""class Calificacion:
    def __init__(self, cultura, proyeccion, entrevista):
        self.cultura = cultura
        self.proyeccion = proyeccion
        self.entrevista = entrevista

    def total(self):
        return (self.cultura + self.proyeccion + self.entrevista) / 3
"""
class Concurso:
    def __init__(self):
        self.candidatas = {}
        self.jurados = {}
        self.cargar_candidatas()
        self.cargar_jurados()

    def cargar_candidatas(self):
        if os.path.exists("candidatas.txt"):
            with open("candidatas.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(":")
                        if len(partes) >=5:
                            dpi, nombre, edad, municipio, institucion = partes[:5]
                            candidata = candidata(dpi, nombre, int(edad), municipio, institucion)
                            if len(partes)>5:
                                califs = partes[5].split(";")
                                for c in califs:
                                    if c:
                                        valores = c.split(",")
                                        if len(valores)==5:
                                            cal = {'cultura': int(valores[0]),
                                                   'proyeccion': int(valores[1]),
                                                   'entrevista': int(valores[2]),
                                                   'jurado': int(valores[3]),
                                                   'metodo': int(valores[4]),
                                                   }
                                            candidata.calificaciones.append(cal)
                            self.candidatas[dpi] = candidata

    def guardar_candidatas(self):
        with open("candidatas.txt", "w", encoding="utf-8") as f:
            for c in self.candidatas.values():
                califs_str = ";".join([f"{cal['cultura']}, {cal['proyeccion']}, {cal['entrevista']}, {cal['jurado']}, {cal['metodo']}" for cal in c.calificaciones])
                f.write(f"{c.dpi}:{c.nombre}:{c.edad}:{c.municipio}:{c.institucion}:{califs_str}\n ")

    def cargar_jurados(self):
        if os.path.exists("jurados.txt"):
            with open("jurados.txt", "r", encoding="utf-8") as  f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(":")
                        if len(partes)==5:
                            dpi, nombre, edad, especialidad, metodo = partes
                            self.jurados[dpi] = Jurado(dpi, nombre, int(edad), especialidad, metodo)

    def guardar_jurados(self):
        with open("jurados.txt", "w", encoding = "utf-8") as f:
            for j in self.jurados.values():
                f.write(f"{j.dpi}:{j.nombre}:{j.edad}:{j.especialidad}:{j.metodo}\n")

    def registrar_candidata(self, candidata):
        if candidata.dpi in self.candidatas:
            messagebox.showwarning("Error", f"La candidata ya está registrada")
            return  False
        self.candidatas[candidata.dpi] = candidata
        self.guardar_candidatas()
        return True

    def registrar_jurado(self, jurado):
        if jurado.dpi in self.jurados:
            messagebox.showwarning("Error", f"Ya es miembro del Jurado Calificador")
        self.jurados[jurado.dpi] = jurado
        self.guardar_jurados()
        return True

    def ranking(self):
        def quick_sort(lista):
            if len(lista) <=1:
                return lista
            pivote = [0]
            menores = [x for x in lista [1:] if x.promedio() <= pivote.promedio()]
            mayores = [x for x in lista[1:] if x.promedio()> pivote.promedio()]
            return quick_sort(mayores) + [pivote] + quick_sort(menores)
        ordenadas = quick_sort(list(self.candidatas.values()))
        return  ordenadas[:4]

class ReinasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reinas de Independencia Xelafer 2025")
        self.ventana.geometry("500x300")
        self.ventana.config(bg="royal blue")
        self.concurso = Concurso()
        self.municipios = ["Almolonga", "Cabricán", "Cajolá", "Cantel", "Colomba", "Concepción Chiquirichapa",
              "El Palmar", "Flores Costa Cuca", "Génova", "Huitán", "La Esperanza", "Olintepeque", "Palestina de Los Altos",
              "Quetzaltenango", "San Francisco La Unión", "San Martín Sacatepéquez", "San Mateo", "San Miguel Sigüilá",
              "Sibilia", "Zunil"]


        self.menu()

        tk.Label(
            self.ventana,text="♕ BIENVENIDO ♕",
            font=("Goudy Old Style", 35, "bold"), bg="Royal blue", fg="red4", justify="center").pack(pady=10)
        tk.Label(
            self.ventana,text=" Sistema de Inscripción y Evaluación de Reinas de Independencia 2025 - Quetzaltenango",
            font=("Goudy Old Style", 25, "bold"), bg="Royal blue", fg="white", justify="center").pack(pady=10)
        tk.Label(
            self.ventana, text="Bases de Inscripción:\n 1. Las señoritas participantes deben ser originarias del departamento de Quetzaltenango \n "
                               "2. Estar comprendidas entre los 18 y 23 años de edad \n 3. Estatura mínima 1.65 \n 4. Ser de reconocida honorabilidad \n"
                               "5. Ser soltera, no haber procreado hijos y no haber tenido una unión de hecho \n 6. Tener facilidad de palabra, ser extrovertida, dinámica y con proyección social",
            font=("Stencil Std", 12, "bold"), bg="royal blue", fg="white", justify="center").pack(pady=10)

        try:
            self.foto = tk.PhotoImage(file="xelafer2025.gif")
            tk.Label(self.ventana, image=self.foto, bg="white smoke").pack(pady=1)
        except Exception as e:
            print("No se pudo cargar la imagen:", e)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana, bg="blue", fg="white", font=("Helvetica", 12, "bold"))
        opciones = tk.Menu(barra, tearoff=0, bg="red4", fg="white", font=("Helvetica", 12, "bold") )
        opciones.add_command(label="Registrar Candidata", command=self.registrar_candidata)
        opciones.add_command(label="Registrar Jurado", command=self.registrar_jurado)
        opciones.add_command(label="Registrar Calificación", command=self.registrar_calificacion)
        opciones.add_command(label="Listado de Reinas", command=self.listar_candidatas)
        opciones.add_command(label="Listado de Jurados", command=self.listar_jurados)
        opciones.add_command(label="Ver Calificaciones", command=self.mostrar_calificaciones)
        opciones.add_command(label="Ver Ranking", command=self.mostrar_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones )
        self.ventana.config(menu=barra)

    def registrar_candidata(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Candidata")
        ventana.config(bg="burlywood1")


        tk.Label(ventana, text="Código:", font = ("Stencil Std", 12, "bold"), bg = "royal blue", fg = "white", justify = "center").pack(pady=2)
        dpi = tk.Entry(ventana);
        dpi.pack(pady=2)
        tk.Label(ventana, text="Nombre:").pack(pady=2)
        nombre = tk.Entry(ventana);
        nombre.pack(pady=2)
        tk.Label(ventana, text="Edad:").pack(pady=2)
        edad = tk.Entry(ventana);
        edad.pack(pady=2)
        tk.Label(ventana, text="Municipio:").pack(pady=2)
        municipio = ttk.Combobox(ventana, values=self.municipios);
        municipio.pack(pady=2)
        tk.Label(ventana, text="Institución:").pack(pady=2)
        institucion = tk.Entry(ventana);
        institucion.pack(pady=2)

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