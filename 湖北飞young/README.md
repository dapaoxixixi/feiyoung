说明 以openwrt为例
===========================

## fy 联网脚本 将其放入/bin文件夹下，并增加权限
```
  cd /bin   chmod u+x fy
```
### *或用winscp直接修改权限
![auto](https://github.com/dapaoxixixi/hubeifeiyoung/blob/main/%E6%B9%96%E5%8C%97%E9%A3%9Eyoung/2.png)
## fy.conf fy配置文件 将其放入/etc文件夹下，并增加权限
```
  cd /etc   chmod u+x fy.conf
```
## 每分钟自动执行一次，确保开机有网，监测断网重连， 文本复制到计划任务里里
```
  * * * * * /bin/py
```
![auto](https://github.com/dapaoxixixi/hubeifeiyoung/blob/main/%E6%B9%96%E5%8C%97%E9%A3%9Eyoung/0.png)



# 自行配置好fy.conf文件，服务器地址，手机号，和31天的安卓端抓包密码，即post请求里%21%5EAdcm0后面跟着的16位
