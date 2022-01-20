from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

todos = ["Learn Flask", "Setup venv", "Build a cool app"]

class AddTodo(FlaskForm):
    todo = StringField("Add a Todo", validators=[DataRequired()])
    add = SubmitField("Add Todo")

class RemoveTodo(FlaskForm):
    removalnum = IntegerField("Remove a Todo", validators=[DataRequired()])
    remove = SubmitField("Remove Todo")


@app.route('/', methods=["GET", "POST"])
def index():
    #instantiate the form
    todo_form = AddTodo()
    remove_form = RemoveTodo()

    #handle todo adding
    if todo_form.validate_on_submit(): #form validation to prevent blank submissions
        new_todo = todo_form.todo.data #accessing form data through the form instance
        todos.append(new_todo) #appending form data to list
    #handle todo removal 
    elif remove_form.validate_on_submit():
        if len(todos) >= remove_form.removalnum.data: #check to make sure the list item at the user's removal index exists
            todos.pop(remove_form.removalnum.data - 1) #remove the item from the list

    return render_template('index.html', todos=todos, template_form=todo_form, template_form2=remove_form)