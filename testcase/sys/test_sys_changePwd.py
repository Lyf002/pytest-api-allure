import pytest
from common.commonData import CommonData
from conftest import http
import allure

@allure.feature('修改密码模块')
class Test_changePwd:

    @allure.story('修改密码成功')
    @pytest.mark.usefixtures("test_resetPwd")
    def test_changePwd(self):
        path='/sys/changePwd'
        data={
            'token':CommonData.token,
            'userId':140,
            'userName':CommonData.mobile,
            'oldPwd':CommonData.password,
            'password':'123123'
        }
        resp_changePwd=http.post(path,data)
        # print(resp_getInfo)
        assert resp_changePwd['code']==200
        assert resp_changePwd['msg']=='操作成功'

    @pytest.fixture()
    def test_resetPwd(self):

        yield
        path = '/sys/changePwd'
        data = {
            'token': CommonData.token,
            'userId': 140,
            'userName': CommonData.mobile,
            'oldPwd': '123123',
            'password': CommonData.password
        }
        resp_changePwd = http.post(path, data)
        # print(resp_getInfo)
        assert resp_changePwd['code'] == 200
        assert resp_changePwd['msg'] == '操作成功'