import requests
import json
def jiemi():
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

def jiami():
    url = "http://10.5.254.242:50000/encrypt/api/v1/sm4/encrypt"
    date = \
        {
            "encryptId": "a4aba1f353ed11ec8658745aaa412d5c",
            "data": [{
                "name": "张彩凤",
                "idcard": "15010519780408904X"
            }, {
                "phone": "13347111105"
            }]
        }

    # date_json = json.dumps(date)
    print(date)
    response = requests.post(url=url, json=date)
    print(response.text)

jiami()
jiemi()