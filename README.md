# Django Books Model Practice

This project is a simple Django practice application focused on learning how to work with **models**, **database relationships**, and **Django admin panel**.

## 📌 Project Purpose
The goal of this project is to practice:

- Creating Django models
- Working with database relationships (ForeignKey, ManyToMany)
- Using field validators and options
- Registering models in Django admin
- Performing database migrations
- Interacting with data using Django shell

---

## 🧱 Models Included
The project contains models representing:

- Books  
- Authors  
- Countries  

These models are connected using relational database concepts.

---

## ⚙️ Technologies Used

- Python  
- Django  
- SQLite (default Django database)  

---

## ▶️ How To Run The Project

1. Clone the repository

```bash
git clone https://github.com/mohamedtalaatinfo/django-books-model.git
Navigate to project folder

cd django-books-model
Install dependencies (if needed)

pip install django
Run migrations

python manage.py migrate
Create superuser

python manage.py createsuperuser
Run development server

python manage.py runserver
Open admin panel

http://127.0.0.1:8000/admin
🎯 Learning Notes
This project is created for learning and practicing Django fundamentals and may be expanded later with views, templates, or APIs.

👨‍💻 Author
Mohamed Talaat