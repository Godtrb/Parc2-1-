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
        self.municipio = municipio
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
                        if len(partes) >= 5:
                            dpi, nombre, edad, municipio, institucion = partes[:5]
                            candidata_obj = Candidata(dpi, nombre, int(edad), municipio, institucion)

                            if len(partes) > 5:
                                califs = partes[5].split(";")
                                for c in califs:
                                    if c:
                                        valores = c.split(",")
                                        if len(valores) == 5:
                                            cal = {
                                                'cultura': int(valores[0]),
                                                'proyeccion': int(valores[1]),
                                                'entrevista': int(valores[2]),
                                                'jurado': valores[3].strip(),
                                                'metodo': valores[4].strip()
                                            }
                                            candidata_obj.calificaciones.append(cal)
                            self.candidatas[dpi] = candidata_obj
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
            if len(lista) <= 1:
                return lista
            pivote = lista[0]
            menores = [x for x in lista[1:] if x.promedio() <= pivote.promedio()]
            mayores = [x for x in lista[1:] if x.promedio() > pivote.promedio()]
            return quick_sort(mayores) + [pivote] + quick_sort(menores)

        ordenadas = quick_sort(list(self.candidatas.values()))
        return ordenadas[:4]

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


        tk.Label(ventana, text="DPI:", font = ("Helvetica", 16, "bold"), bg = "burlywood1", fg = "white", justify = "center").pack(pady=2)
        dpi = tk.Entry(ventana);
        dpi.pack(pady=2)
        tk.Label(ventana, text="Nombre:", font = ("Helvetica", 16, "bold"), bg = "burlywood1", fg = "white", justify = "center").pack(pady=2)
        nombre = tk.Entry(ventana);
        nombre.pack(pady=2)
        tk.Label(ventana, text="Edad:", font = ("Helvetica", 16, "bold"), bg = "burlywood1", fg = "white", justify = "center").pack(pady=2)
        edad = tk.Entry(ventana);
        edad.pack(pady=2)
        tk.Label(ventana, text="Municipio:", font = ("Helvetica", 16, "bold"), bg = "burlywood1", fg = "white", justify = "center").pack(pady=2)
        municipio = ttk.Combobox(ventana, values=self.municipios);
        municipio.pack(pady=2)
        tk.Label(ventana, text="Institución:", font = ("Helvetica", 16, "bold"), bg = "burlywood1", fg = "white", justify = "center").pack(pady=2)
        institucion = tk.Entry(ventana);
        institucion.pack(pady=2)


        def guardar():
            if not dpi.get() or not nombre.get() or not edad.get() or not municipio.get() or not institucion.get():
                messagebox.showwarning("Atención", "Todos los campos son obligatorios")
                return
            if nombre.get().isdigit():
                messagebox.showwarning("Atención", "El nombre no puede ser un número")
                return
            try:
                edad_val = int(edad.get())
            except:
                messagebox.showwarning("Atención", "Edad debe ser numérica")
                return
            if edad_val < 18 or edad_val > 23:
                messagebox.showwarning("Atención", "La edad debe estar entre 18 y 23 años")
                return
            candidata = Candidata(dpi.get(), nombre.get(), edad_val, municipio.get(), institucion.get())
            if self.concurso.registrar_candidata(candidata):
                messagebox.showinfo("Éxito", "Candidata registrada correctamente")
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
        tk.Button(ventana, text="Cancelar", command=ventana.destroy).pack(pady=5)
        try:
            self.foto = tk.PhotoImage(file="reina.gif")
            tk.Label(ventana, image=self.foto, bg="burlywood1").pack(side="right", padx=10, pady=10)
        except Exception as e:
            print("No se pudo cargar la imagen:", e)

    def registrar_jurado(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Jurado")
        ventana.config(bg="LightBlue3")

        tk.Label(ventana, text="DPI:").pack(pady=2)
        dpi = tk.Entry(ventana);
        dpi.pack(pady=2)
        tk.Label(ventana, text="Nombre:").pack(pady=2)
        nombre = tk.Entry(ventana);
        nombre.pack(pady=2)
        tk.Label(ventana, text="Edad:").pack(pady=2)
        edad = tk.Entry(ventana);
        edad.pack(pady=2)
        tk.Label(ventana, text="Especialidad:").pack(pady=2)
        especialidad = tk.Entry(ventana);
        especialidad.pack(pady=2)
        tk.Label(ventana, text="Método:").pack(pady=2)
        metodo = tk.Entry(ventana);
        metodo.pack(pady=2)

        def guardar():
            if not dpi.get() or not nombre.get() or not edad.get() or not especialidad.get() or not metodo.get():
                messagebox.showwarning("Atención", "Todos los campos son obligatorios")
                return
            if nombre.get().isdigit():
                messagebox.showwarning("Atención", "El nombre no puede ser un número")
                return
            try:
                edad_val = int(edad.get())
            except:
                messagebox.showwarning("Atención", "Edad debe ser numérica")
                return
            jurado = Jurado(dpi.get(), nombre.get(), edad_val, especialidad.get(), metodo.get())
            if self.concurso.registrar_jurado(jurado):
                messagebox.showinfo("Éxito", "Jurado registrado correctamente")
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
        tk.Button(ventana, text="Cancelar", command=ventana.destroy).pack(pady=5)

    def registrar_calificacion(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Calificación")
        ventana.config(bg="snow")

        tk.Label(ventana, text="Candidata:").pack(pady=2)
        candidata_combo = ttk.Combobox(ventana, values=[c.nombre for c in self.concurso.candidatas.values()])
        candidata_combo.pack(pady=2)

        tk.Label(ventana, text="Jurado:").pack(pady=2)
        jurado_combo = ttk.Combobox(ventana, values=[j.nombre for j in self.concurso.jurados.values()])
        jurado_combo.pack(pady=2)

        tk.Label(ventana, text="Cultura:").pack(pady=2)
        cultura = ttk.Combobox(ventana, values=[str(i) for i in range(1, 11)], state="readonly")
        cultura.pack(pady=2)

        tk.Label(ventana, text="Proyección:").pack(pady=2)
        proyeccion = ttk.Combobox(ventana, values=[str(i) for i in range(1, 11)], state="readonly")
        proyeccion.pack(pady=2)

        tk.Label(ventana, text="Entrevista:").pack(pady=2)
        entrevista = ttk.Combobox(ventana, values=[str(i) for i in range(1, 11)], state="readonly")
        entrevista.pack(pady=2)

        def guardar():
            if not candidata_combo.get() or not jurado_combo.get() or not cultura.get() or not proyeccion.get() or not entrevista.get():
                messagebox.showwarning("Atención", "Todos los campos son obligatorios")
                return
            try:
                cultura_val = int(cultura.get())
                proy_val = int(proyeccion.get())
                ent_val = int(entrevista.get())
            except:
                messagebox.showwarning("Atención", "Las calificaciones deben ser numéricas")
                return

            candidata = next((c for c in self.concurso.candidatas.values() if c.nombre == candidata_combo.get()), None)
            jurado = next((j for j in self.concurso.jurados.values() if j.nombre == jurado_combo.get()), None)

            if not candidata or not jurado:
                messagebox.showwarning("Atención", "Seleccione datos válidos")
                return

            calificacion = {
                'cultura': cultura_val,
                'proyeccion': proy_val,
                'entrevista': ent_val,
                'jurado': jurado.nombre,
                'metodo': jurado.metodo
            }

            if candidata.agregar_calificacion(calificacion):
                self.concurso.guardar_candidatas()
                messagebox.showinfo("Éxito", "Calificación registrada correctamente")
                ventana.destroy()
            else:
                messagebox.showwarning("Atención", f"El jurado {jurado.nombre} ya calificó a esta candidata")

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
        tk.Button(ventana, text="Cancelar", command=ventana.destroy).pack(pady=5)

    def mostrar_ranking(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Ranking")
        ventana.config(bg="MistyRose2")

        ranking = self.concurso.ranking()
        posiciones = ["Ganadora", "Primera Finalista", "Segunda Finalista", "Tercera Finalista"]

        for i, candidata in enumerate(ranking):
            tk.Label(ventana, text=f"{posiciones[i]}: {candidata.nombre} - Promedio: {candidata.promedio():.2f}").pack(
                pady=2)

    def listar_candidatas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Listado de Candidatas")
        ventana.config(bg="wheat1")

        for c in self.concurso.candidatas.values():
            tk.Label(ventana, text=f"{c.dpi} - {c.nombre} ({c.edad} años) - {c.municipio} - {c.institucion}").pack(
                pady=2)

    def listar_jurados(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Listado de Jurados")
        ventana.config(bg="wheat1")

        for j in self.concurso.jurados.values():
            tk.Label(ventana, text=f"{j.dpi} - {j.nombre} ({j.edad} años) - {j.especialidad} - {j.metodo}").pack(
                pady=2)

    def mostrar_calificaciones(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Calificaciones")
        ventana.config(bg="plum2")

        for c in self.concurso.candidatas.values():
            if c.calificaciones:
                tk.Label(ventana, text=f"Candidata: {c.nombre}", font=("Helvetica", 10, "bold")).pack(pady=2)
                for cal in c.calificaciones:
                    tk.Label(ventana,
                             text=f"Jurado: {cal['jurado']} - Cultura: {cal['cultura']} - Proyección: {cal['proyeccion']} - Entrevista: {cal['entrevista']}").pack(
                        pady=2)
            else:
                tk.Label(ventana, text=f"Candidata: {c.nombre} - Sin calificaciones").pack(pady=2)


if __name__ == "__main__":
    ReinasApp()