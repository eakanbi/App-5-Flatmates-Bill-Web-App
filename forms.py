from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired



class BillForm(FlaskForm):
    amount = StringField("Bill Amount: ", 
                         default="100", validators=[DataRequired()])
    period = StringField("Bill Period: ", 
                         default= 'December 2022', validators=[DataRequired()])

    name1 = StringField("Name: ", default="Mary", 
                        validators=[DataRequired()])
    days_in_house1 = StringField("Days in the House: ", 
                                 default="25",validators=[DataRequired()])

    name2 = StringField("Name: ", default="John")
    days_in_house2 = StringField("Days in the House: ", default="28", 
                                 validators=[DataRequired()])

    button = SubmitField("Calculate")