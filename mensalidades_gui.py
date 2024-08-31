import tkinter as tk
from tkinter import messagebox, ttk
import crud

def obter_alunos():
    alunos = crud.ler_aluno()
    return [f"{aluno[1]} (ID: {aluno[0]})" for aluno in alunos]

def obter_aluno_id(nome):
    alunos = crud.ler_aluno()
    for aluno in alunos:
        if f"{aluno[1]} (ID: {aluno[0]})" == nome:
            return aluno[0]
    return None

def obter_mensalidades():
    return crud.ler_mensalidade()

def preencher_campos(id):
    mensalidades = obter_mensalidades()
    for mensalidade in mensalidades:
        if mensalidade[0] == id:
            aluno_id = mensalidade[1]
            aluno_nome = [aluno[1] for aluno in crud.ler_aluno() if aluno[0] == aluno_id][0]
            combo_aluno.set(f"{aluno_nome} (ID: {aluno_id})")
            entry_data_pagamento.delete(0, tk.END)
            entry_data_pagamento.insert(0, mensalidade[2])
            entry_valor.delete(0, tk.END)
            entry_valor.insert(0, mensalidade[3])
            entry_status.delete(0, tk.END)
            entry_status.insert(0, mensalidade[4])
            return

def limpar_campos():
    combo_aluno.set("")
    entry_data_pagamento.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_status.delete(0, tk.END)

def listar_mensalidades():
    for widget in frame_list.winfo_children():
        widget.destroy()
    
    tk.Label(frame_list, text="Aluno", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame_list, text="Data Pagamento", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame_list, text="Valor", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
    tk.Label(frame_list, text="Status", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=5, pady=5)
    
    mensalidades = obter_mensalidades()
    alunos_dict = {aluno[0]: aluno[1] for aluno in crud.ler_aluno()}
    
    for i, mensalidade in enumerate(mensalidades, start=1):
        aluno_nome = alunos_dict.get(mensalidade[1], "Desconhecido")
        tk.Label(frame_list, text=aluno_nome).grid(row=i, column=0, padx=5, pady=5)
        tk.Label(frame_list, text=mensalidade[2]).grid(row=i, column=1, padx=5, pady=5)
        tk.Label(frame_list, text=f"R$ {mensalidade[3]:.2f}").grid(row=i, column=2, padx=5, pady=5)
        tk.Label(frame_list, text=mensalidade[4]).grid(row=i, column=3, padx=5, pady=5)
        
       
        tk.Button(frame_list, text="Selecionar", command=lambda id=mensalidade[0]: preencher_campos(id)).grid(row=i, column=4, padx=5, pady=5)

def adicionar_mensalidade():
    try:
        aluno_nome = combo_aluno.get()
        aluno_id = obter_aluno_id(aluno_nome)
        if aluno_id is None:
            raise ValueError("Aluno não encontrado.")
        data_pagamento = entry_data_pagamento.get()
        valor = float(entry_valor.get())
        status = entry_status.get()
        crud.criar_mensalidade(aluno_id, data_pagamento, valor, status)
        listar_mensalidades()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Mensalidade adicionada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar mensalidade: {e}")

def atualizar_mensalidade_ui():
    try:
        aluno_nome = combo_aluno.get()
        aluno_id = obter_aluno_id(aluno_nome)
        if aluno_id is None:
            raise ValueError("Aluno não encontrado.")
        data_pagamento = entry_data_pagamento.get()
        valor = float(entry_valor.get())
        status = entry_status.get()
        selected_id = obter_mensalidades()[0][0]  # Obter o primeiro ID como exemplo; ajuste conforme necessário
        crud.atualizar_mensalidade(selected_id, aluno_id, data_pagamento, valor, status)
        listar_mensalidades()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Mensalidade atualizada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar mensalidade: {e}")

def deletar_mensalidade_ui():
    try:
        selected_id = obter_mensalidades()[0][0]  # Obter o primeiro ID como exemplo; ajuste conforme necessário
        crud.deletar_mensalidade(selected_id)
        listar_mensalidades()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Mensalidade deletada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar mensalidade: {e}")


def abrir_main():
    import main
    main.root.mainloop()

app = tk.Tk()
app.title("Gerenciamento de Mensalidades")

frame_form = tk.Frame(app)
frame_form.pack(padx=10, pady=10)

tk.Label(frame_form, text="Aluno").grid(row=0, column=0)
tk.Label(frame_form, text="Data Pagamento").grid(row=1, column=0)
tk.Label(frame_form, text="Valor").grid(row=2, column=0)
tk.Label(frame_form, text="Status").grid(row=3, column=0)

combo_aluno = ttk.Combobox(frame_form, values=obter_alunos())
entry_data_pagamento = tk.Entry(frame_form)
entry_valor = tk.Entry(frame_form)
entry_status = tk.Entry(frame_form)

combo_aluno.grid(row=0, column=1)
entry_data_pagamento.grid(row=1, column=1)
entry_valor.grid(row=2, column=1)
entry_status.grid(row=3, column=1)

tk.Button(frame_form, text="Adicionar", command=adicionar_mensalidade).grid(row=4, column=0, pady=5)
tk.Button(frame_form, text="Atualizar", command=atualizar_mensalidade_ui).grid(row=4, column=1, pady=5)
tk.Button(frame_form, text="Deletar", command=deletar_mensalidade_ui).grid(row=4, column=2, pady=5)
tk.Button(frame_form, text="Voltar para Menu Principal", command=abrir_main).grid(row=5, column=0, columnspan=3, pady=10)

frame_list = tk.Frame(app)
frame_list.pack(padx=10, pady=10)

listar_mensalidades()

app.mainloop()
