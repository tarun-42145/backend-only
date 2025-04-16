import sqlite3

def connect():
    return sqlite3.connect('employees.db')

def init_db():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_employee(name, role):
    conn = connect()
    c = conn.cursor()
    c.execute('INSERT INTO employees (name, role) VALUES (?, ?)', (name, role))
    emp_id = c.lastrowid
    conn.commit()
    conn.close()
    return emp_id

def get_employees():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT id, name, role FROM employees')
    employees = [{'id': row[0], 'name': row[1], 'role': row[2]} for row in c.fetchall()]
    conn.close()
    return employees

def delete_employee(emp_id):
    conn = connect()
    c = conn.cursor()
    c.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    deleted = c.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
