# coding:utf-8

from Common import MysqlUtil
from Common import OpHTTP
from Config import ReadConfig
from Common import CommFiles
from TestCase import Order


rConfig = ReadConfig.ReadConfig()
ophttp = OpHTTP.OpHTTP()
mysqlUtil = MysqlUtil.MysqlUtil()
commfiles = CommFiles.CommFiles()
order = Order.Order()


class Payment():
    def __init__(self):
        self.token = commfiles.test_app_token()
        self.http_url = rConfig.get_http()
        self.orderId = order.test_Order_createOrder().get("content")["data"]["id"]

    '''
    支付订单
    '''
    def test_payment_payCommit(self):
        headers = commfiles.test_app_headers()
        payload = {
            "orderId": self.orderId,
            "payOrderType": "1",
            "useSubsidy": "2",
            "paymentType": "11",
            "platform": "WEIXIN_APP",
            "useBalance": "1",
            "paymentAmount": "45111.33"
        }
        url = self.http_url + "payment/c/api/payment/1/payCommit"
        response = ophttp.send_request(url, method="post", json=payload, headers=headers)
        return response


if __name__ == '__main__':
    p = Payment().test_payment_payCommit()
    print(p)