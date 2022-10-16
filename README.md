# Getting started
___
**Open your cmd, then clone the project**  
```
cd *your_directory*
git clone https://github.com/DJsega1/django-intensive.git
cd django-intensive
```  

**Create and start a virtual environment**  
```
python -m venv venv
venv\Scripts\activate.bat
```

**Install the project dependencies**  
```
pip install -r requirements.txt
```

**For the site to work correctly, create .env file in the project directory (path should be "django-intensive/.env")**  
**Write in it the following variables (if you want to add some hosts, write separate it by whitespace):**
```
SECRET_KEY = 'django-insecure-i7u1s+!d05n8$%l^&+r!wl%=b7)rkx$af98$u(jowvs2q8u-n@'
DEBUG = True
ALLOWED_HOSTS = '127.0.0.1, '
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
