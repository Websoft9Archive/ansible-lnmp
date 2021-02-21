# FAQ

#### LEMP 与 LNMP 有何不同？

LEMP 就是 LNMP，是不同的用户采用的不同名称而已

#### 默认字符集是什么？
UTF-8

#### Nginx 虚拟主机配置文件是什么？

虚拟主机配置文件是 Nginx 用于管理多个网站的**配置段集合**，路径为：*/etc/nginx/conf.d/default.conf*。  
每个配置段的形式为： `server{ }`，有多少个网站就有多少个配置段

#### LNMP 环境中默认有伪静态模板吗？

已经内置了部分常用网站的伪静态规则文件，进入目录可以查看
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/lnmp-multi/lnmp-rewrite-1-websoft9.png)

#### 如何修改示例网站根目录？

示例网站路径信息 */data/wwwroot/www.example.com* 存放在 [Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx)中

#### LNMP 环境是否支持部署多个网站？

支持。每增加一个网站，只需在[Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx)中增加对应的 **server{ }** 即可。

#### 如果没有域名是否可以部署 LNMP？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

```
sudo docker stop phpmyadmin
```

#### 网站源码路径如何修改？

通过修改 [Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx) 中相关路径参数

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### 通过 SFTP 上传网站源码后是否需要修改拥有者权限？

不需要，LNMP 会自动修正

#### 如何重置 php.ini 文件？

[下载 php.ini 模板](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) 后覆盖你服务器上的 */ect/php.ini*

#### Enabling Gzip Compression for HTML, CSS, and JavaScript Files

By default, compression is disabled in NGINX but depending on your installation or Linux distribution, some settings might be enabled in the default nginx.conf file. Here we enable gzip compression in the NGINX configuration file:

```
gzip on;
gzip_types application/xml application/json text/css text/javascript application/javascript;
gzip_vary on;
gzip_comp_level 6;
gzip_min_length 500;
```

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```

#### 如果设置 HTTP 跳转到 HTTPS？

只需在网站对应的 server{} 配置段中增加规则即可：
```
 if ($scheme != "https") 
    {
    return 301 https://$host$request_uri;
    }
```
#### LNMP 默认安装了哪些 Nginx模块？ 

运行命令 `nginx -V` 查看

#### LNMP 默认安装了哪些 PHP 模块？

运行命令 `php -m` 查看

#### 如何启用或禁用 Nginx 模块？

不支持模块启用或关闭

#### 如何禁用IP访问网站，防止恶意解析？

参考 [Nginx 相关配置文档](https://support.websoft9.com/docs/linux/zh/webs-nginx.html#禁用ip访问-防止恶意解析)

#### 没有域名是否可以通过 http://公网IP/mysite1 这样的方式访问网站？

可以。具体配置方法参考 [安装网站](/zh/solution-deployment.md#安装第二个网站)

#### 部署和安装有什么区别？

部署是将一序列软件按照不同顺序，先后安装并配置到服务器的过程，是一个复杂的系统工程。  
安装是将单一的软件拷贝到服务器之后，启动安装向导完成初始化配置的过程。  
安装相对于部署来说更简单一些。 

#### 云平台是什么意思？

云平台指提供云计算服务的平台厂家，例如：Azure,AWS,阿里云,华为云,腾讯云等

#### 实例，云服务器，虚拟机，ECS，EC2，CVM，VM有什么区别？

没有区别，只是不同厂家所采用的专业术语，实际上都是云服务器
