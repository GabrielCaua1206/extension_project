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

def obter_desempenhos():
    return crud.ler_desempenho()

def preencher_campos(id):
    desempenhos = obter_desempenhos()
    for desempenho in desempenhos:
        if desempenho[0] == id:
            aluno_id = desempenho[1]
            aluno_nome = [aluno[1] for aluno in crud.ler_aluno() if aluno[0] == aluno_id][0]
            combo_aluno.set(f"{aluno_nome} (ID: {aluno_id})")
            entry_data_registro.delete(0, tk.END)
            entry_data_registro.insert(0, desempenho[2])
            entry_observacoes.delete(0, tk.END)
            entry_observacoes.insert(0, desempenho[3])
            return

def limpar_campos():
    combo_aluno.set("")
    entry_data_registro.delete(0, tk.END)
    entry_observacoes.delete(0, tk.END)

def listar_desempenhos():
    for widget in frame_list.winfo_children():
        widget.destroy()
    
    tk.Label(frame_list, text="Aluno", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame_list, text="Data Registro", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame_list, text="Observações", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
    
    desempenhos = obter_desempenhos()
    alunos_dict = {aluno[0]: aluno[1] for aluno in crud.ler_aluno()}
    
    for i, desempenho in enumerate(desempenhos, start=1):
        aluno_nome = alunos_dict.get(desempenho[1], "Desconhecido")
        tk.Label(frame_list, text=aluno_nome).grid(row=i, column=0, padx=5, pady=5)
        tk.Label(frame_list, text=desempenho[2]).grid(row=i, column=1, padx=5, pady=5)
        tk.Label(frame_list, text=desempenho[3]).grid(row=i, column=2, padx=5, pady=5)
        
        tk.Button(frame_list, text="Selecionar", command=lambda id=desempenho[0]: preencher_campos(id)).grid(row=i, column=3, padx=5, pady=5)

def adicionar_desempenho():
    try:
        aluno_nome = combo_aluno.get()
        aluno_id = obter_aluno_id(aluno_nome)
        if aluno_id is None:
            raise ValueError("Aluno não encontrado.")
        data_registro = entry_data_registro.get()
        observacoes = entry_observacoes.get()
        crud.criar_desempenho(aluno_id, data_registro, observacoes)
        listar_desempenhos()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Desempenho adicionado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar desempenho: {e}")

def atualizar_desempenho_ui():
    try:
        aluno_nome = combo_aluno.get()
        aluno_id = obter_aluno_id(aluno_nome)
        if aluno_id is None:
            raise ValueError("Aluno não encontrado.")
        data_registro = entry_data_registro.get()
        observacoes = entry_observacoes.get()
        selected_id = [desempenho[0] for desempenho in obter_desempenhos()][0]  
        crud.atualizar_desempenho(selected_id, aluno_id, data_registro, observacoes)
        listar_desempenhos()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Desempenho atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar desempenho: {e}")

def deletar_desempenho_ui():
    try:
        selected_id = [desempenho[0] for desempenho in obter_desempenhos()][0]
        listar_desempenhos()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Desempenho deletado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar desempenho: {e}")


def abrir_main():
    import main
    main.root.mainloop()

app = tk.Tk()
app.title("Gerenciamento de Desempenho")

frame_form = tk.Frame(app)
frame_form.pack(padx=10, pady=10)

tk.Label(frame_form, text="Aluno").grid(row=0, column=0)
tk.Label(frame_form, text="Data Registro").grid(row=1, column=0)
tk.Label(frame_form, text="Observações").grid(row=2, column=0)

combo_aluno = ttk.Combobox(frame_form, values=obter_alunos())
entry_data_registro = tk.Entry(frame_form)
entry_observacoes = tk.Entry(frame_form)

combo_aluno.grid(row=0, column=1)
entry_data_registro.grid(row=1, column=1)
entry_observacoes.grid(row=2, column=1)

tk.Button(frame_form, text="Adicionar", command=adicionar_desempenho).grid(row=3, column=0, pady=5)
tk.Button(frame_form, text="Atualizar", command=atualizar_desempenho_ui).grid(row=3, column=1, pady=5)
tk.Button(frame_form, text="Deletar", command=deletar_desempenho_ui).grid(row=3, column=2, pady=5)
tk.Button(frame_form, text="Voltar para Menu Principal", command=abrir_main).grid(row=4, column=0, columnspan=3, pady=10)

frame_list = tk.Frame(app)
frame_list.pack(padx=10, pady=10)

listar_desempenhos()

app.mainloop()
