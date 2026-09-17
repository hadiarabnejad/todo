# Todo Project

A Django-based todo application starter project with a simple coming-soon landing page and a ready-to-expand app structure.

## Project Structure

```text
.
├── .venv/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core_app/
│   ├── templates/
│   │   └── core_app/
│   │       └── coming_soon.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.x
- Django 6.1.1
- SQLite database (included by default)

The dependencies are listed in `requirements.txt`.

## Setup

1. Open a terminal in the project folder:

   ```bash
   cd d:\WEBS\todo
   ```

2. Activate the virtual environment:

   ```bash
   .\.venv\Scripts\activate
   ```

3. Install dependencies if needed:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

## Run the Project

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Current Status

This project currently includes:

- Django project configuration
- A `core_app` app
- A simple coming-soon landing page

## Next Steps

You can expand this into a full todo application by adding:

- Todo models
- Task creation and deletion
- Edit/update actions
- User authentication
- Templates and styling
- Database migrations for app-specific models

## Useful Commands

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## License

This project is for learning and development purposes.
