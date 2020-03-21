import http.client

conn = http.client.HTTPConnection("test-shoppinghelper,housediy,lan")

payload = ""

headers = {
    'accept': "*/*",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Content-Length': "280",
    'Host': "test-shoppinghelper.housediy.lan",
    'Origin': "http://test-shoppinghelper.housediy.lan",
    'Proxy-Connection': "keep-alive",
    'Referer': "http://test-shoppinghelper.housediy.lan/swagger-ui.html",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "d1981f12-8615-4033-ace3-dd3168ed4127"
    }

conn.request("POST", "c,api,preOrder,1,fromCart", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))