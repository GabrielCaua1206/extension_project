import sqlite3

conn = sqlite3.connect("escolinha.db")
cursor = conn.cursor()

def criar_conexao():
    conn = sqlite3.connect("escolinha.db")
    return conn

cursor.execute('''
               CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INTEGER,
                   turma TEXT,
                   responsavel TEXT,
                   contato_responsavel TEXT
               )
               ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS mensalidades (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   aluno_id INTEGER,
                   data_pagamento DATE,
                   valor REAL,
                   status TEXT,
                   FOREIGN KEY(aluno_id) REFERENCES alunos(id)
               )
               ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS desempenho (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        data_registro DATE,
        observacoes TEXT,
        FOREIGN KEY(aluno_id) REFERENCES alunos(id)
    )
''')

conn.commit()
conn.close()