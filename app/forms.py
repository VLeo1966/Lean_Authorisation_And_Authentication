from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(min=2, max=35)], render_kw={"placeholder": "Введите ваше имя"})
    email = StringField('Почта', validators=[DataRequired(), Email()], render_kw={"placeholder": "Введите вашу почту"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Введите пароль"})
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Введите пароль"})
    submit = SubmitField('Регистрация')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Такая почта уже используется')

class LoginForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(min=2, max=35)], render_kw={"placeholder": "Введите ваше имя"})
    email = StringField('Почта', validators=[DataRequired(), Email()], render_kw={"placeholder": "Введите вашу почту"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Введите пароль"})
    remember = BooleanField('Запомни меня')
    submit = SubmitField('Войти')

class EditProfileForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(min=2, max=80)], render_kw={"placeholder": "Введите ваше имя"})
    email = StringField('Почта', validators=[DataRequired(), Email()], render_kw={"placeholder": "Введите вашу почту"})
    password = PasswordField('Новый пароль', validators=[Length(min=8, message="Пароль должен содержать минимум 8 символов")], render_kw={"placeholder": "Введите пароль"})
    confirm_password = PasswordField('Подтвердите пароль', validators=[EqualTo('password', message="Пароли должны совпадать")], render_kw={"placeholder": "Введите пароль"})
    submit = SubmitField('Сохранить изменения')