from flask import Flask, render_template, redirect, request, jsonify
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from wtforms import SubmitField, FormField, TextAreaField, StringField
from wtforms.validators import DataRequired

import requests
import urllib
import base64

# straight from the wtforms docs:
class TelephoneForm(Form):

    email = StringField('Email', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])


class ContactForm(Form):

    contact_form = FormField(TelephoneForm)

    submit_button = SubmitField('Submit Form')


def create_app(configfile=None):
    app = Flask(__name__)
    # Flask-Appconfig is not necessary, but highly recommend =) https://github.com/mbr/flask-appconfig
    AppConfig(app, configfile)

    Bootstrap(app)
    app.config['SECRET_KEY'] = 'devkey'

    # in a real app, these should be configured through Flask-Appconfig
    PDS_OAUTH_ENDPOINT = 'http://my-tyk-instance.dev:8080/oauth/authorize/'
    PDS_OAUTH_TOKEN_ENDPOINT = 'http://my-tyk-instance.dev:8080/oauth/token/'

    PDS_CLIENT_ID = 'ffedab5c7d3549455af73176612cbb10'
    PDS_CLIENT_SECRET = 'ZjEzZmIyZTQtNGZlYy00YjliLTc3Y2QtYzI3MzdhZGQ2YTIy'
    CLIENT_CALLBACK = 'http://127.0.0.1:9190/token_callback/'

    REQUEST_STATE = '0807edf7d85e5d'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = ContactForm()
        form.validate_on_submit()  # to get error messages to the browser

        return render_template('index.html', form=form)

    @app.route('/pds/contacts/', methods=('GET', 'POST'))
    def request_authorization():
        try:

            pds_authorize_url = PDS_OAUTH_ENDPOINT + "?client_id=" + PDS_CLIENT_ID + \
                                "&response_type=code&state=" + REQUEST_STATE + \
                                "&redirect_uri=" + CLIENT_CALLBACK

            return redirect(pds_authorize_url)

        except Exception as e:
            return redirect('/')

    @app.route('/token_callback/', methods=('GET', 'POST'))
    def token_callback():
        try:
            if request.method == 'GET' and request.args.get('error'):

                return jsonify(response={
                    'status': False,
                    'message': request.args.get('error')
                })

            elif request.method == 'GET' and request.args.get('code') and request.args.get('code') != '':

                """
                Authorization code received
                """

                data = {'grant_type': 'authorization_code',
                        'client_id': PDS_CLIENT_ID,
                        'code': str(request.args.get('code')),
                        'redirect_uri': CLIENT_CALLBACK
                        }

                payload = urllib.urlencode(data)

                base64string = base64.encodestring(
                    '%s:%s' % (PDS_CLIENT_ID, PDS_CLIENT_SECRET)).replace('\n', '')

                headers = {
                    'authorization': "Basic " + base64string,
                    'cache-control': "no-cache",
                    'content-type': "application/x-www-form-urlencoded"
                }

                response = requests.post(url=PDS_OAUTH_TOKEN_ENDPOINT, data=payload, headers=headers)

                if response.status_code == 200:
                    user_data = get_user_data(response.json(), request.args.get('user_id'))
                    return jsonify({
                        'user_response': user_data
                    })
                else:
                    return jsonify({
                        'status': False,
                        'message': response.json()
                    })

        except ValueError as e:
            return jsonify(response={'Error': 'Value error'})
        except KeyError as e:
            return jsonify(response={'Error': 'Key error'})

    def get_user_data(token_data, user_id):
        user_data_url = "http://my-tyk-instance.dev:8080/api/v1/users/"+ str(user_id) + "/emails/"
        headers = {
            'authorization': "Bearer " + str(token_data['access_token']),
            'cache-control': "no-cache"
        }

        response = requests.request("GET", user_data_url, headers=headers)

        if response.status_code == 200:
            print(response.text)
            return response.json()
        else:
            return {'error': "Unable to retrieve user data",
                    'status': response.status_code}

    return app

if __name__ == '__main__':
    create_app().run(debug=True, port=9190)
