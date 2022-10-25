# Getting started
## Open your cmd, then clone the project
```
cd *your_directory*
git clone https://github.com/DJsega1/django-intensive.git
cd django-intensive
```  
## Create an virtual environment
**Windows with Bash**
```
python -m venv venv
```
**Linux/Mac**
```
python3 -m venv venv
```
  
## Activate virtual enviroment
**Windows with Bash**
```
. venv/Scripts/activate
```
**Linux/Mac**
```
source venv/bin/activate
```

## Install the project dependencies
**Windows with Bash**
```
pip install -r requirements.txt
```
**Linux/Mac**
```
pip3 install -r requirements.txt
```
## Setting environment
**Create .env file and set variables like in .env example:**
```
SECRET_KEY=NOT_SO_SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```
## Start the development server
**Windows with Bash**
```
python manage.py runserver
```  
**Linux/Mac**
```
python3 manage.py runserver
```
___
The project starts on **127.0.0.1:8000** by default.  
If you want to change that, read the docs:  
https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver  
**Press Ctrl+C in order to stop the server.**
