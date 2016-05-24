# pds-client Set Up

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/), [PDS running on AppScale](https://github.com/Sunnepah/iupds-appscale).*

Fork this repository.
* `$ git clone  git@github.com:<your username>/pds-client-app.git`
* `$ cd pds-client-app`
* `$ virtualenv venv`
* `$ source venv/bin/activate`
* `$ pip install -r requirements.txt # installs flask, flask_bootstrap`

Read the comments in create_pds_client.py before running the script
* `$ python create_pds_client.py     # PDS on AppScale and Tyk server must be running`

Using the client's credentials created in previous step, update client_id, client_secret and redirect_uri in pds-client.py 
* `$ python pds-client.py`


Now head over to http://127.0.0.1:9190/ to view the application.