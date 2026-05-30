import sqlite3  # built-in library for working with SQLite database

# connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()  # cursor to execute SQL commands

# create tasks table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        title TEXT,                             
        done INTEGER DEFAULT 0                  
    )
''')
conn.commit()  # save changes

def add_task(title):
    # insert new task into table
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    print(f'Task added: {title}')

def show_tasks():
    # select all tasks from table
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()  # get all results as list of tuples
    if not tasks:
        print('There are no tasks')
        return
    for task in tasks:
        status = 'done' if task[2] == 1 else 'not done'  # task[2] is done field
        print(f'{task[0]}.[{status}] {task[1]}')  # task[0] is id, task[1] is title

def complete_task(id):
    # update done field to 1 for specific task
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (id,))
    conn.commit()
    print(f'Task {id} completed')

def delete_task(id):
    # delete task by id
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    print(f'Task {id} deleted')

# main menu loop
while True:
    print('\n1. Show tasks')
    print('2. Add a task')
    print('3. Mark completed')
    print('4. Delete task')
    print('5. Exit')

    choice = input('Choose an action: ')

    if choice == '1':
        show_tasks()
    elif choice == '2':
        title = input('Task name: ')
        add_task(title)
    elif choice == '3':
        id = int(input('Task number: '))
        complete_task(id)
    elif choice == '4':
        id = int(input('Task number: '))
        delete_task(id)
    elif choice == '5':
        break  # exit the program
    