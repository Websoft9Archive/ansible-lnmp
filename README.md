## 变量说明
mysql,php版本可以选，另外还有其他变量
* mysqlver是mysql版本变量，包含55/56/57,默认版本为: 56
* mysql_password是mysql密码变量，默认为: 123456
* remote是是否开启远程连接变量，值为yes/no，默认为: no
* phpver是php版本变量，包含54 55 56 70 71 72，默认: 70

在awx中YAML调用方式参考（注意空格）

mysqlver: 56
phpver: 70

### 如何增加java支持？

运行如下命令，重启即可

~~~
yum install tomcat-* -y && systemctl enable tomcat
~~~

## 其他事项
安装Certbot时 可能会报错 忽略即可 加入了错误处理
