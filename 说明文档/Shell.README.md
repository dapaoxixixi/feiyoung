## 💻 路由器版版说明文档

- 用WinScp将三个文件上传到 /bin 文件夹


```
直接用WinSCP属性设置权限
```


<img width="600" alt="上传文件" src="https://github.com/dapaoxixixi/feiyoung/blob/main/Image/s1.png">

<img width="600" alt="上传文件" src="https://github.com/dapaoxixixi/feiyoung/blob/main/Image/2.png">


- 如图，把帐号和31天密码填入userprofile.txt文件，并保存


<img width="600" alt="修改文件" src="https://github.com/dapaoxixixi/feiyoung/blob/main/Image/4.png">


- 在路由器的计划任里设置每半分钟启动一次脚本，如图


```
* * * * * /bin/cy
* * * * * sleep 30; /bin/cy
```


<img width="600" alt="设置脚本" src="github.com/dapaoxixixi/feiyoung/blob/main/Image/3.png">


## 👏 现在就可以享受7*24小时不间断网络服务啦
