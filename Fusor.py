from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

frame = tk.Tk()
frame.title("Fusor PDFs")
frame.configure(bg='#33A5FF')
anchoventana = 400
altoventana = 300
x_ventana = frame.winfo_screenwidth() // 2 - anchoventana // 2
y_ventana = frame.winfo_screenwidth() // 2 - altoventana // 2
posicion = str(anchoventana) + "x" + str(altoventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
frame.geometry(posicion)
frame.resizable(0,0)

pdfs = []
merge = PdfFileMerger()

def select():
    global filename
    tipoArchivo = (('text files', '*.pdf'),)
    filename = askopenfilename(filetypes=tipoArchivo)
    pdfs.append(filename)
    file_name = os.path.basename(filename)
    inputtxt.insert('end', file_name + '\n')
    #messagebox.showinfo(message="Archivo Seleccionado")
    

def convertir():
    global pdfs
    for pdf in pdfs:
        merge.append(pdf)
    merge.write("./result.pdf")
    messagebox.showinfo(message="Unión exitosa")

inputtxt = tk.Text(frame, height = 5, width = 40)
inputtxt.pack(pady=10)

sButton = tk.Button(frame, text = "Seleccionar archivo", width=15, height=1, command = select)
sButton.pack(pady=30)

printButton = tk.Button(frame, text = "Unir archivo", width=15, height=1, command = convertir)
printButton.pack(pady=10)

frame.mainloop()
