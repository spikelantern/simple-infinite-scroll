# Simple infinite scroll example in Django

This is an example of a very simple infinite scroll implementation in Django.

I blogged about this here: https://spikelantern.com/articles/simple-infinite-scroll-in-django/

Hope this helps you!

## Installation

Create and activate a virtualenv like this (instructions may differ on Windows):

```
$ python -m venv myvenv
$ source myvenv/bin/activate
```

Install the requirements:

```
$ pip install -r requirements.txt
```

Run migrations:

```
$ python manage.py migrate
```

Now you can start the server:

```
$ python manage.py runserver
```

You can view the example at http://127.0.0.1:8000

# License

MIT
