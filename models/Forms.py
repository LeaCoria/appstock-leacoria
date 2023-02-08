from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Regexp


class SignUpForm(Form):
    email = StringField('email', validators=[
        InputRequired(message="Enter an email"),
        Regexp(r"[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+[.][a-z]{2,3}$",
               message="Enter a valid email")
    ])
    password = PasswordField('password', validators=[
        InputRequired(message="Enter a password"),
        Regexp(r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$",
               message="""The password must contain at least 1 uppercase
               character, 1 lowercase character, 1 digit, and  a length of
               at least 6 charaters """)
    ])
    username = StringField('username', validators=[
        InputRequired(message="Enter an username"),
        Length(max=20, message="""The username must not be over than
               20 characteres""")
    ])
    name = StringField('name', validators=[
        InputRequired(message="Enter your name"),
        Length(max=20, message="""Your name must not be over than
               30 characteres""")
    ])
    lastname = StringField('lastname', validators=[
        InputRequired(message="Enter your lastname"),
        Length(max=20, message="""Your lastname must not be over than
               30 characteres""")
    ])


class RegisterItemForm(Form):
    cod = StringField('cod', validators=[
        InputRequired(message="Enter a code"),
        Length(max=30, message="The code can not be over than 30 characteres")
    ])
    name = StringField('name', validators=[
        InputRequired(message="Enter a name"),
        Length(max=50, message="The name can not be over than 30 characteres")
    ])
    brand = StringField('brand', validators=[
        InputRequired(message="Enter a brand"),
        Length(max=30, message="The brand can not be over than 30 characteres")
    ])
    quantity = StringField('quantity', validators=[
        InputRequired(message="Enter a quantity"),
        Regexp(r'^[0-9]+$',
               message="The quantity must be an integer number greater than 0")
    ])


class SubstractQuantityForm(Form):
    quantity_to_substract = StringField('quantity_to_substract', validators=[
        InputRequired(message="Enter a quantity"),
        Regexp(r'^[1-9]+[0-9]*$',
               message="The quantity must be an integer number greater than 0")
    ])


class AddQuantityForm(Form):
    quantity_to_add = StringField('quantity_to_add', validators=[
        InputRequired(message="Enter a quantity"),
        Regexp(r'^[1-9]+[0-9]*$',
               message="The quantity must be an integer number greater than 0")
    ])
