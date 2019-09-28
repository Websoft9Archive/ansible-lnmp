# 安装网站

在 LNMP 环境上安装一个网站，也就是我们常说的增加一个虚拟主机。

全局上看，只需两个步骤：**上传网站代码** + [**虚拟机主机配置文件**](/zh/stack-components.md#nginx) **中增加 server{} 配置段**

> server{} 又称之为虚拟主机配置段，每个网站必定在 default.conf 中对应唯一的 server{}。

## 准备

安装网站之前，请了解如下几个要点，做好准备工作

*  虚拟机主机配置文件：*/etc/nginx/conf.d/default.conf* 
*  连接工具：使用 WinSCP 连接服务器，它包含文件管理、运行命令两方面功能
*  域名：若需要使用域名，请确保备案后的域名成功解析到服务器IP
*  数据库：网站安装向导过程中可能需要使用数据库，请使用 [phpMyAdmin 管理数据库](/zh/admin-mysql.md)

有一个全局认知并完成准备工作之后，我们开始部署网站

## 安装第一个网站

下面通过**替换示例网站**（LNMP 默认存在一个示例网站）的方式来教你安装你的第一个网站：

1. 使用 WinSCP 连接服务器
2. 删除示例网站 */data/wwwroot/www.example.com* 下的所有文件（保留目录）
3. 将本地电脑上的网站源码上传到示例目录下
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-uploadcodestoexample-websoft9.png)
4. 修改 *default.conf* 中已有 server{} 配置段（[修改参考](/zh/solution-deployment.md#server)），实现绑定域名、修改网站目录名称等操作。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-editvhostconf-websoft9.png)
   ::: warning
   如果不绑定域名、不修改网站目录名称，请跳过步骤4和5
   :::
5. 保存 default.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启 Nginx 服务命令
      sudo systemctl restart nginx
      ~~~
6. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 即可访问您的网站

## 安装第二个网站

从安装第二个网站开始，需要在 *default.conf* 中增加对应的虚拟主机配置段，具体如下

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)
2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)
3. 编辑 *default.conf* 文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-editvhostconf-websoft9.png)

    根据是否通过域名访问，选择下面操作之一：

     * **有域名，通过 http://域名 访问网站**
     
     请将下面 server 模板拷贝到 default.conf 中，并修改其中的 server_name, root, error_log, access_log等项的值
 
       ```
       server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        include conf.d/extra/*.conf;

        ## Includes one of your Rewrite rules if you need, examples
        # include conf.d/rewrite/wordpress.conf;
        # include conf.d/rewrite/joomla.conf;
        }
        ```

     * **没有域名，通过 http://mysite1.yourdomain.com/mysite2 访问网站**  
    
     请将下面 Alias 模板插入到 default.conf 中已存在的 server{} 段中，并修改其中的 location,alias 

      ```
      location /mysite2
      {
       alias /data/wwwroot/mysite2;
       index index.php index.html;
       location ~ ^/mysite2/.+\.php$ {
        alias /data/wwwroot/mysite2;
        fastcgi_pass  unix:/dev/shm/php-fpm-default.sock;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME /data/wwwroot/$fastcgi_script_name;
        include        fastcgi_params; }
      include conf.d/extra/*.conf;
      }
      ```
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-insertalias-websoft9.png)

      注意：Alias 模板只能插入到 server{} 配置段中

4. 保存 *default.conf*，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启Nginx服务命令
      sudo systemctl restart nginx
      ~~~
5. 如果配置了域名，通过：*http://域名* 访问你的网站。
6. 如果没有配置域名，通过：*http://mysite1.yourdomain.com/mysite2* 访问你的网站


## 安装第 N 个网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 LNMP 安装网站步骤： 

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导 

## Server

server{ } 改动务必准确无误，任何错误的修改都会导致服务器上所有的网站不可访问

|  server 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  server_name  |  域名，如果配置两个域名需以空格分开   |  必须填写 |
|  root |  网站存放目录  | 务必准确无误 |
|  error_log  | 错误日志路径，系统会根据定义的路径产生相关日志文件   |  可以不填或删除 |
|  access_log  | 访问日志路径，系统会根据定义的路径产生相关日志文件  |  可以不填或删除 |
|  ssl_certificate  | HTTPS 证书路径  |  设置 HTTPS 访问时必填 |
|  ssl_certificate_key  | HTTPS 证书秘钥路径   |  设置 HTTPS 访问时必填 |

## 常见问题

#### 访问刚安装的网站，页面显示 “没有权限...” ？

运行一条修改文件权限的命令
~~~
chown -R nginx.nginx /data/wwwroot
~~~

#### 修改 default.conf 文件之后，Nginx 服务无法启动？

一般是 server{ } 中虚拟主机的目录位置不正确导致

#### 新增网站不可访问，且导致其他网站都不可访问？

一般是 server{ } 中虚拟主机的目录位置不正确导致 Nginx 无法启动

#### 打开新增的网站，显示404错误？

一般是网站目录下没有 index.php 或 index.html 等默认首页导致

#### 新增的网站，显示 500 Internal Server Error？

程序代码错误，需要查看程序的日志文件