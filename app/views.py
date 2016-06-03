from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required
from subreddit import generate_user_suggestions
from . import app


class PredictForm(Form):
    """Fields for Predict"""
    username = fields.StringField('Reddit Username:', validators=[Required()])

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    prediction = None
    subs = []
    alternate_subs = []
    
    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        username = submitted_data['username']

        subs, alternate_subs = generate_user_suggestions(username)

    return render_template('index.html', form=form, subs=subs, alternate_subs = alternate_subs)
