# coding:utf-8

from Common import MysqlUtil
from Common import OpHTTP
from Config import ReadConfig
from Common import CommFiles

rConfig = ReadConfig.ReadConfig()
ophttp = OpHTTP.OpHTTP()
mysqlUtil = MysqlUtil.MysqlUtil()
commfiles = CommFiles.CommFiles()


class Order():
    def __init__(self):
        # self.token = commfiles.test_app_token()
        self.headers = commfiles.test_app_headers()
        self.http_url = rConfig.get_http()

    '''
    创建待支付订单
    '''
    def test_Order_createOrder(self):
        headers = commfiles.test_app_headers()
        payload = {
            "amount": "45111.33",
            "remark": "",
            "useCoin": "2",
            "addressId": "191196494680481792",
            "orderFrom": "4",
            "deliveryTime": "",
            "useZeroLoan": "2",
            "useValidAmount":"1",
            "skuList":[
            {
            "customizeFlag":"1",
            "skuCount":"2.234",
            "skuId":"446002664670167658",
            "estimatedDeliveryDay":"55",
            "skuType":"1"
            },
            {
            "customizeFlag":"2",
            "skuCount":"4",
            "skuId":"163242394700107776",
            "estimatedDeliveryDay":"20",
            "skuType":"1"
            },
            {
            "customizeFlag":"2",
            "skuCount":"50",
            "skuId":"164376269740462081",
            "estimatedDeliveryDay":"10",
            "skuType":"1"
            },
            {
            "customizeFlag":"2",
            "skuCount":"30",
            "skuId":"164374181782376449",
            "estimatedDeliveryDay":"10",
            "skuType":"1"
            },
            {
            "customizeFlag":"2",
            "skuCount":"100",
            "skuId":"162494893581160448",
            "estimatedDeliveryDay":"10",
            "skuType":"1"
            },
            {
            "customizeFlag":"2",
            "skuCount":"1",
            "skuId":"606765667915197658",
            "estimatedDeliveryDay":"6",
            "skuType":"1"
            },
            {
            "customizeFlag":"2",
            "skuCount":"2",
            "skuId":"312155635841917658",
            "estimatedDeliveryDay":"6",
            "skuType":"1"
            }
            ],
            "orderType":"11",
            "designerId":"136609432657555456"
            }
        url = self.http_url + "order/c/api/order/1/createOrder"
        response = ophttp.send_request(url, method="post", json=payload, headers=headers)
        return response



