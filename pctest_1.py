import requests
import json

headers = {"Authorization": "Basic c2FpdHJvbi14Z3ltbm1JbmZvOmlOelUwT2RrdFlXOEV0TmpRek9TMDBPV05qMjNnZGhl"}

response = requests.post('http://8.140.146.161:4005/oauth/token?grant_type=client_credentials', headers=headers,
                         verify=False)
data = json.loads(response.text)['access_token']
data = "Bearer " + data
print(data)
header = {"Authorization": data}

url = 'http://8.140.146.161:4005/api/getOrgVaccinateReport'
data_1 = {
    "dateTimeEnd": "2021-04-03 08:00:00",
    "dateTimeStart": "2021-04-03 08:00:00",
    "page": 1,
    "size": 10
}

rp = requests.post('http://8.140.146.161:4005/api/getOrgVaccinateReport', headers=header, data=json.dumps(data_1),
                   verify=False)
print(rp.text)
