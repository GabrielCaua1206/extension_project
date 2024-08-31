import tkinter as tk
from tkinter import ttk, messagebox
import crud

# opens main.py
def abrir_main():
    import main
    main.root.mainloop()

def criar_interface():
    global app
    app = tk.Tk()
    app.title("Gerenciar Alunos")

    # Frames
    frame_listar = tk.Frame(app)
    frame_listar.pack(padx=10, pady=10)

    frame_form = tk.Frame(app)
    frame_form.pack(padx=10, pady=10)

    # Function for "alunos"
    def listar():
        for item in tree.get_children():
            tree.delete(item)
        alunos = crud.ler_aluno()
        for index, aluno in enumerate(alunos):
            # Defines line's color based on index
            if index % 2 == 0:
                tree.insert("", tk.END, values=aluno[1:], tags=("evenrow",))
            else:
                tree.insert("", tk.END, values=aluno[1:], tags=("oddrow",))

        # Define tag's style
        tree.tag_configure("evenrow", background="#f0f0f0")
        tree.tag_configure("oddrow", background="#ffffff") 

    # Fill the fields when select an item
    def selecionar_item(event):
        item = tree.selection()[0]
        nome = tree.item(item, "values")[0]
        aluno = next(a for a in crud.ler_aluno() if a[1] == nome)
        if aluno:
            id_var.set(aluno[0])
            nome_var.set(aluno[1])
            idade_var.set(aluno[2])
            turma_var.set(aluno[3])
            responsavel_var.set(aluno[4])
            contato_responsavel_var.set(aluno[5])

    # Add one aluno
    def adicionar():
        try:
            crud.criar_aluno(nome_var.get(), idade_var.get(), turma_var.get(), responsavel_var.get(), contato_responsavel_var.get())
            listar()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Update aluno's data
    def atualizar():
        try:
            crud.atualizar_aluno(id_var.get(), nome_var.get(), idade_var.get(), turma_var.get(), responsavel_var.get(), contato_responsavel_var.get())
            listar()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Delete aluno
    def remover():
        try:
            crud.deletar_aluno(id_var.get())
            listar()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Clean the fields
    def limpar_campos():
        id_var.set("")
        nome_var.set("")
        idade_var.set("")
        turma_var.set("")
        responsavel_var.set("")
        contato_responsavel_var.set("")

    # Tree configuration to list alunos
    tree = ttk.Treeview(frame_listar, columns=("Nome", "Idade", "Turma", "Responsável", "Contato"), show="headings")
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Turma", text="Turma")
    tree.heading("Responsável", text="Responsável")
    tree.heading("Contato", text="Contato")
    tree.pack()
    tree.bind("<ButtonRelease-1>", selecionar_item)

    # Form configuration
    tk.Label(frame_form, text="Nome").grid(row=0, column=0)
    tk.Label(frame_form, text="Idade").grid(row=1, column=0)
    tk.Label(frame_form, text="Turma").grid(row=2, column=0)
    tk.Label(frame_form, text="Responsável").grid(row=3, column=0)
    tk.Label(frame_form, text="Contato").grid(row=4, column=0)

    id_var = tk.StringVar()
    nome_var = tk.StringVar()
    idade_var = tk.StringVar()
    turma_var = tk.StringVar()
    responsavel_var = tk.StringVar()
    contato_responsavel_var = tk.StringVar()

    tk.Entry(frame_form, textvariable=nome_var).grid(row=0, column=1)
    tk.Entry(frame_form, textvariable=idade_var).grid(row=1, column=1)
    tk.Entry(frame_form, textvariable=turma_var).grid(row=2, column=1)
    tk.Entry(frame_form, textvariable=responsavel_var).grid(row=3, column=1)
    tk.Entry(frame_form, textvariable=contato_responsavel_var).grid(row=4, column=1)

    tk.Button(frame_form, text="Adicionar", command=adicionar).grid(row=5, column=0, pady=10)
    tk.Button(frame_form, text="Atualizar", command=atualizar).grid(row=5, column=1, pady=10)
    tk.Button(frame_form, text="Remover", command=remover).grid(row=5, column=2, pady=10)
    tk.Button(frame_form, text="Voltar para Menu Principal", command=abrir_main).grid(row=6, column=0, columnspan=3, pady=10)

    listar()  # Initialize alunos list

    app.mainloop()

criar_interface()
