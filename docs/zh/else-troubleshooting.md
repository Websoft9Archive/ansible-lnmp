# 故障处理

故障处理主要通过日志文件进行分析，从某种程度上，处理故障就是解读日志文件。

我们收集使用 LNMP 过程中最常见的故障，供您参考：

## 网站类

#### 网站显示重定向错误？

检查网站根目录下的 *.htaccess* 文件，分析其中的重定向规则，找到其中的死循环。

## 数据库类

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### 数据库日志文件太大，导致磁盘空间不足？

默认安装，mysql会自动开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MySQL 配置文件](/zh/stack-components.md#mysql)，注释掉 binlog 日志
  ~~~
  #log-bin=mysql-bin  
  ~~~
2. 重启mysql
  ~~~
  systemctl restart mysqld
  ~~~

#### phpMyAdmin 出现 Error during session...错误？

Error during session start; please check your PHP and/or webserver log file and configure your PHP installation properly. Also ensure that cookies are enabled in your browser. session_start(): open(SESSION_FILE, O_RDWR) failed: Permission denied (13)

**问题原因**：系统更新后，PHP 的 session.save_path 路径目录的权限设置不正确。  
**解决方案**：打开WinSCP，运行如下命令即可
~~~
chown -R root:nginx /var/lib/php/session
echo 'chown nginx. -R /var/lib/php' >> /etc/cron.daily/0yum-daily.cron
~~~


## Nginx类

#### 重启 Nginx 服务显示 *No spaces...*

出现此信息的时候，重启服务是成功的。

#### 502 错误？

Nginx应用服务器出现502错误的原因很多，但是基本都是资源不够造成的。 包括：内存不足，CPU超标，硬盘满了，另外可能也有程序导致php-fpm停止运行。对应的的解决办法：

*   内存和CPU超标，通过重启一下php-fpm 和nginx mysql 三个服务可以临时解决，如果是1核1g的配置且经常出现502错误的话，建议升级
*   硬盘满了的话，会导致MySQL停止服务，需要进行硬盘扩容
*   php-fpm服务停止或者报错也会出现502，需要重启php-fpm

#### 413 Request Entity Too Large

## 服务器类

服务器以及网络相关故障的诊断和解决，与云平台密切相关，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)