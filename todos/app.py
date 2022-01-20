from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

todos = ["Learn Flask", "Setup venv", "Build a cool app"]

class TodoForm(FlaskForm):
    todo = StringField("Todo to Add", validators=[DataRequired()])
    add = SubmitField("Add Todo")
    removalnum = IntegerField("Todo to Remove", validators=[DataRequired()])
    remove = SubmitField("Remove Todo")

@app.route('/', methods=["GET", "POST"])
def index():
    todo_form=TodoForm()
    if todo_form.validate_on_submit():
        new_todo=todo_form.todo.data
        todos.append(new_todo)
    #elif 'removalnum' in request.form:
        #todos.pop('removalnum')
    return render_template('index.html', todos=todos, template_form=todo_form)