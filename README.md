# todo_app
This is a simple Flask-based web application that allows users to add tasks with their respective time duration. The tasks are stored in a CSV file and can be viewed and deleted.

# Task Tracker App

A simple Flask-based task tracker that allows users to add tasks with a name and time (in hours), view them, and delete tasks when needed. The app uses `Flask-WTF` for form handling, `Flask-Bootstrap` for styling, and stores data in a CSV file.

## Features

- Add tasks with a name and time.
- View a list of all tasks.
- Delete specific tasks.
- Data persistence using a CSV file.

## Technologies Used

- **Flask**: For building the web application.
- **Flask-WTF**: For handling form validation and input.
- **Flask-Bootstrap**: For easy and responsive styling.
- **WTForms**: For form creation and validation.
- **CSV**: For data storage.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Pooja389/todo_app.git
   cd todo_app
2. create a virtual environment to install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. install required package
   ```bash
   pip install flask flask-wtf flask-bootstrap
   ```
4.run the application
  ```bash
  python  app.py
      
