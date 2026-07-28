<h1 align="center">
🚀 To-Do Backend API
</h1>

<h3 align="center">
A Production-Ready RESTful API built using Django REST Framework
</h3>

<p align="center">
Designed with scalability, clean architecture and REST best practices.
</p>



<p align="center">

![Django](https://img.shields.io/badge/Django-5.x-darkgreen?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

</p>

---

## 🌟 Overview

A **RESTful To-Do Backend API** built using **Django** and **Django REST Framework**.

This project allows users to efficiently manage their daily tasks through powerful REST APIs. It supports complete CRUD operations, filtering, searching, ordering, pagination, validation, and bonus features like priority levels and due dates.

---

# ✨ Features

✅ Create Tasks

✅ Retrieve All Tasks

✅ Retrieve Single Task

✅ Update Tasks (PUT)

✅ Partial Update (PATCH)

✅ Delete Tasks

✅ Search Tasks

✅ Filter Tasks

✅ Order Tasks

✅ Pagination

✅ Custom Validation

✅ Due Date Support

✅ Priority Levels

✅ Django Admin Panel

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming Language |
| 🌿 Django | Web Framework |
| ⚡ Django REST Framework | REST APIs |
| 🗄 SQLite | Database |
| 🔍 Django Filter | Filtering APIs |

---

# 📂 Project Structure

```
Todo_Backend/
│
├── tasks/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── todo_backend/
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# 🧠 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/tasks/` | Retrieve All Tasks |
| GET | `/api/tasks/<id>/` | Retrieve Single Task |
| POST | `/api/tasks/` | Create Task |
| PUT | `/api/tasks/<id>/` | Update Complete Task |
| PATCH | `/api/tasks/<id>/` | Update Selected Fields |
| DELETE | `/api/tasks/<id>/` | Delete Task |

---

# 🔍 Search

```
GET /api/tasks/?search=django
```

Searches in:

- Title
- Description

---

# 🎯 Filter

Filter by Priority

```
GET /api/tasks/?priority=High
```

Filter by Status

```
GET /api/tasks/?status=Completed
```

---

# 📊 Ordering

Ascending

```
GET /api/tasks/?ordering=due_date
```

Descending

```
GET /api/tasks/?ordering=-created_at
```

---

# 📄 Pagination

Default Page Size

```
5 Tasks per Page
```

Navigate pages

```
?page=2
```

---

# 📝 Sample JSON

### Request

```json
{
    "title":"Complete DRF Project",
    "description":"Finish CodSoft Internship Task",
    "priority":"High",
    "status":"Pending",
    "due_date":"2026-08-10"
}
```

---

### Response

```json
{
    "id":1,
    "title":"Complete DRF Project",
    "description":"Finish CodSoft Internship Task",
    "priority":"High",
    "status":"Pending",
    "due_date":"2026-08-10",
    "created_at":"2026-07-27T14:45:30Z"
}
```

---

# ✅ Validation

The API validates incoming requests before saving them.

✔ Title must contain at least **3 characters**

✔ Due Date cannot be in the past

✔ Priority accepts only:

- Low
- Medium
- High

✔ Status accepts only:

- Pending
- Completed

---

# ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/TO-DO-Backend.git
```

### Move into Project

```bash
cd TO-DO-Backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

# 📸 Screenshots

> Add screenshots here

- Django Admin - "https://github.com/CoderXash9/TO-DO-Backend/blob/main/admin_page.png?raw=true"
- API List View
- API Detail View
- POST Request
- Search
- Filter

---

# 💡 What I Learned

- Django Models
- Django ORM
- Django REST Framework
- ModelViewSet
- Serializers
- Routers
- CRUD APIs
- Filtering
- Searching
- Ordering
- Pagination
- Validation
- REST Architecture

---

# 🚀 Future Improvements

- JWT Authentication
- User Login
- User-specific Tasks
- Email Notifications
- Docker Support
- PostgreSQL
- Deployment on Render

---

# 👨‍💻 Developer

### **Ashwini Purohit**

Backend Developer | Django Developer | Python Enthusiast

⭐ If you like this project, don't forget to **Star** the repository!

---

<p align="center">

### ⭐ Star this Repository if you found it helpful!

Made with ❤️ using Django REST Framework

</p>
