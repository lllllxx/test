import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'x-wif-nonce': 'QkjjtiLM2dCratiA',
    'x-wif-signature': 'CE05E80852AFD16F3FEDF3D8AF4D26CFE071AB72C66723096698861F24D375A7',
    'x-wif-timestamp': '1640598747',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'x-wif-paasid': 'smt-application',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'http://bmfw.www.gov.cn',
    'Referer': 'http://bmfw.www.gov.cn/',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

data = '{"appId":"NcApplication","paasHeader":"zdww","timestampHeader":"1640598747","nonceHeader":"123456789abcdefg","signatureHeader":"EC4F61E09FBCD447C4CF201815EAAC61A7A40A6538632FF7FA3C0F1FF8B7CB79","key":"3C502C97ABDA40D0A60FBEE50FAAD1DA"}'

response = requests.post('http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson', headers=headers, data=data, verify=False)
print(response.text)