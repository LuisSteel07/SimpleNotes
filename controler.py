import sqlite3

def get_id():
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    id_task = cur.execute("SELECT max(id) FROM Note").fetchone()[0]
    if id_task is None: return 0
    else: return id_task

def create_table():
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE "Note" (
                        "id"	INTEGER NOT NULL UNIQUE,
	                    "title"	TEXT NOT NULL,
	                    "text" TEXT NOT NULL,
                        "completed"	TEXT NOT NULL,
                        PRIMARY KEY("id" AUTOINCREMENT)
                );""")

def add_note(task_name: str, text: str):
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    cur.execute("INSERT INTO Note (title, text, completed) VALUES (?, ?, ?)", (task_name, text, "False"))
    conn.commit()

def update_note(task_id: int, new_task_name: str, completed: bool):
    completed_str = "False"
    if completed: completed_str = "True"

    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    cur.execute("UPDATE Note SET title = ?, completed = ? WHERE id = ?", (new_task_name, completed_str,task_id))
    conn.commit()

def delete_note(task_id: int):
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor()
    cur.execute("DELETE FROM Note WHERE id = ?", (task_id,))
    conn.commit()

def get_notes():
    try:
        conn = sqlite3.connect("data.sqlite")
        cur = conn.cursor()
        return cur.execute("SELECT * FROM Note").fetchall()
    except sqlite3.OperationalError:
        create_table()
        get_notes()