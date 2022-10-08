import flask_wtf
import wtforms


# Sign up for the first time ~ Register


class RegisterForm(flask_wtf.FlaskForm):
    first_name = wtforms.StringField("First Name")
    last_name = wtforms.StringField("Last Name")
    email_address = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    confirm_password = wtforms.PasswordField("Confirm Password")
    submit = wtforms.SubmitField("Submit")


# Sign in ~ User


class SignInForm(flask_wtf.FlaskForm):
    email = wtforms.EmailField("email")
    password = wtforms.PasswordField("Password")
    submit = wtforms.SubmitField("Sign in")


# Add new crop
crop_list = ["potato", "tomato"]
units_list = ["kg", "g", "units"]


class NewCrop(flask_wtf.FlaskForm):
    crop_name = wtforms.SelectField("Crop", choices=crop_list)
    sow_date = wtforms.DateField("Sow date")
    submit = wtforms.SubmitField("Submit")


class HarvestForm(flask_wtf.FlaskForm):
    crop_name = wtforms.SelectField("Crop", choices=crop_list)
    sow_date = wtforms.DateField("Sow date")
    harvest_date = wtforms.DateField("Harvest date")
    quantity = wtforms.IntegerField("Quantity")
    units = wtforms.SelectField("Units", choices=units_list)
    submit = wtforms.SubmitField("Submit")


class ContactForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name")
    contact_address = wtforms.EmailField("Email Adress")
    message = wtforms.TextAreaField("Message")
    send = wtforms.SubmitField("Send")
