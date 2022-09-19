#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import uuid
import time
import re
import configparser
from xml.dom.minidom import parse, parseString

conf = configparser.ConfigParser()
conf.read('cy.ini', encoding='utf-8')

def session():
    session = str(uuid.uuid1()).replace('-', '')
    return session

def times():
    times = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return times

def fyu():
    headers = {
    'User-Agent': 'CDMA+WLAN(Maod)',
    }
    url='http://www.msftconnecttest.com/redirect'
    r = requests.get(url, headers=headers)
    xmlresult = (r.content.decode("utf-8"))
    return(xmlresult)

def info(): 
    conf['info']['acname'] = str(acname()[0])
    conf['info']['ipv4'] =  str(ipv4()[0])
    with open("cy.ini", "w+") as f:
        conf.write(f)

def acname():
    p = re.compile(r'wlanacname=([^&]*)')
    return(p.findall(fyu()))

def ipv4():
    p = re.compile(r'userip=([^]]*)')
    return(p.findall(fyu()))

def login(user,password):
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
        ('wlanacname', conf.get('info', 'acname')),
        ('wlanuserip', conf.get('info', 'ipv4')),
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

def logout():
    headers = {
        'User-Agent': 'CDMA+WLAN(Maod)',
    }
    params = (
        ('wlanacname', conf.get('info', 'acname')),
        ('wlanuserip', conf.get('info', 'ipv4')),
    )
    url = 'http://58.53.199.144:8001/wispr_logout.jsp'
    a = requests.post(url, headers=headers, params=params)
    b = a.content.decode("utf-8")
    y = re.compile(r'<ResponseCode>([^<]*)')
    z = y.findall(b)
    if z == ['150']:
        return('注销成功',':',z)
    else:
        return('注销失败',':',z)

