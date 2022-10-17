# Getting started
**Open your cmd, then clone the project**  
```
cd *your_directory*
git clone https://github.com/DJsega1/django-intensive.git
cd django-intensive
```  

**Create an virtual environment**  
```
python -m venv venv
```
**If you use Windows, activate venv with this:**
```
venv\Scripts\activate
```
**If you use Linux/Mac, activate venv with this:**
```
source venv/Scripts/activate
```

**Install the project dependencies**  
```
pip install -r requirements.txt
```

**For the site to work correctly, create .env file in the project directory (path should be "django-intensive/.env")**  
**Write in it the following variables (if you want to add some hosts, separate it by whitespace):**
```
SECRET_KEY = '{your_secret_key}'
DEBUG = *True or False*
ALLOWED_HOSTS = '{host1} {host2}'
```

**To start the development server on**  
```
cd intensive
python manage.py runserver
```  
The project starts on **127.0.0.1:8000** by default.  
If you want to change that, read the docs:  
https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver  
**Press Ctrl+C in order to stop the server.**
