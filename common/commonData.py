import random
class CommonData:
    host = "http://192.168.1.203:8083"
    mobile='15735518554'
    password='123456'
    token=None
    proxies = {'http': 'http://localhost:8888'}
    register_NickName=str(random.randint(10000000,100000000))
    register_userName="157"+register_NickName
