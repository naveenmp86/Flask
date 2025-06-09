from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import (
    DataRequired,
    Length,
    email,
    optional,
    equal_to
)

class Signup(FlaskForm):
    username=StringField(
        "Username",
        validators=[DataRequired(),Length(4,30)]
    )
    email=StringField(
        "Email",
        validators=[DataRequired(),email()]
    )
    gender=SelectField(
        "Gender",
        choices=["Male","Female","Other"],
        validators=[optional()]
    )
    DOB=DateField(
        "DOB",
        validators=[optional()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    confirm_password=PasswordField(
        "Confirm_Password",
        validators=[DataRequired(),Length(5,25),equal_to("password")]
    )
    submit=SubmitField("Sign-Up")
    

class Login(FlaskForm):
    email=StringField(
        "Email",
        validators=[DataRequired(),email()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    remember_me=BooleanField("Remember me")
    submit=SubmitField("Login")