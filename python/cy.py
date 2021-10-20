#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import uuid
import time
import re
from xml.dom.minidom import parse, parseString

# cookie
def session():
    session = str(uuid.uuid1()).replace('-', '')
    return session

# aidc1
def times():
    times = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return times

# 重定向url
def fyu():
    headers = {
    'User-Agent': 'CDMA+WLAN(Maod)',
    }
    url='http://www.msftconnecttest.com/redirect'
    r = requests.get(url, headers=headers)
    xmlresult = (r.content.decode("utf-8"))
    return(xmlresult)

# 服务器地址
def acname():
    p = re.compile(r'wlanacname=([^&]*)')
    return(p.findall(fyu()))

# 本机ip
def ipv4():
    p = re.compile(r'userip=([^]]*)')
    return(p.findall(fyu()))

def login(user,password):
    # 接口
    user = user
    password = password
    cookies = {
    'JSESSIONID': session(),
    }

    headers = {
        'User-Agent': 'CDMA+WLAN(Maod)',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    params = (
        ('aidcauthtype', '0'),
        ('wlanacname', acname()),
        ('wlanuserip', ipv4()),
    )
    data = {
        'UserName': '!^Adcm0' + user,
        'PassWord': password, 
        'AidcAuthAttr1': times(),
        'AidcAuthAttr3': 'VNdRYxtO',
        'AidcAuthAttr4': 'AZYCIkQWCs3skFXnr5oNtQ%3D%3D',
        'AidcAuthAttr5': 'VMtWYxlXAbCShlTi1I8KsbyvVia%2FRiyhjeFKpuOBr1z6',
        'button': 'Login',
        'createAuthorFlag': '0'
    }
    # 登陆地址
    url = 'http://58.53.199.144:8001/wispr_auth.jsp?'
    a = requests.post(url, headers=headers, params=params, data=data)
    b = a.content.decode("utf-8")
    x = re.compile(r'<ReplyMessage>([^<]*)')
    y = re.compile(r'<ResponseCode>([^<]*)')
    w = x.findall(b)
    z = y.findall(b)
    if z == ['50']:
        return('认证成功',':',z)
    else:
        return w
