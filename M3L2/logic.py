import sqlite3
from config import DATABASE, TOKEN

class DB_Manager:
    def __init__(self, database):
        self.database = database # Nama databasenya
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
            conn.execute('''CREATE TABLE skills (
              skill_id INTEGER PRIMARY KEY,
              skill_name TEXT
            )
        ''')

            conn.execute('''CREATE TABLE status (
              status_id INTEGER PRIMARY KEY,
              status_name TEXT
            )
        ''')

            conn.execute('''CREATE TABLE projects (
              project_id INTEGER PRIMARY KEY,
              project_name TEXT,
              description TEXT,
              url TEXT,
              status_id INTEGER,
              FOREIGN KEY(status_id) REFERENCES status(status_id)
            )
        ''')

            conn.execute('''CREATE TABLE project_skills (
              project_id INTEGER,
              skill_id INTEGER,
              FOREIGN KEY(project_id) REFERENCES projects(project_id),
              FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
            )
        ''')

            conn.commit()

        print("Database terbuat")