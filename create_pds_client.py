import requests
import json

# url to pds application on AppScale, modify if necessary
pds_url = 'http://192.168.33.10:8080/oauth/clients/create/'

payload = {
    'client_name': 'Test Client',
    'redirect_uri': "http://127.0.0.1:9190/token_callback/"
}
headers = {
    'Content-Type': "application/json"
}

try:
    # Request to Create to create client
    pds_response = requests.request("POST", pds_url, data=json.dumps(payload), headers=headers)

    if pds_response.status_code == 200:
        print "Client created on PDS at AppScale!"

        received_json_data = json.loads(pds_response.text)

        print pds_response.text

        client_id = received_json_data['client_id']
        client_secret = received_json_data['client_secret']
        redirect_uri = received_json_data['redirect_uri']
    else:
        print pds_response.status_code
        print "Unable to create client"
except Exception as e:
    print e.message

