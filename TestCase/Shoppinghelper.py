# coding:utf-8

from Common import MysqlUtil
from Common import OpHTTP
from Common import CommFiles
from Config import ReadConfig

rConfig = ReadConfig.ReadConfig()
ophttp = OpHTTP.OpHTTP()
mysqlUtil = MysqlUtil.MysqlUtil()
commfiles = CommFiles.CommFiles()

class Shoppinghelper():

    def __init__(self):
        # self.http_info = rConfig.get_testhttp()
        # self.http_url = self.http_info['test_shoppinghelper']
        self.http_url = rConfig.get_http()
        self.token = commfiles.test_app_token()

    '''
    APP扫描配电系统二维码请求预支付
    '''
    def test_preOrder_fromQrCode(self):
        headers = {
            "token": self.token
        }
        payload = {
            "id": "196957278583652352"
        }
        url = self.http_url + "shoppinghelper/c/api/preOrder/1/fromQrCode"
        response = ophttp.send_request(url, method="post", json=payload, headers=headers)
        return response

if __name__ == '__main__':
    t = Shoppinghelper().test_preOrder_fromQrCode()
    print(t)
