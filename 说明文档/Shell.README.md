## 💻 路由器版版说明文档

- 用WinSCP将cy文件上传到 /bin 文件夹下 ， 将cy.conf文件上传到 /etc 文件夹下

```
cd命令进入/bin与/etc，将两个文件提升权限 chmod u+x  或者如果，直接用WinSCP属性设置
```

<img width="500" alt="上传文件" src="https://github.com/dapaoxixixi/feiyoung/blob/main/Image/op1.png">

- 如图，修改cy.conf，并保存

<img width="500" alt="修改文件" src="https://github.com/dapaoxixixi/feiyoung/blob/main/Image/op3.png">

- 在路由器的计划任务里设置每隔一分钟启动一次脚本，如图

```
* * * * * /bin/cy
```

<img width="500" alt="设置脚本" src="https://github.com/dapaoxixixi/feiyoung/blob/main/Image/op2.png">

## 👏 现在就可以享受7*24小时不间断网络服务啦
