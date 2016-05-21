import requests
import json

url = "http://my-tyk-instance.dev:8080/tyk/oauth/clients/create"

# api_id - ID of the API you created on Tyk API Gateway
payload = '{"api_id": "f8dda7f3475e48b741b137f32df9a8d5", "redirect_uri": "http://127.0.0.1:9190/token_callback/"}'

# get x-tyk-authorization code which is the node_secret
# from /opt/tyk-gateway/tyk.conf on tyk server
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'x-tyk-authorization': "352d20ee67be67f6340b4c0605b044b7",
    }

# request to create OAuth client on Tyk
response = requests.request("POST", url, data=payload, headers=headers)

if response.status_code == 200:
    received_json_data = json.loads(response.text)
    print(received_json_data)

    # will print out
    # {"client_id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "secret":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    #     "redirect_uri":"http://127.0.0.1:9190/token_callback"}

    pds_url = 'http://192.168.33.10:8080/clients/create/notify/'
    payload = {
        'client_id': received_json_data['client_id'],
        'client_secret': received_json_data['secret'],
        'redirect_uri': received_json_data['redirect_uri'],
        'client_name': 'Test Client'
    }
    headers = {
        'Content-Type': "application/json"
    }
    # Request to Notify AppScale of the newly created client
    pds_response = requests.request("POST", pds_url, data=json.dumps(payload), headers=headers)

    if pds_response.status_code == 200:
        print pds_response.text
        print "Client created on PDS at AppScale!"
    else:
        print pds_response.text

else:
    print(response.text)