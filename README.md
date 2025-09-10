### PARCIAL #2

La Municipalidad de Quetzaltenango necesita un prototipo rápido para gestionar la elección de la Reina de Independencia 2025.

Requerimientos mínimos: 
1. Registrar candidatas (código, nombre, edad, institución educativa, municipio).
2. Registrar jurados y calificaciones en tres criterios (cultura general, proyección escénica, entrevista).
3. Calcular puntaje promedio por jurado y puntaje final por candidata, mostrando ranking y ganadora.
4. Guardar y cargar datos en archivos de texto (formato TXT).
5. Interfaz mínima con Tkinter: agregar candidata, calificación, mostrar ranking, botones para guardar/cargar.

# División
 2 Branches
 - Things (Luis)
 - Jalegosa (Jackie)

**Tabla de Contenidos**

[TOCM]

[TOC]
##Luis 
Clases principales,  Registro (RAMA Things)
```
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
                califs_str = ";".join(
                    [f"{cal['cultura']}, {cal['proyeccion']}, {cal['entrevista']}, {cal['jurado']}, {cal['metodo']}" for
                     cal in c.calificaciones])
                f.write(f"{c.dpi}:{c.nombre}:{c.edad}:{c.municipio}:{c.institucion}:{califs_str}\n ")
```

##Jackie 
Interfaz, Carga y Validaciones (RAMA Jalegosa)


    
            def registrar_candidata(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Candidata")
        ventana.config(bg="burlywood1")

        tk.Label(ventana, text="DPI:", font=("Helvetica", 16, "bold"), bg="burlywood1", fg="white",
                 justify="center").pack(pady=2)
        dpi = tk.Entry(ventana);
        dpi.pack(pady=2)
        tk.Label(ventana, text="Nombre:", font=("Helvetica", 16, "bold"), bg="burlywood1", fg="white",
                 justify="center").pack(pady=2)
        nombre = tk.Entry(ventana);
        nombre.pack(pady=2)
        tk.Label(ventana, text="Edad:", font=("Helvetica", 16, "bold"), bg="burlywood1", fg="white",
                 justify="center").pack(pady=2)
        edad = tk.Entry(ventana);
        edad.pack(pady=2)
        tk.Label(ventana, text="Municipio:", font=("Helvetica", 16, "bold"), bg="burlywood1", fg="white",
                 justify="center").pack(pady=2)
        municipio = ttk.Combobox(ventana, values=self.municipios);
        municipio.pack(pady=2)
        tk.Label(ventana, text="Institución:", font=("Helvetica", 16, "bold"), bg="burlywood1", fg="white",
                 justify="center").pack(pady=2)
        institucion = tk.Entry(ventana);
        institucion.pack(pady=2)

        def guardar():
            if not dpi.get() or not nombre.get() or not edad.get() or not municipio.get() or not institucion.get():
                messagebox.showwarning("Atención", "Todos los campos son obligatorios")
                dpi.focus_set()
                return
            if nombre.get().isdigit():
                messagebox.showwarning("Atención", "El nombre no puede ser un número")
                nombre.focus_set()
                return
            try:
                edad_val = int(edad.get())
            except:
                messagebox.showwarning("Atención", "Edad debe ser numérica")
                edad.focus_set()

                return
            if edad_val < 18 or edad_val > 23:
                messagebox.showwarning("Atención", "La edad debe estar entre 18 y 23 años")
                edad.focus_set()

                return
            candidata = Candidata(dpi.get(), nombre.get(), edad_val, municipio.get(), institucion.get())
            if self.concurso.registrar_candidata(candidata):
                messagebox.showinfo("Éxito", "Candidata registrada correctamente")
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
        tk.Button(ventana, text="Cancelar", command=ventana.destroy).pack(pady=5)
        try:
            self.foto_candidata = tk.PhotoImage(file="reina.gif")
            tk.Label(ventana, image=self.foto_candidata, bg="burlywood1").pack(anchor="center", padx=10, pady=10)
        except Exception as e:
            print("No se pudo cargar la imagen:", e)
###End
