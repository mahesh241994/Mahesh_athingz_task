# Sales Record Management System

##  Project Scope

This Django web application allows users to manage and analyze sales records efficiently with the following core features:

###  Features
- Upload and import sales records from Excel or CSV files
- Store records in a relational database (SQLite/MySQL)
- View paginated sales records (500 per page)
- Search and filter sales records
- Add, Edit, and Delete sales records via web interface
- Export filtered records to a CSV file (with proper date formatting)
- Region, Country, and Item Type are dropdown fields

---

###  Setup Instructions

### 1. Clone the Repository

git clone https://github.com/mahesh241994/Mahesh_athingz_task.git
cd Mahesh_athingz_task

### Create and Activate Virtual Environment
python -m venv env
source env/bin/activate   ---  Linux users
env\Scripts\activate ---- Windows users

### Install Requirements
pip install -r requirements.txt

### Apply Migrations
python manage.py makemigrations
python manage.py migrate

### Run Development Server
python manage.py runserver

### http://127.0.0.1:8000

