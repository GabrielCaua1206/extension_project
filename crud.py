import sqlite3
from db import criar_conexao

# Create an aluno

def criar_aluno(nome, idade, turma, responsavel, contato_responsavel):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO alunos (nome, idade, turma, responsavel, contato_responsavel)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, idade, turma, responsavel, contato_responsavel))
        conn.commit()
    except:
        print("Ocorreu um erro.")
    finally:
        conn.close()
        
# Read an aluno

def ler_aluno(id=None):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        if id is None:
            cursor.execute('SELECT * FROM alunos')
        else:
            cursor.execute('SELECT * FROM alunos WHERE id = ?', (id,))
        alunos = cursor.fetchall()
        return alunos
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    finally:
        conn.close()

# Update an aluno

def atualizar_aluno(id, nome=None, idade=None, turma=None, responsavel=None, contato_responsavel=None):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE alunos
            SET nome = ?, idade = ?, turma = ?, responsavel = ?, contato_responsavel = ?
            WHERE id = ?
        ''', (nome, idade, turma, responsavel, contato_responsavel, id))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conn.close()

# Delete an aluno

def deletar_aluno(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM alunos WHERE id = ?', (id,))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conn.close()


# Mensalidades table

# Creates a mensalidade
def criar_mensalidade(aluno_id, data_pagamento, valor, status):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO mensalidades (aluno_id, data_pagamento, valor, status)
            VALUES (?, ?, ?, ?)
        ''', (aluno_id, data_pagamento, valor, status))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao criar a mensalidade: {e}")
    finally:
        conn.close()

# Read a mensalidade
def ler_mensalidade(id=None):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        if id is None:
            cursor.execute("SELECT * FROM mensalidades")
        else:
            cursor.execute("SELECT * FROM mensalidades WHERE id = ?", (id,))
        mensalidades = cursor.fetchall()
        return mensalidades
    except Exception as e:
        print(f"Ocorreu um erro ao ler a mensalidade: {e}")
        return None
    finally:
        conn.close()

# Update a mensalidade
def atualizar_mensalidade(id, aluno_id, data_pagamento, valor, status):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE mensalidades
            SET aluno_id = ?, data_pagamento = ?, valor = ?, status = ?
            WHERE id = ?
        ''', (aluno_id, data_pagamento, valor, status, id))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar a mensalidade: {e}")
    finally:
        conn.close()

# Delete a mensalidade
def deletar_mensalidade(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM mensalidades WHERE id = ?', (id,))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao deletar a mensalidade: {e}")
    finally:
        conn.close()


# Desempenho table

# Creates a register of student's performance
def criar_desempenho(aluno_id, data_registro, observacoes):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO desempenho (aluno_id, data_registro, observacoes)
            VALUES (?, ?, ?)
        ''', (aluno_id, data_registro, observacoes))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao criar o desempenho: {e}")
    finally:
        conn.close()

# Reads the student's performance
def ler_desempenho():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM desempenho")
        desempenhos = cursor.fetchall()
        return desempenhos
    except Exception as e:
        print(f"Ocorreu um erro ao ler o desempenho: {e}")
        return None
    finally:
        conn.close()

# Updates student's performance
def atualizar_desempenho(id, aluno_id=None, data_registro=None, observacoes=None):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE desempenho
            SET aluno_id = ?, data_registro = ?, observacoes = ?
            WHERE id = ?
        ''', (aluno_id, data_registro, observacoes, id))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o desempenho: {e}")
    finally:
        conn.close()

# Remove the performance information
def deletar_desempenho(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM desempenho WHERE id = ?', (id,))
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao deletar o desempenho: {e}")
    finally:
        conn.close()
