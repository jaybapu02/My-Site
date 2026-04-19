# 🌐 My-Site

A personal **Django-based portfolio website** showcasing projects, skills, certifications, and contact details. This project demonstrates full-stack web development using Django, static assets, and dynamic content rendering.

---

## 🚀 Features

* 🏠 Personal portfolio homepage
* 📁 Projects showcase section
* 🧠 Skills and technologies display
* 📞 Contact form functionality
* 📄 Resume and certification downloads
* 🎨 Static assets (images, PDFs, media)
* ⚙️ Django admin panel support

---

## 🏗️ Project Structure

```bash id="1s9k2m"
My-Site/
│
├── manage.py
│
├── mysite/                # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── jay/                   # Core application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── template/              # HTML templates
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   ├── project.html
│   ├── skills.html
│   ├── nav_bar.html
│   └── fotter.html
│
├── static/                # Static files (images, PDFs)
│   ├── images
│   ├── certificates
│   └── resume files
│
├── staticfiles/           # Collected static files (production)
│
└── db.sqlite3             # Database
```

*(Structure based on your project files )*

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash id="b2k9zv"
git clone https://github.com/your-username/My-Site.git
cd My-Site
```

### 2️⃣ Create virtual environment

```bash id="o9x4pl"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash id="z3m1ac"
pip install django
```

### 4️⃣ Apply migrations

```bash id="q7h2ye"
python manage.py migrate
```

### 5️⃣ Run the server

```bash id="p8u6rt"
python manage.py runserver
```

Open in browser:

```id="m4n2kl"
http://127.0.0.1:8000/
```

---

## 📸 Pages Included

* Home
* About
* Skills
* Projects
* Contact

---

## 🧑‍💻 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite

---

## 📌 Future Improvements

* Add responsive design improvements
* Integrate email sending in contact form
* Add animations and modern UI
* Deploy using cloud platforms

---

## 👨‍💻 Author

**Jaychandra Das**

---

## ⭐ Contribution

Feel free to fork this repository and contribute.

---

## 📄 License

This project is for personal and educational purposes.
