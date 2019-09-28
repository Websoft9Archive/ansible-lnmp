# 高级：Apache&Nginx动静分离

## 路径

## 应用程序
应用程序目录: /data/wwwroot/default  
default是应用程序的默认目录，其中的index.html是引导文件，可以删除

### 运行环境（PHP 7.0,Apache 2.4.8） 

- PHP配置文件目录: /usr/local/php/etc  
- PHP 扩展配置文件目录: /usr/local/php/etc/php.d  
- Apache目录：/usr/local/apache  
- Apache虚拟主机目录: /usr/local/apache/conf/vhost  
- 日志文件目录：/usr/local/apache/logs  

### 数据库（MySQL5.6.3）
- Database目录: /usr/local/mysql or /usr/local/mariadb
- Database 数据目录: /data/mysql or /data/mariadb
- Database 配置文件: /etc/my.cnf
- 数据库面板访问路径：*http://公网ip/phpmyadmin*

### 运维面板（9panel）

9Panel是Websoft9根据镜像用户的习惯和技术能力而研制的轻量级面板，以帮助用户快速掌握程序安装和运维工作  
访问路径：http://ip/9panel


## 主要特点

* 基于系统源码编译安装，细节安全优化，纯命令行，占用系统资源低
* Jemalloc优化MySQL内存管理
* 交互添加Apache虚拟主机，方便快捷，支持Let’s Encrypt一键设置
* 菜单式FTP账号管理脚本，轻松建立ftp虚拟用户
* 提供在线MySQL、PHP、Redis、Memcached、phpMyAdmin升级脚本
* 提供本地备份和远程备份（服务器之间rsync）、内网阿里云OSS备份功能

## 使用手册

请下载后阅读：http://libs.websoft9.com/Websoft9/documents/zh/lanmp/lanmp.zip