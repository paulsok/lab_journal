# lab_journal
A simple project using the Django framework to keep a lab log.
All notes are organized by topics in which users can add their notes. The time when the note was written is indicated.
Each user has access only to his topics and notes.

## Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/paulsok/lab_journal.git
$ cd lab_journal
```

In order to create a superuser do this
```sh
$ python manage.py createsuperuser
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ python3 -m venv /path/to/new/virtual/environment
$ source env/bin/activate
```

Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd lab_journal
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
