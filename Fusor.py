import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF3
import os

class PDFMergerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Merger")
        self.master.geometry("400x350")
        
        self.file_list = []
        
        self.label = tk.Label(master, text="Selecciona los archivos PDF:")
        self.label.pack()
        
        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE, height=10, width=50)
        self.listbox.pack()
        
        self.select_button = tk.Button(master, text="Seleccionar archivos", command=self.select_files)
        self.select_button.pack()
        
        self.delete_button = tk.Button(master, text="Eliminar Seleccionados", command=self.delete_selected)
        self.delete_button.pack()
        
        self.move_up_button = tk.Button(master, text="Mover Arriba", command=self.move_up)
        self.move_up_button.pack()
        
        self.move_down_button = tk.Button(master, text="Mover Abajo", command=self.move_down)
        self.move_down_button.pack()
        
        self.merge_button = tk.Button(master, text="Unir PDFs", command=self.merge_pdfs)
        self.merge_button.pack()
        
    def select_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            filename = os.path.basename(file)
            self.listbox.insert(tk.END, filename)
        self.file_list.extend(files)
        print("Archivos seleccionados:", self.file_list)
        
    def delete_selected(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Advertencia", "Selecciona archivos para eliminar.")
            return
        
        selected_files = [self.file_list[index] for index in selected_indices]
        for index in selected_indices[::-1]:
            self.listbox.delete(index)
            del self.file_list[index]
        print("Archivos eliminados:", selected_files)
        
    def move_up(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices or selected_indices[0] == 0:
            return
        
        for index in selected_indices:
            item = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index - 1, item)
            self.file_list[index], self.file_list[index - 1] = self.file_list[index - 1], self.file_list[index]
        self.listbox.selection_set(selected_indices[0] - 1)
        
    def move_down(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices or selected_indices[-1] == self.listbox.size() - 1:
            return
        
        for index in reversed(selected_indices):
            item = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index + 1, item)
            self.file_list[index], self.file_list[index + 1] = self.file_list[index + 1], self.file_list[index]
        self.listbox.selection_set(selected_indices[-1] + 1)
        
    def merge_pdfs(self):
        if not self.file_list:
            print("No hay archivos para unir.")
            messagebox.showwarning("Advertencia", "No hay archivos para unir.")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_file:
            return
        
        merger = PyPDF3.PdfFileMerger()
        for file in self.file_list:
            try:
                merger.append(file)
            except PyPDF3.utils.PdfReadError:
                print("Error al abrir el archivo:", file)
        
        try:
            merger.write(output_file)
            print("PDFs unidos con éxito:", output_file)
            messagebox.showinfo("Éxito", "PDFs unidos con éxito.")
        except Exception as e:
            print("Error al guardar el archivo:", e)
            messagebox.showerror("Error", "Error al guardar el archivo.")
        
        merger.close()
        
        self.clear_listbox()
        
    def clear_listbox(self):
        self.listbox.delete(0, tk.END)
        self.file_list.clear()
        
def main():
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
