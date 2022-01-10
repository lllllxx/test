import requests


def fx():
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'x-wif-nonce': 'QkjjtiLM2dCratiA',
        'x-wif-signature': '1C505E0C6E4CD2B6659B070AC11B03AD0AEDBF1C43F0DD3C2558C00D84C1DB74',
        'x-wif-timestamp': '1641810174',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'x-wif-paasid': 'smt-application',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'http://bmfw.www.gov.cn',
        'Referer': 'http://bmfw.www.gov.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = '{"appId":"NcApplication","paasHeader":"zdww","timestampHeader":"1641810174","nonceHeader":"123456789abcdefg","signatureHeader":"23E25E96CDD58DFFA5E2D64C6A6FC343464E47A3457407B1CF42493CBF3C7ACC","key":"3C502C97ABDA40D0A60FBEE50FAAD1DA"}'

    response = requests.post('http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson', headers=headers,
                             data=data, verify=False)
    return (response.text)
