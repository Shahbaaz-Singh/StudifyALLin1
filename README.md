# StudifyALLin1

## Overview
Studify is a Flask-based web application designed for managing users, including admins, employees, and applicants.
The application uses PostgreSQL as the database and incorporates SQLAlchemy for ORM functionality.
This document provides setup instructions, including creating an admin user, configuring the database, and managing migrations.

---

## Prerequisites
1. **Python** (latest version recommended)
2. **PostgreSQL** with **pgAdmin**
3. **Flask Framework**
4. Necessary Python packages (listed in `requirements`)

---

## Setup Instructions

### Step 1: Set Up PostgreSQL Database
1. **Install PostgreSQL** and **pgAdmin** if not already installed.
2. Open pgAdmin and perform the following steps:
    - Create a new database named `database_name`.
    - Create a new login/group role:
      - **Username**: `username`
      - **Password**: `password`
      - Grant appropriate privileges to `Studify_User` for the `Studify` database.
3. If you want to use a custom username, password, or database name, update the connection URI in `__init__.py`:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost:5432/<database_name>'
    ```

### Step 2: Set Up the Project
1. Copy the project files into your working directory.
2. Open a command prompt and navigate to the project directory.

---

## Virtual Environment and Dependencies

### Step 1: Create and Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### Step 2: Install Required Dependencies
```
pip install -r requirements
```

## Database Initialization

### Initialize Database Migrations
Run the following commands in the command prompt:
```
flask db init
flask db migrate
flask db upgrade
```

---

## Creating an Admin User
To create an admin user, use the Flask shell:

### Step 1: Open Flask Shell
Run the following command in the project directory:
```
flask shell
```

### Step 2: Create an Admin
Inside the shell, execute the following commands:
```python
from app import db
from app.models import Admin

admin = Admin(username="admin_name")
admin.set_password("password")
db.session.add(admin)
db.session.commit()
```
Replace `admin_name` and `password` with your desired admin credentials.

---

## Running the Application
Start the Flask development server with:
```
flask run
```
The application will be accessible at `http://127.0.0.1:5000/`.

---

## Troubleshooting

### Error: "Database Does Not Exist"
If the database `database_name` is deleted and recreated:
1. Ensure the database name and user credentials are correctly set.
2. Delete the `migrations` folder.
3. Reinitialize the migrations and apply them:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

---

## Notes
1. The `username` and `password` credentials are the default settings. Change them as needed and ensure the connection URI in the code matches.
2. Using a virtual environment to manage dependencies is advisable.
---