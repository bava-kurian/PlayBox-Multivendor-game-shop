# PlayBox-Multivendor-game-shop

# E-commerce Platform for Gaming Products

## Description

This is an e-commerce platform built with Django, designed to allow users to buy and sell gaming consoles, games, and related hardware. Vendors can manage their products, including adding, editing, and removing items from their store.

## Features

- User authentication and profile management
- Vendor management with product CRUD (Create, Read, Update, Delete) operations
- Category hierarchy for products
- Product search and filtering
- Image upload for products
- Vendor-specific product listing

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or later
- PostgreSQL (or any preferred database)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/bava-kurian/PlayBox-Multivendor-game-shop.git
   cd playbox
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Update your database settings in `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '',
       }
   }
   ```

5. **Run migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

### Adding Categories

Run the `populate.py` script to add categories:

```sh
python populate.py
```
