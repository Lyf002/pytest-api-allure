import sys
sys.path.append('D:/自动化测试/py_workspace/Discuz_autoTestFrame')



from conftest import http
from common.commonData import CommonData
import allure

@allure.feature('登录模块')
class Test_login:

    #用户名密码正确
    @allure.story('登录成功')
    def test_login_success(self):
        data={
            'userName':CommonData.mobile,
            'password':CommonData.password
        }
        resp_login=http.post('/sys/login',data)
        assert resp_login['code']==200
        assert resp_login['msg']=='操作成功'
        assert resp_login['object']['userId']==140

    #用户名不存在
    @allure.story('用户名不存在进行登录')
    def test_login_uNameErr(self):
        data={
            'userName':'15735518550',
            'password':CommonData.password
        }
        resp_login=http.post('/sys/login',data)
        assert resp_login['code']==301
        assert resp_login['msg']=='用户不存在'

    # 密码错误
    @allure.story('密码错误进行登录')
    def test_login_uPwdErr(self):
        data = {
            'userName': CommonData.mobile,
            'password': '123789'
        }
        resp_login = http.post('/sys/login', data)
        assert resp_login['code'] == 410
        assert resp_login['msg'] == '用户名或密码错误'

    # 用户名为空
    @allure.story('用户名为空进行登录')
    def test_login_uNameNull(self):
        data = {
            'userName': '',
            'password': CommonData.password
        }
        resp_login = http.post('/sys/login', data)
        assert resp_login['code'] == 301
        assert resp_login['msg'] == '账号不能为空'

    # 密码为空
    @allure.story('密码为空进行登录')
    def test_login_uPwdNull(self):
        data = {
            'userName': CommonData.mobile,
            'password': ''
        }
        resp_login = http.post('/sys/login', data)
        assert resp_login['code'] == 410
        assert resp_login['msg'] == '用户名或密码错误'

    # 用户名参数找不到
    def test_login_uNameNone(self):
        data = {
            'password': CommonData.password
        }
        resp_login = http.post('/sys/login', data)
        assert resp_login['code'] == 301
        assert resp_login['msg'] == '用户不存在'

    # 密码参数找不到
    @allure.story('密码参数找不到进行登录')
    def test_login_uPwdNone(self):
        data = {
            'userName': CommonData.mobile
        }
        resp_login = http.post('/sys/login', data)
        assert resp_login['code'] == 500