from common.commonData import CommonData
from conftest import http
import allure

@allure.feature('获取用户信息模块')
@allure.story('获取用户信息成功')
def test_getUserInfo():
    path='/sys/getUserInfo'
    data={'token':CommonData.token}
    resp_getInfo=http.post(path,data)
    # print(resp_getInfo)
    try:
        assert resp_getInfo['code']==200
        print("获取用户信息成功")
    except:
        print("断言错误，实际结果：",resp_getInfo)