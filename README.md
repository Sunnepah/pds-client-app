# iupds-appengine-django

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/).*

* Fork this repository.
* `$ git clone  git@github.com:<your username>/pds-client-app.git`
* `$ mkvirtualenv pds-client-app`
* `$ cd pds-client-app/`
* `$ pip install -r requirements-local.txt`
* `$ python manage.py migrate`
* `$ python manage.py runserver`