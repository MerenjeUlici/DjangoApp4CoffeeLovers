# DjangoApp4CoffeeLovers
This app will be a locator for coffee in Skopje

Python version: 3.8.14
Django version: 3.2

Set appropriate python version, for example, using pyenv:
```
pyenv install 3.8.14
pyenv local 3.8.14
```

Create virtual environment:
```
python -m venv venv
pip install --upgrade pip
```

Install requirements:
```
pip install -r requirements.txt
```

Start server:
```
python manage.py runserver
```

Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

Create super user:
```
python manage.py createsuperuser
```

Install nodejs and npm on Ubuntu:
```
curl -sL https://deb.nodesource.com/setup_14.x -o setup_14.sh
sudo sh ./setup_14.sh
sudo apt install nodejs
sudo npm i -g npx
```