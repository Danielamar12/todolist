from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# נתיב לקובץ מסד הנתונים - נשים אותו בתיקיית data כדי לקשר ל-Volume
DB_FOLDER = '/app/data'
DB_FILE = os.path.join(DB_FOLDER, 'todo.db')

# יצירת התיקייה והדאטה-בייס אם לא קיימים
def init_db():
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content:
            c.execute("INSERT INTO tasks (content) VALUES (?)", (task_content,))
            conn.commit()
            return redirect('/')

    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    init_db()
    # הגדרת הפורט ל-90 כפי שנדרש במשימה
    app.run(host='0.0.0.0', port=90)
