import sqlite3

def criar_banco_de_dados():
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    data DATETIME DEFAULT CURRENT, 
    concluida BOOLEAN NOT NULL DEFAULT 0
    )
""")
    connection.commit()
    connection.close()

def criar_tarefa(descricao):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tarefas (descricao, data, concluida) VALUES(?, CURRENT_TIMESTAMP, 0)', (descricao,))
    connection.commit()
    connection.close()

def mostrar_tarefas():
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, descricao, data, concluida FROM tarefas')
    tarefas = cursor.fetchall()
    connection.close()
    return tarefas

def apagar_tarefa(id):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    connection.commit()
    connection.close()

def concluir_tarefa(id):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (id,))
    connection.commit()
    connection.close()