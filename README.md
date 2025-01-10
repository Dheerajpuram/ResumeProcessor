# Resume Upload and Data Extraction

This project is a simple Django-based application that allows users to upload a resume, extract key data from it (like name, email, phone number), and save the extracted information to a database.

## Features

- **File Upload:** Users can upload their resume (PDF file).
- **Data Extraction:** The app extracts key data from the resume like the candidate's name, email, and phone number.
- **Database Integration:** The extracted data is saved into a PostgreSQL database.
- **User Feedback:** Success and error messages are displayed based on the file upload status.

## Requirements

- Python 3.x
- Django 5.1.4+
- PostgreSQL
- Required Python packages:
  - `django`
  - `psycopg2`
  - `pymupdf`
  - `django-bootstrap4`
  - `requests`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ResumeProcessor.git
cd ResumeProcessor

##2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

##3. Install Dependencies

pip install -r requirements.txt

##4. Set Up PostgreSQL Database
	•	Create a new database in PostgreSQL:

CREATE DATABASE resume_processor;


 •	Update your settings.py with your PostgreSQL database credentials under the DATABASES setting:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume_processor',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



5. Apply Migrations

Run the following command to create necessary database tables:

python manage.py makemigrations
python manage.py migrate

6. Run the Development Server

Start the development server by running:

python manage.py runserver

Access the app by opening your browser and going to:

http://127.0.0.1:8000/

