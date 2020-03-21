# coding:utf-8

import time


def test_baidu_01(browser):
    browser.get("https://www.baidu.com")
    time.sleep(2)
    t = browser.title
    assert "百度" in t
