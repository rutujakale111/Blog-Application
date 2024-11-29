# Django Blog Application

A simple and functional blog application built with Django. This project allows users to create, read, update, and delete blog posts. It also includes user authentication features, such as login, signup, and logout.

---

## Features

- **User Authentication**
  - Signup, Login, and Logout functionality.
- **CRUD Operations**
  - Create, Read, Update, and Delete blog posts.
- **Post Management**
  - Manage posts with detailed views.
- **Admin Panel**
  - Customizable Django admin panel for managing posts and users.

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS.
- **Database:** SQLite (default Django database)
- **Tools:** Postman (for API testing)

---

## Installation

### Prerequisites
- Python 3.x installed
- Django installed (`pip install django`)
- Git (optional, for cloning the repository)

### Steps

1. **Clone the Repository**
   
   git clone https://github.com/rutujakale111/Blog-Application
   cd django-blog-app
2. **Install Dependencies**

pip install -r requirements.txt
3. **Set Up the Database**

python manage.py makemigrations
python manage.py migrate
4. **Run the Development Server**

python manage.py runserver
Access the Application

Open a web browser and navigate to http://127.0.0.1:8000/.
API Endpoints (for REST Framework)
Base URL: /api/
List All Posts
GET /posts/

Create a New Post
POST /posts/

Retrieve a Specific Post
GET /posts/<post_id>/

Update a Post
PUT /posts/<post_id>/

Delete a Post
DELETE /posts/<post_id>/

Project Structure

blog_project/
├── blog_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── blog_app/
│   │       ├── base.html
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── post_confirm_delete.html
│   ├── views.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── admin.py
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
Customization
Admin Panel
**Access the Django admin panel at http://127.0.0.1:8000/admin/. Use the following command to create a superuser:**

python manage.py createsuperuser