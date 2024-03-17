from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email


class PropertyForm(FlaskForm):
    property_title = StringField("Property Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    rooms_number = IntegerField("No of Rooms", validators=[DataRequired()])
    bedrooms_number = IntegerField(
        "No of Bedrooms", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    property_type = SelectField("Property Type", choices=[(
        'house', 'House'), ('apartment', 'Apartment')], validators=[DataRequired()])
    location = TextAreaField("Location", validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png'], 'Upload a .png or .jpg file')])
