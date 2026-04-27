#  Django Blog Website

A fully functional blog web application built with **Python** and **Django** as part of my web development learning journey.

---

##  About The Project

This is a blog website where users can read posts. The project is built using the Django framework and demonstrates core web development concepts including URL routing, views, templates, forms, and the Django admin panel.

---

##  Features

-  **Blog Posts** – View and read blog articles
-  **Django Admin Panel** – Manage posts and content easily through the built-in admin interface
-  **Forms** – Interactive forms for user input
-  **Database Integration** – Data stored and managed using Django's ORM
-  **Django Templates** – Clean and structured HTML rendering

---

##  Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.x | Backend programming language |
| Django | Web framework |
| SQLite | Database |
| HTML/CSS | Frontend templates |

---

##  Project Structure

```
Web-project-1/
│
├── Abicir/
│   └── testwebsite/
│       ├── manage.py
│       ├── testwebsite/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       └── ...
```

---

##  Getting Started

Follow these steps to run the project locally:

### Prerequisites

- Python 3.x installed
- pip installed

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/santhana2006ea/Web-project-1.git
   cd Web-project-1
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for Admin Panel)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

##  Author

**Santhana Eswari**  
B.Tech Information Technology Student  
 Tamil Nadu, India  
 [GitHub](https://github.com/santhana2006ea)

---

##  Learning Source

This project was built by following a **Udemy** course on Python Django Web Development.

---

##  Note

This is a learning project built to understand Django fundamentals. More features and improvements will be added as I continue to grow my skills! 
