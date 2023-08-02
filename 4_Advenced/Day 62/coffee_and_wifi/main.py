from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
import csv
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location URL', validators=[DataRequired()])
    open_time = StringField('Open time', validators=[DataRequired()])
    close_time = StringField('Close time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', validators=[DataRequired()],
                                choices=['✘', '☕️', '☕☕️️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕☕️☕️☕️☕️️'])
    wifi_rating = SelectField('Wifi rating', validators=[DataRequired()],
                                choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪️️'])
    power_rating = SelectField('Power rating', validators=[DataRequired()],
                                choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌️'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    form = CafeForm()
    if form.validate_on_submit():
        form_data = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data,
                form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
        with open(r'cafe-data.csv', 'a', newline='', encoding="utf-8") as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow(form_data)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
