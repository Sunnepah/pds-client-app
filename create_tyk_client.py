import requests, base64

# url = "http://my-tyk-instance.com:3000/oauth/clients/create"
#
# payload = "{\n    \"api_id\" : \"c089b27e0eb34908679e6c0a51a883ec\",\n    \"redirect_uri\" : \"http://third-party-app.dev:9190/api/v1/token_callback/\"\n}"
# headers = {
#     'content-type': "application/json",
#     'authorization': "983bc55e1c614a626dfdd2f302145411",
#     'cache-control': "no-cache",
#     'postman-token': "3e00ef07-b0e1-0db0-ef49-615a131879be"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)

import requests

url = "http://my-tyk-instance.dev:8080/pds-api-v1/oauth/token/"

payload = "grant_type=authorization_code&client_idcode=e5fd3e7a1594412b68e6659f06c42676" \
          "&code=_uSVdTDSTGeCx31yG5hiWg" \
          "&redirect_uri=http%3A%2F%2Fthird-party-app.dev%3A9190%2Fapi%2Fv1%2Ftoken_callback%2F"
headers = {
    'authorization': "Basic ZTVmZDNlN2ExNTk0NDEyYjY4ZTY2NTlmMDZjNDI2NzY6T1RKak1qWTNZelF0TkRJd015MDBNVFJtTFRjMk9EUXRNRE16TkRJMll6YzVaR0pt",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# basic_auth = base64.b64encode("e5fd3e7a1594412b68e6659f06c42676:OTJjMjY3YzQtNDIwMy00MTRmLTc2ODQtMDMzNDI2Yzc5ZGJm")
# print basic_auth + "\n"
