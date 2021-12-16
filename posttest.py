import requests
import json
url = "http://10.5.254.242:50000/encrypt/api/v1/sm4/decrypt"
date = \
    {
        "encryptId": "a4ababd053ed11ec8658745aaa412d5c",
        "data": [{
            "name": "N+eUrTtH/TC7DOP4UXXMvw==",
            "idcard": "Nrq6mxb6r/Sw4ErXb6ns/gZJ0a5kWeyUHcWn69uRfLs="
        }, {
            "phone": "kwt5YEfDFPNSkTFPj2rMaQ=="
        }]
    }

# date_json = json.dumps(date)
print(date)
response = requests.post(url = url ,json = date)
print(response.text)
# help(requests)