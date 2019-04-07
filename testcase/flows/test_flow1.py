from conftest import http
from common.commonData import CommonData
import pytest
class Test_flow1:
    """登录
    注册    userId
    查看    1.用户列表第一条记录昵称是否为你所填昵称 2.userId是否与注册返回userId一致
    查看用户详情
    """
    @pytest.mark.debug
    def test_flow1(self):

    #注册
        data_register={'token': CommonData.token,
              "nickName":CommonData.register_NickName,
              "userName":CommonData.register_userName,
              "telNo":"",
              "email":"",
              "address":"",
              "roleIds":"",
              "regionId":1,
              "regionLevel":1}
        resp_register=http.post('/user/saveOrUpdateUser',data_register)
        # assert resp_register['code']==200
        # assert resp_register['msg']=='操作成功'

    #新用户登录
        data_newUser={
            'userName':CommonData.register_userName,
            'password':CommonData.password
        }
        resp_newlogin=http.post('/sys/login',data_newUser)
        assert resp_newlogin['code']==200
        assert resp_newlogin['msg']=='操作成功'

    #加载用户列表
        data_loadUserList = {
	        "pageCurrent": 1,
	        "pageSize": 10,
	        "nickName": "",
	        "userName": "",
	        "regionId": 1
        }
        resp_loadUserList = http.post('/user/loadUserList', data_loadUserList)
        assert resp_loadUserList['code'] == 200
        assert resp_loadUserList['msg'] == '操作成功'
        assert resp_newlogin['object']['userId'] == resp_loadUserList['object']['list'][0]['id']
        assert CommonData.register_NickName == resp_loadUserList['object']['list'][0]['nickName']

    #查看用户详情
        data_userInfo = {
            'id':resp_newlogin['object']['userId']
        }
        resp_getInfo = http.post('/user/loadUserInfo', data_userInfo)
        # print(resp_getInfo)
        assert resp_getInfo['code'] == 200
        assert resp_getInfo['msg'] == '操作成功'




#登录
    # def test_login_success(self):
    #     data={
    #         'userName':CommonData.mobile,
    #         'password':CommonData.password
    #     }
    #     resp_login=http.post('/sys/login',data)
    #     assert resp_login['code']==200
    #     assert resp_login['msg']=='操作成功'
    #     assert resp_login['object']['userId']==140
    #
    # #注册
    # def test_register_success(self):
    #     data={"nickName":"asdf",
    #           "userName":"15735518552",
    #           "telNo":"",
    #           "email":"",
    #           "address":"",
    #           "roleIds":"",
    #           "regionId":1,
    #           "regionLevel":1}
    #     resp_login=http.post('/user/saveOrUpdateUser',data)
    #     assert resp_login['code']==200
    #     assert resp_login['msg']=='操作成功'
    #     print(resp_login['nickName'])
    #     return resp_login['nickName']
    #
    # @pytest.mark.usefixtures("test_getUserInfo")
    # #新用户登录
    # def test_newUserlogin_success(self):
    #     data={
    #         'userName':15735518552,
    #         'password':CommonData.password
    #     }
    #     resp_login=http.post('/sys/login',data)
    #     assert resp_login['code']==200
    #     assert resp_login['msg']=='操作成功'
    #     return resp_login['object']['userId']
    #
    # #查看用户详情
    # @pytest.fixture()
    # def test_getUserInfo(self):
    #
    #     yield
    #     userId = self.test_newUserlogin_success
    #     path = '/sys/getUserInfo'
    #     data = {'token': CommonData.token}
    #     resp_getInfo = http.post(path, data)
    #     # print(resp_getInfo)
    #     assert resp_getInfo['code'] == 200
    #     assert resp_getInfo['msg'] == '操作成功'
    #     assert resp_getInfo['userId']==userId
    #     assert resp_getInfo['nickName']=='asdf'