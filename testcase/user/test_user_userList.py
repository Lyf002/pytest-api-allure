import pytest
from common.commonData import CommonData
from conftest import http
class Test_loadUserList:
    # @pytest.mark.usefixtures("my_fixtures")
    def test_loadUserList(self):
        path='/user/loadUserList'
        data={
            "pageCurrent":1,
            "pageSize":10,
            "nickName":"",
            "userName":"",
            "regionId":1
        }
        resp_loadUserList=http.post(path,data)
        # print(resp_getInfo)
        assert resp_loadUserList['code']==200
        assert resp_loadUserList['msg']=='操作成功'
        # print(resp_loadUserList['object'])