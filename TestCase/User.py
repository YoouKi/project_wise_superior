# coding:utf-8

from Common import MysqlUtil
from Common import OpHTTP
from Config import ReadConfig

rConfig = ReadConfig.ReadConfig()
ophttp = OpHTTP.OpHTTP()
mysqlUtil = MysqlUtil.MysqlUtil()



class User():
    def __init__(self):
        # self.http_info = rConfig.get_testhttp()
        # self.http_url = self.http_info['test_user']
        self.http_url = rConfig.get_http()

    def test_user_verificationCode(self, tel):
        """
        C端获取登陆验证码
        """
        url = self.http_url + "user/c/api/sms/1/verificationCode/{tel}".format(self=self, tel=tel)
        # #请求不带参数的get方法
        ophttp.send_request(url, method="get")

    def test_phone_login(self):
        """
        C端用户登陆
        """
        sql = 'SELECT content FROM re_sms_record WHERE tel = "18613226004" ORDER BY update_time Desc'
        Code = mysqlUtil.mysql_getstring(sql)
        payload = {
            "tel": "18613229000",
            "verificationCode":Code
        }
        url = self.http_url + "user/c/api/home/1/phone"
        headers = {
            "platform": "MALL_APP",

        }
        response = ophttp.send_request(url, method="post", json=payload, headers=headers)
        return response

    def test_post_login(self):
        """
        Web端用户登陆
        :return:
        """
        payload = {
            "tel": "18613226004",
            "password": "123456"
        }
        url = self.http_url + "user/w/api/1/login"
        response = ophttp.send_request(url, method="post", json=payload)
        return response


if __name__ == '__main__':
    User().test_user_verificationCode(18613229000)
    response = User().test_phone_login()
    print(response.get('headers'))
    print(type(response))
    print(response)
    token = response.get("content")["data"]["token"]
    print(token)
