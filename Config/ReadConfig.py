# coding:utf-8

import os
import codecs
import configparser


# 获取cfg的文件路径
cfgpath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cfgpath, "cfg.ini")


# 读取cfg配置文件
class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self):
        smtp_server = self.cf.get("Email", "smtp_server")
        port = self.cf.get("Email", "port")
        sender = self.cf.get("Email", "sender")
        psw = self.cf.get("Email", "psw")
        email = {'setp_sever': smtp_server,
                 'port': port,
                 'sender': sender,
                 'psw': psw
        }
        return email

    def get_database(self):
        host = self.cf.get("DATABASE", "host")
        port = self.cf.get("DATABASE", "port")
        username = self.cf.get("DATABASE", "username")
        password = self.cf.get("DATABASE", "password")
        database = self.cf.get("DATABASE", "database")

        db = {'host': host,
              'port': port,
              'username': username,
              'password': password,
              'database': database
        }
        return db

    def get_http(self):
        http = self.cf.get("HTTP", "http")
        return http

    def get_testhttp(self):
        test_cms = self.cf.get("TESTHTTP", "test_cms")
        test_config = self.cf.get("TESTHTTP", "test_config")
        test_decoration = self.cf.get("TESTHTTP", "test_decoration")
        test_distribution = self.cf.get("TESTHTTP", "test_distribution")
        test_good = self.cf.get("TESTHTTP", "test_good")
        test_marketing = self.cf.get("TESTHTTP", "test_marketing")
        test_order = self.cf.get("TESTHTTP", "test_order")
        test_payment = self.cf.get("TESTHTTP", "test_payment")
        test_postsale = self.cf.get("TESTHTTP", "test_postsale")
        test_price = self.cf.get("TESTHTTP", "test_price")
        test_search = self.cf.get("TESTHTTP", "test_search")
        test_shoppinghelper = self.cf.get("TESTHTTP", "test_shoppinghelper")
        test_supplychain = self.cf.get("TESTHTTP", "test_supplychain")
        test_user = self.cf.get("TESTHTTP", "test_user")
        http = {
                'test_cms': test_cms,
                'test_config': test_config,
                'test_decoration': test_decoration,
                'test_distribution': test_distribution,
                'test_good': test_good,
                'test_marketing': test_marketing,
                'test_order': test_order,
                'test_payment': test_payment,
                'test_postsale': test_postsale,
                'test_price': test_price,
                'test_search': test_search,
                'test_shoppinghelper': test_shoppinghelper,
                'test_supplychain': test_supplychain,
                'test_user': test_user
        }
        return http

