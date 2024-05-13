from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Configuración de la ventana principal
frame = tk.Tk()
frame.title("Fusor PDFs")
frame.configure(bg='#33A5FF')
frame.resizable(0, 0)

# Calcula la posición para centrar la ventana
anchoventana = 400
altoventana = 300
x_ventana = frame.winfo_screenwidth() // 2 - anchoventana // 2
y_ventana = frame.winfo_screenheight() // 2 - altoventana // 2
posicion = f"{anchoventana}x{altoventana}+{x_ventana}+{y_ventana}"
frame.geometry(posicion)

# Lista para almacenar las rutas de los archivos PDF seleccionados
pdfs = []

# Lista auxiliar para mantener el orden de selección
pdfs_ordered = []

# Función para seleccionar archivos PDF
def select():
    global pdfs
    # Filtra para seleccionar solo archivos PDF
    tipos_archivo = [('Archivos PDF', '*.pdf')]
    filenames = filedialog.askopenfilenames(filetypes=tipos_archivo)
    # Añade cada archivo seleccionado a la lista 'pdfs'
    for filename in filenames:
        pdfs.append(filename)
        pdfs_ordered.append(filename)  # Añadir a la lista auxiliar
    refresh_text_area()

# Función para eliminar un archivo de la lista pdfs
def remove_file(index):
    global pdfs, pdfs_ordered
    pdfs.pop(index)
    pdfs_ordered.pop(index)
    refresh_text_area()

# Función para actualizar el área de texto con los nombres de los archivos seleccionados
def refresh_text_area():
    inputtxt.delete(1.0, tk.END)
    for pdf in pdfs_ordered:
        inputtxt.insert(tk.END, os.path.basename(pdf) + '\n')
        remove_button = tk.Button(frame, text="Eliminar", command=lambda pdf=pdf: remove_file(pdfs.index(pdf)))
        inputtxt.window_create(tk.END, window=remove_button)
        inputtxt.insert(tk.END, '\n')

# Función para fusionar los archivos PDF seleccionados
def convertir():
    try:
        global pdfs
        # Crear un objeto PdfWriter para escribir el archivo fusionado
        writer = PdfWriter()

        # Fusionar cada archivo PDF
        for pdf in pdfs:
            # Leer el archivo PDF con PdfReader
            reader = PdfReader(pdf)
            # Añadir cada página al objeto writer
            for page in reader.pages:
                writer.add_page(page)

        # Abrir un cuadro de diálogo para guardar el archivo PDF fusionado
        file_name = name_entry.get()
        if not file_name:
            file_name = "result"
        
        # Abrir cuadro de diálogo para elegir la ubicación de guardado
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")], initialfile=file_name)
        
        if save_path:
            # Guardar el archivo PDF fusionado en la ubicación seleccionada
            with open(save_path, "wb") as output_file:
                writer.write(output_file)

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Unión exitosa")
        else:
            # Mostrar un mensaje si el usuario canceló el diálogo
            messagebox.showinfo("Cancelado", "Proceso de guardado cancelado")
    except Exception as e:
        # Mostrar un mensaje de error si ocurre un problema
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Área de texto para mostrar los nombres de los archivos seleccionados
inputtxt = tk.Text(frame, height=5, width=40)
inputtxt.pack(pady=10)

# Contenedor para la etiqueta y el campo de entrada
name_frame = tk.Frame(frame)
name_frame.pack(pady=10)

# Etiqueta para el campo de entrada
name_label = tk.Label(name_frame, text="Nombre de archivo:")
name_label.pack(side="left")

# Campo de entrada para el nombre del archivo
name_entry = tk.Entry(name_frame, width=40)
name_entry.pack(side="left")
name_entry.insert(0, "result")  # Nombre predeterminado

# Botón para seleccionar archivos PDF
sButton = tk.Button(frame, text="Seleccionar archivos", width=20, height=1, command=select)
sButton.pack(pady=10)

# Botón para fusionar los archivos seleccionados
printButton = tk.Button(frame, text="Unir archivos", width=15, height=1, command=convertir)
printButton.pack(pady=10)

# Inicia el bucle de la interfaz gráfica de usuario
frame.mainloop()
