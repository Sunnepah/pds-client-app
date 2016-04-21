# iupds-appengine-django

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/).*

* Fork this repository.
* `$ git clone  git@github.com:<your username>/third-party-iupds.git`
* `$ mkvirtualenv third-party-iupds`
* `$ cd third-party-iupds/`
* `$ pip install -r requirements-local.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ gulp default`
* `$ python manage.py migrate`
* `$ python manage.py runserver`