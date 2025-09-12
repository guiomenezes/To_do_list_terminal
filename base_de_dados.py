import sqlite3

def criar_banco_de_dados():
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    data DATETIME DEFAULT CURRENT, 
    concluida BOOLEAN NOT NULL DEFAULT 0
    )
""")
    connection.commit()
    connection.close()

def criar_tarefa(descricao):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tarefas (descricao, data, concluida) VALUES(?, DATETIME("now", "localtime"), 0)', (descricao,))
    connection.commit()
    connection.close()

def editar_tarefa(id, nova_descricao, concluida):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE tarefas SET descricao = ?, data = DATETIME("now", "localtime"), concluida = ? WHERE id = ?', (nova_descricao, concluida,id,))
    connection.commit()
    connection.close()

def mostrar_tarefas():
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, descricao, data, concluida FROM tarefas')
    tarefas = cursor.fetchall()
    connection.close()
    return tarefas

def mostrar_unica_tarefa(id):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('SELECT descricao, data, concluida FROM tarefas WHERE id = ?', (id,))
    tarefa = cursor.fetchone()
    connection.close()
    return tarefa

def apagar_tarefa(id):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    connection.commit()
    connection.close()

def alterar_status(id, status):
    connection = sqlite3.connect('tarefas.db')
    cursor = connection.cursor()
    if status == '1':
        cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (id,))
    if status == '2':
        cursor.execute('UPDATE tarefas SET concluida = 0 WHERE id = ?', (id,))
    connection.commit()
    connection.close()
