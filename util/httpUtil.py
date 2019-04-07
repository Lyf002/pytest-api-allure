import requests
import json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers={'Content-Type': 'application/json;charset=UTF-8'}

    def post(self,path,data):
        proxies = CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data)
        # headers = {}
        # headers['Content-Type'] = 'application/json;charset=UTF-8'
        self.headers['token']=CommonData.token
        resp_login = self.http.post(url=host+path,
                         proxies=proxies,
                         data=data_json,
                         headers=self.headers)
        assert resp_login.status_code==200
        resp_json=json.loads(resp_login.text)       #dict转json
        return resp_json





