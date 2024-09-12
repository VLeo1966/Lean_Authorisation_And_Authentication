```markdown
# Теория на сегодня:

## 1. Что будет на уроке. Создание формы

Сегодня мы продолжим наше изучение веб-разработки, сосредоточившись на теме аутентификации и авторизации. В ходе этого урока:

- разберём, что такое авторизация и аутентификация;
- научимся использовать Flask для реализации авторизации и аутентификации;
- разработаем небольшой проект с регистрацией пользователей на нашем сайте.

### Аутентификация

Аутентификация — это процесс проверки личности пользователя. Примеры аутентификации включают:

- ввод логина и пароля;
- сравнение введенных данных с данными в базе данных.

Если данные совпадают, то пользователь допускается к системе.

### Авторизация

Авторизация — это процесс определения того, какие действия может выполнять пользователь на сайте. Различные уровни доступа включают:

- **администратор**: имеет доступ к дополнительным страницам и функциям;
- **обычный пользователь**: ограничен в доступе к определенным страницам.

Авторизация управляет тем, какие права и возможности есть у конкретного пользователя.

### Идентификация

Идентификация — это процесс определения личности пользователя.

На этом уроке мы сосредоточимся на аутентификации и авторизации.

## Инструменты

Перед тем как перейти к разработке, рассмотрим инструменты, которые помогут нам безопасно реализовать аутентификацию и авторизацию во Flask:

- **Flask-Login**: библиотека для управления сеансами пользователей;
- **Werkzeug Security**: модуль для безопасного хеширования паролей;
- **Flask-WTF**: для создания и обработки форм.

---

## Начало работы с Flask и расширением SQLAlchemy

### Установка необходимых пакетов

1. **Flask** — это микрофреймворк для разработки веб-приложений на Python.
2. **Flask-SQLAlchemy** — расширение для работы с базами данных.

#### Установка через терминал:

```bash
pip install Flask
pip install Flask-SQLAlchemy
```

### Создание приложения Flask

1. Импортируем модули:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
```

2. Создаём приложение и настраиваем базу данных:

```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```

---

## Определение модели базы данных

### 1. Создание модели `User`:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

### 2. Создание базы данных:

```python
with app.app_context():
    db.create_all()
```

### 3. Работа с базой данных: добавление пользователей

Создаём маршрут для добавления пользователей:

```python
@app.route('/add_user')
def add_user():
    new_user = User(username='new_username')
    db.session.add(new_user)
    db.session.commit()
    return 'User added'
```

---

## Использование Flask-WTF для работы с формами

### Установка пакета:

```bash
pip install flask-wtf
```

### 1. Импортируем модули:

```python
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
```

### 2. Создаём форму:

```python
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

### 3. Создание маршрута для отображения формы:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('hello', name=name))
    return render_template('index.html', form=form)
```

---

## Заключение

Сегодня мы рассмотрели:

- основные концепции аутентификации и авторизации;
- использование Flask для создания веб-приложений с аутентификацией;
- работу с формами через Flask-WTF и валидацию данных.
```