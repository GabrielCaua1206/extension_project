import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def abrir_alunos():
    import alunos_gui
    alunos_gui.app.mainloop()

def abrir_mensalidades():
    import mensalidades_gui
    mensalidades_gui.app.mainloop()

def abrir_desempenho():
    import desempenho_gui
    desempenho_gui.app.mainloop()

# Close the app function
def sair():
    root.destroy()

# Setting up the main window
root = tk.Tk()
root.title("Sistema de Gestão")

# Setting up the interface
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Button(frame, text="Gerenciar Alunos", command=abrir_alunos).pack(fill=tk.X, pady=5)
tk.Button(frame, text="Gerenciar Mensalidades", command=abrir_mensalidades).pack(fill=tk.X, pady=5)
tk.Button(frame, text="Gerenciar Desempenho", command=abrir_desempenho).pack(fill=tk.X, pady=5)
tk.Button(frame, text="Sair", command=sair).pack(fill=tk.X, pady=5)

root.mainloop()
