from flask import Flask,render_template,request,url_for
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5
import csv

app = Flask(__name__)
app.secret_key = "pooja"
Bootstrap5(app)
tasks = []

class MyForm(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    time = StringField("time(hrs)",validators=[DataRequired()])
    submit = SubmitField("submit")


@app.route("/",methods = ["GET","POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        time = form.time.data
        with open("data.csv",mode = "a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name,time])
        return  redirect(url_for("content"))
    return render_template("index.html",form = form)



@app.route("/content")
def content():
    form = MyForm()
    tasks = []
    try:
        with open("data.csv",mode = "r") as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader):
                tasks.append({"index":index,"name":row[0],"time":row[1]})
    except FileNotFoundError:
        pass        
    return render_template("content.html",tasks = tasks,form = form)

@app.route("/delete/<int:task_index>", methods=["POST"])
def delete_task(task_index):
    tasks = []
    # Read all tasks except the one to delete
    with open("data.csv", mode="r") as file:
        reader = csv.reader(file)
        tasks = [row for i, row in enumerate(reader) if i != task_index]

    # Write the updated list back to the CSV file
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
    
    return redirect(url_for("content"))

if __name__ == "__main__":
    app.run(debug=True)

