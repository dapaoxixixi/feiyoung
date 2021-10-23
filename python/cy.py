
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
