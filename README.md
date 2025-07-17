# 🥗 Django Blog Of Food

A web-based food blog platform built with Django where users can explore, create, and share culinary posts. This project showcases Django’s full-stack capabilities including user authentication, CRUD functionality, and deployment using PythonAnywhere.

🔗 **Live Site**: [Visit the site](https://kyaraaves.pythonanywhere.com/)

---

## 📸 Preview

![BlogOfFood Screenshot](https://github.com/Kyara0797/Django-BlogOfFood/blob/main/media/uploads/reference_Blog_of_food.png)

---

## 📌 Features

- 📝 Create, update, and delete food-related blog posts.
- 🔐 User registration and login/logout system.
- 📂 Category-based blog navigation.
- 👩‍🍳 Admin dashboard for content management.
- 📱 Responsive design with Bootstrap.
- 🌐 Hosted on PythonAnywhere.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite (default)
- **Hosting**: PythonAnywhere

---

## 🚀 Installation (Local Setup)

### Prerequisites

- Python 3.x
- Virtualenv (recommended)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Kyara0797/Django-BlogOfFood.git
cd Django-BlogOfFood
```
# 2. Create and activate virtual environment
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

👩‍💻 **Project Structure**

blog_enterprise/
├── blog/                     # App containing the blog logic
├── blog_enterprise/         # Django project configuration
├── templates/               # HTML templates
├── static/                  # CSS, JS, and images
├── media/                   # Uploaded media files
├── db.sqlite3               # SQLite database (for development)
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies

⚙️ **Admin Access**
To access the Django admin dashboard:

# Create a superuser
python manage.py createsuperuser
Then visit http://127.0.0.1:8000/admin/ and log in with the credentials you just created.

🌐 **Deployment**
This project is deployed on PythonAnywhere.

