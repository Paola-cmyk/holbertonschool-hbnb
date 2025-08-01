from app import create_app
import os
import sqlite3

def execute_script(db_path, script_path):
    try:
        with sqlite3.connect(db_path) as conn:
            with open(script_path, 'r') as script:
                conn.executescript(script.read())
        print(f"Successfully executed: {script_path}")
    except Exception as e:
        print(f"Error executing script {script_path}: {e}")

def initialize_database():
    base_dir = os.path.dirname(__file__)
    db_path = "/home/franciscobaez/holbertonschool-hbnb/instance/development.db"
    scripts_path = os.path.join(base_dir, "app/persistence", "scripts.sql")
    seed_path = os.path.join(base_dir, "app/persistence", "seed.sql")

    if not os.path.exists(os.path.join(base_dir, "app/persistence")):
        print("Error: The 'database' folder does not exist.")
        return

    print("Initializing database...")
    execute_script(db_path, scripts_path)
    execute_script(db_path, seed_path)
    print("Database initialization complete.")

app = create_app()
with app.app_context():
    initialize_database()

if __name__ == '__main__':
    app.run(debug=True)
