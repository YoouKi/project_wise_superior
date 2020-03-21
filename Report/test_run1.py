# coding:utf-8
from TestCase import User

class TestClass:
    def test_one(self):
        User().test_user_verificationCode(18613229000)
        response = User().test_phone_login()
        print(response.get('headers'))
        print(type(response))
