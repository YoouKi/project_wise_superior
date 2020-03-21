# -*- coding:utf-8 -*-


from os import environ
import requests
from logs import MyLogger


class OpHTTP:
    def __get(self, url, params=None, **kwargs):
        '''
        根据传入的数据进行get请求调用
        :param url:请求url地址
        :param params:get参数
        :param kwargs:其他参数
        :return:返回的是一个dict类型的数据
        （1）200：请求正常，返回json格式的数据
        格式：result = {"resultCode": 200, "message": "请求成功，返回json格式的数据", "content": responce.json()}
        （2）201：请求正常，返回string类型的数据
        格式： result = {"resultCode": 201, "message": "请求成功，返回string格式的数据","content": responce.text}
        （3）300：response的status code 不等于200，content为空字符串
        格式：result = {"resultCode": 300, "message": "接口请求的状态码错误-非200", "content": ""}
        （4）400：请求过程出现异常，content为空字符串
        格式：result = {"resultCode": 400, "message": "接口请求过程出现异常", "content": ""}
        '''
        try:
            responce = requests.get(url, params, timeout=environ.get("timeout"), **kwargs)
            if responce.status_code == 200:
                # 判断返回的结果是否是json格式的数据：通过headers的Content-Type来获取接口返回数据格式
                # 如果是json格式的数据，那么返回包含json对象的结果，否则返回content
                if "application/json" in responce.headers.get("Content-Type"):
                    result = {"resultCode":200,"message":"请求成功，返回json格式的数据","content":responce.json()}
                else:
                    result = {"resultCode":201,"message":"请求成功，返回string格式的数据",
                              "content":responce.text} #responce.text:根据接口返回的信息，会自动将原始数据转换成字符串类型的数据，格式是根据headers里面来转的
            else:
                result = {"resultCode": 300, "message": "接口请求的状态码错误-非200", "content": ""}
        except BaseException as  e:
            MyLogger.info("[http_requests_get_info] - url=%s,params=%s,**kwargs=%s" % (url, params, kwargs)) #打印出get请求的参数信息
            MyLogger.exception(e)
            result = {"resultCode": 400, "message": "接口请求过程出现异常", "content": ""}
        finally:
            return result

    def __post(self, url, data=None, json=None, headers=None, **kwargs):
        '''
        根据传入的数据进行post请求调用
        :param url:请求url地址
        :param data:参数
        :param json:json格式的参数
        :param kwargs:其他参数
        :return:返回的是一个dict类型的数据
        （1）200：请求正常，返回json格式的数据
        格式：result = {"resultCode": 200, "message": "请求成功，返回json格式的数据", "content": responce.json()}
        （2）201：请求正常，返回string类型的数据
        格式： result = {"resultCode": 201, "message": "请求成功，返回string格式的数据","content": responce.text}
        （3）300：response的status code 不等于200，content为空字符串
        格式：result = {"resultCode": 300, "message": "接口请求的状态码错误-非200", "content": ""}
        （4）400：请求过程出现异常，content为空字符串
        格式：result = {"resultCode": 400, "message": "接口请求过程出现异常", "content": ""}
        '''
        try:
            responce = requests.post(url, data=data, json=json, headers=headers, timeout=environ.get("timeout"), **kwargs)
            if responce.status_code == 200:
                if "application/json" in responce.headers.get("Content-Type"):
                    result = {"resultCode": 200, "message": "请求成功，返回json格式的数据", "content": responce.json(), "headers": responce.headers}
                else:
                    result = {"resultCode": 201, "message": "请求成功，返回string格式的数据",
                              "content": responce.text}  # responce.text:根据接口返回的信息，会自动将原始数据转换成字符串类型的数据，格式是根据headers里面来转的
            else:
                result = {"resultCode": 300, "message": "接口请求的状态码错误-非200", "content": ""}
        except BaseException as e:
            MyLogger.info("[http_requests_post_info] - url=%s,params=%s,json=%s,kwargs=%s]" % (url, data, json, kwargs)) #打印出post请求的参数信息
            MyLogger.exception(e)
            result = {"resultCode": 400, "message": "接口请求过程出现异常", "content": ""}
        finally:
            return result

    # 发送http请求，根据你传入的method参数决定执行get还是post请求
    def send_request(self, url, method="post", params=None, data=None, json=None, headers=None, **kwargs):
        '''
        根据你传入的method参数决定执行get还是post请求
        :param url: 接口地址
        :param method: post（默认）或者get，小写，如果传入post，则使用post的方式发送http请求，如果传入get，则使用get的方式发送请求
        :param params: dict类型的参数(还有其他类型等)，使用get（带参数）方式发送http请求的时候需要传入，默认None
        :param data: dict类型的参数，默认为None，使用post（带参数）方式发送http请求的时候传入
        :param json: json格式的参数，默认为None，使用post（带参数）方式发送http请求的时候传入
        :param kwargs:---headers：cookies：auth：timeout（本类已经在配置文件中进行读取）：allow_redirects：proxies：stream
        :return:返回的是一个dict类型的数据
        （1）200：请求正常，返回json格式的数据
        格式：result = {"resultCode": 200, "message": "请求成功，返回json格式的数据", "content": responce.json()}
        （2）201：请求正常，返回string类型的数据
        格式： result = {"resultCode": 201, "message": "请求成功，返回string格式的数据","content": responce.text}
        （3）300：response的status code 不等于200，content为空字符串
        格式：result = {"resultCode": 300, "message": "接口请求的状态码错误-非200", "content": ""}
        （4） 301:调用自定义方法传入的参数有问题
        格式：{"resultCode": 301, "message": "传入参数值错误", "content": ""}
        （5）400：请求过程出现异常，content为空字符串
        格式：result = {"resultCode": 400, "message": "接口请求过程出现异常", "content": ""}

        '''
        try:
            if method == "post":
                result = self.__post(url=url, data=data, json=json, headers=headers, **kwargs)
            elif method == "get":
                result = self.__get(url=url, params=params, **kwargs)
            else:
                result = {"resultCode": 301, "message": "传入参数值错误", "content": ""} #方法的入参有错误，无法正常解析
        except BaseException as  e:
            result = {"resultCode": 400, "message": "接口请求过程出现异常", "content": ""}
            MyLogger.info("def send_request(self,url=%s,method=%s,params=%s,data=%s,json=%s,**%s)" % (url, method, params, data, json,headers, kwargs))
            MyLogger.exception(e)
        return result

