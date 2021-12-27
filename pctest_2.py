import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRzIjoiMGY5MWM3ZjM3M2U5NGYxMTgyMWRhMzk2ZDg5ZWRiN2UiLCJ1c2VyX25hbWUiOiLlhoXokpnlj6Toh6rmsrvljLoiLCJkZXB0SWQiOjE1MjkxMCwicm9sZXNTZXQiOiJbMTIxXSIsInVzZXJJZCI6MTc1LCJhdXRob3JpdGllcyI6WyJST0xFX0NPVklEX1BST1ZJTkNFIl0sImNsaWVudF9pZCI6IjBmOTFjN2YzNzNlOTRmMTE4MjFkYTM5NmQ4OWVkYjdlIiwic2NvcGUiOlsiYWxsIl0sImxvZ2luTmFtZSI6Im5tZ3p6cTEiLCJ0ZWwiOiIiLCJleHAiOjE2NDA2MDYzNjQsImp0aSI6ImRkZDBhZjlmLWJkYzctNDc3Zi1iNzQwLWY1NzRiNDFkNDE0MCIsIm1hbmFnZS5zZXJ2ZXIiOiJodHRwOi8vMTAuNS4yNTQuMjMyOjcwMDAvYWRtaW4ifQ.jFy0zJOr1Wif0Y3-maXBZjvJ5Sp9rFbBjJ1qWmB1Jzc',
    'Referer': 'http://10.5.254.206:9000/screen/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('code', '15'),
)

response = requests.get('http://10.5.254.206:9000/bigscreen/api/v1/medical/resource/fixedhospital/groupByCounty', headers=headers, params=params, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://10.5.254.206:9000/bigscreen/api/v1/medical/resource/fixedhospital/groupByCounty?code=15', headers=headers, verify=False)