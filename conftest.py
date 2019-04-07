import pytest
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonData
#session/module/class/function
http =HttpUtil()
@pytest.fixture(scope='session',autouse=True)
#全局初始化操作
def session_fixture():

    path_login="/sys/login"
    data_login={}
    data_login['userName']=CommonData.mobile
    data_login['password']=CommonData.password
    resp_login=http.post(path_login,data_login)

    # resp_dict = json.loads(resp_login.text)  # json转python dict

    CommonData.token = resp_login['object']['token']  # 获取token

    # try:
    #     assert resp_login['code'] == 200
    #     print("登录成功")
    # except:
    #     print("断言错误，实际结果：",resp_login)  #打印response的body值

    yield
    path_logout = "/sys/logout"
    data_logout = {}
    resp_logout = http.post(path_logout,data_logout)
    try:
        assert resp_logout['code']==200
        print("退出成功")
    except:
        print(resp_logout)



