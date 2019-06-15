from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    title = StringField('Title',
        validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description',
        validators=[DataRequired(), Length(max=1000)])
    price = DecimalField('Price', validators=[DataRequired()])
    image_file = StringField('Image file', default='default.jpg')
    submit = SubmitField('Save')
