from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter import messagebox, filedialog
import os

frame = tk.Tk()
frame.title("Fusor PDFs")
frame.configure(bg='#33A5FF')
frame.resizable(0,0)

# Calcula la posición para centrar la ventana
anchoventana = 400
altoventana = 300
x_ventana = frame.winfo_screenwidth() // 2 - anchoventana // 2
y_ventana = frame.winfo_screenheight() // 2 - altoventana // 2
posicion = str(anchoventana) + "x" + str(altoventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
frame.geometry(posicion)

pdfs = []
merge = PdfFileMerger()

def select():
    global pdfs
    tipos_archivo = [('Archivos PDF', '*.pdf')]
    filenames = filedialog.askopenfilenames(filetypes=tipos_archivo)
    for filename in filenames:
        pdfs.append(filename)
        file_name = os.path.basename(filename)
        inputtxt.insert('end', file_name + '\n')

def convertir():
    global pdfs
    for pdf in pdfs:
        merge.append(pdf)
    merge.write("./result.pdf")
    messagebox.showinfo(message="Unión exitosa")

inputtxt = tk.Text(frame, height=5, width=40)
inputtxt.pack(pady=10)

sButton = tk.Button(frame, text="Seleccionar archivos", width=20, height=1, command=select)
sButton.pack(pady=10)

printButton = tk.Button(frame, text="Unir archivos", width=15, height=1, command=convertir)
printButton.pack(pady=10)

frame.mainloop()
