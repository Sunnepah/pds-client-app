# from django.core import serializers
# from django.http import HttpResponse
from iupds import settings

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.shortcuts import redirect

import requests
import urllib
import base64


def index(request):
    return render(request, 'user/signup_form.html', {"foo": "bar"},
                  content_type="application/xhtml+xml")


@api_view(['GET'])
def request_authorization(request):
    try:
        pds_authorize_url = settings.PDS_OAUTH_ENDPOINT

        pds_authorize_url = pds_authorize_url + "?client_id=" + settings.PDS_CLIENT_ID +\
                            "&response_type=code" \
                            "&state=" + settings.REQUEST_STATE + \
                            "&redirect_uri=" + settings.CLIENT_CALLBACK

        print pds_authorize_url

        return redirect(pds_authorize_url)

    except Exception as e:
        print e.message
        return Response({'response': 'No content'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def request_token(request):
    try:
        r = requests.post(settings.PDS_API_ENDPOINT,
                          data={'response_type': 'code',
                                'client_id': settings.PDS_CLIENT_ID,
                                'redirect_uri': settings.CLIENT_CALLBACK,
                                })
        print r.content
        print settings.PDS_API_ENDPOINT
        return Response({
            'status': r.status_code,
            'response': r.content
        }, status=r.status_code)
    except Exception as e:
        print e.message
        return Response({'response': 'No content'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def token_callback(request):
    try:
        if request.method == 'GET' and 'error' in request.GET:
            return Response({
                'status': False,
                'message': 'User denied authorization'
            }, status=status.HTTP_404_NOT_FOUND)

        elif request.method == 'GET' and 'code' in request.GET and request.GET['code'] != '':

            """
            Authorization token received
            """

            data = {'grant_type': 'authorization_code',
                    'client_id': settings.PDS_CLIENT_ID,
                    'code': str(request.GET['code']),
                    'redirect_uri': settings.CLIENT_CALLBACK
                    }
            print data
            payload = urllib.urlencode(data)

            base64string = base64.encodestring('%s:%s' % (settings.PDS_CLIENT_ID, settings.PDS_CLIENT_SECRET)).replace('\n', '')
            print base64string

            headers = {
                'authorization': "Basic " + base64string,
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded"
            }

            response = requests.post(url=settings.PDS_OAUTH_TOKEN_ENDPOINT, data=payload, headers=headers)

            if response.status_code == 200:
                print(response.text)
                return Response({
                    'status': True,
                    'token_response': response.json()
                }, status=status.HTTP_200_OK)
            else:
                print(response.text)
                return Response({
                    'status': False,
                    'message': str(response.text)
                }, status=response.status_code)

    except ValueError as e:
        print e.message
        return Response({'Error': 'Value error'}, status=status.HTTP_404_NOT_FOUND)
    except KeyError as e:
        print e.message
        return Response({'Error': 'Key error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def test(request):
    return Response({
        'status': 'ok'
    })


def get_user_data(token_data):
    import requests

    url = "http://my-tyk-instance.dev:8080/api/v1/users/1/emails/"

    headers = {
        'authorization': "Bearer "+str(token_data['access_token']),
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print(response.text)
        return response.json()
