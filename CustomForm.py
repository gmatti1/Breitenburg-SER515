from wtforms import Form, StringField, PasswordField, TextAreaField, validators, FileField
from wtforms.fields.html5 import EmailField

# Register Form Class
class RegisterForm(Form):
    name_field = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email_field = EmailField('Email', [validators.DataRequired(), validators.Length(min=6, max=50)])
    password_field = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm_field', message='Passwords do not match')])
    confirm_field = PasswordField('Confirm Password')

class LoginForm(Form):
    email_field = StringField('Email')
    password_field = PasswordField('Password')

class CreatePostForm(Form):
    title_field = StringField('Title', [validators.DataRequired(), validators.Length(min=1, max=50)])
    body_field = TextAreaField('Body', [validators.DataRequired(), validators.Length(min=1, max=5000)])

class EditPostForum(Form):
    post_field = StringField('Post_id', [validators.DataRequired(), validators.Length(min=1, max=50)])

class BlockUserForm(Form):
    email_field = StringField('Email')

class UpdateAccountForm(Form):
    name_field = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    password_field = PasswordField('Password')
    email_field = EmailField('Email', [validators.DataRequired(), validators.Length(min=6, max=50), validators.Email()])
    dob_field = StringField('Date of birth')
    gender = StringField('Gender')
    address_field = StringField('Address', [validators.DataRequired(), validators.Length(min=6, max=150)])
    phone_field = StringField('Phone', [validators.Length(min=10, max=10)])
    work_field = StringField('Work', [validators.Length(min=6, max=100)])
    education_field = StringField('Education', [validators.Length(min=6, max=150)])
    details_field= StringField('Other details', [validators.Length(min=6, max=250)])
    picture_field = FileField('Update Profile Picture')
