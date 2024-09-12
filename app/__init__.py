# Импортируем необходимые модули
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# Создаём объект Flask
app = Flask(__name__)
# Устанавливаем секретный ключ
app.config['SECRET_KEY'] = 'your_secret_key'
# Настраиваем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Создаём объект SQLAlchemy
db = SQLAlchemy(app)
# Создаём объект Bcrypt
bcrypt = Bcrypt(app)
# Создаём объект LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Модуль будет перенаправлять пользователя на маршрут, который мы указываем (на авторизацию)
# Импортируем маршрут (файл из пакета)
from app import routes