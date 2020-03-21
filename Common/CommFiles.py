# coding:utf-8
from TestCase import User


class CommFiles():
    def __init__(self):
        self.u = User.User()

    def test_web_headers(self):
        """
        获取web端的headers
        :return:
        """
        response = self.u.test_post_login()
        headers = dict(response.get("headers"))
        return headers

    def test_app_headers(self):
        """
        获取app端headers
        :return:
        """
        response = self.u.test_phone_login()
        headers = response.get("headers")
        return headers

    def test_app_token(self):
        """
        获取APP端token
        :return:
        """
        response = self.u.test_phone_login()
        token = response.get("content")["data"]["token"]
        return token

    def test_app_headers(self):
        headers = {
            "token": self.test_app_token(),
            "Accept": "application/json",
            "Timestamp": "1565767243",
            "AppVersion": "3.3.8",
            "OS": "ios",
            "Accept-Language": "zh-Hans-CN;q=1",
            "platform": "MALL_APP",
            "Accept-Encoding": "gzip, deflate",
            "DeviceId": "B2DC753D-3BCF-423A-B5FF-87CF1A4EAE97",
            "Content-Length": "58",
            "User-Agent": "YouJiaTest/3.3.8 (iPhone; iOS 12.3.1; Scale/2.00)",
            "Content-Type": "application/json",
            "OsVersion": "12.3.1",
            "Connection": "keep-alive"
        }
        return headers
