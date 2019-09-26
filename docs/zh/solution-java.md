# 扩展Java（双能）

熟悉 LNMP 之后，部分读者朋友可能会考虑，能否在 LNMP 的基础上运行 Java 程序呢？经过实践的研究，我们发现只要在 LNMP 基础上再安装 Tomcat 和 JDK，便可以让 LNMP 同时支持 PHP 和 Java 程序

## 安装 Java

如果你使用的是 **PHP&Java 运行环境**，那么意味着你的环境已经支持 Java，无需再安装 Java。  

否则，请通过下面一条命令，安装Java以及Tomcat  

```
yum install tomcat-* -y && systemctl enable tomcat && systemctl start tomcat
```

安装成功之后，本地浏览器访问 *http://服务器公网IP:8080/sample/* 即可显示 Java 示例页面

> 需提前开启安全组8080端口，方可以访问

## 路径参数

Java 安装到服务器之后，主要路径信息如下：

### Java
Java Edition：*OpenJDK*  
JVM Directory：	*/usr/lib/jvm*

### Tomcat
Tomcat 配置文件： */etc/tomcat/server.xml*    
Tomcat 安装目录： */usr/share/java*     
Tomcat 网站目录： */var/lib/tomcat/webapps*    
Tomcat 日志目录： */var/log/tomcat*  
Tomcat 欢迎页面： *http://Internet IP:8080* and *http://Internet IP:8080/examples/*

## 部署 Java 应用程序

部署Java网站分为两种场景，请根据您的实际情况选择对应的方案：

### 安装第一个Java应用

1. 上传程序包到 `/data/wwwroot/default`目录下，且修改所属用户和组`chown www: -R /data/wwwroot`

2. 修改 Tomcat 配置文件`etc/tomcat/server.xml`，参考下图
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/java/lnmp-modifytomcat001-websoft9.png)



3. 修改 Nginx 配置文件`/etc/nginx/conf.d/default.conf`，参考下图
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/java/lnmp-modifynginx001-websoft9.jpg)

4. 重启服务
   ```
   systemctl restart tomcat
   systemctl restart nginx
   ```
5. 访问网址或者服务器IP测试网站


### 安装第二个Java应用

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)
2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)
3. 编辑 Nginx 配置文件 *default.conf* 文件    
   将下面 **server{ } 模板**插入到 default.conf 中，并修改其中的 server_name, root, error_log, access_log
 
       ```
       server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.jsp index.do index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        
        #include php.conf;
        include jsp.conf;
        }
        ```
4. 编辑 Tomcat 配置文件 *server.xml* 文件   
   将下面 `<Host></Host>` 模板插入到 server.xml 中，并修改其中的 name, appBase, docBase, prefix
    ```
    <Host name="mysite2.yourdomain.com" appBase="/data/wwwroot" unpackWARs="true" autoDeploy="true">
    <Context path="" docBase="/data/wwwroot/mysite2" reloadable="false" crossContext="true"/>
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" prefix="mysite2.yourdomain.com_access_log" suffix=".txt" pattern="%h %l %u %t &quot;%r&quot; %s %b" />
    <Valve className="org.apache.catalina.valves.RemoteIpValve" remoteIpHeader="X-Forwarded-For" protocolHeader="X-Forwarded-Proto" protocolHeaderHttpsValue="https"/>
    </Host>
    ```

4. 保存 *default.conf*，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启Nginx服务命令
      sudo systemctl restart nginx
      ~~~
5. 根据有无域名，本地浏览器访问：http://mysite1.yourdomain.com/mysite2  访问你的网站。

6. 访问网址或者服务器IP测试网站

## Host 配置说明

针对 Tomcat 下的 server.xml 文件中的 host 配置段，需要修改的参数说明如下：  

`name` : 域名配置  
`appBase` : 程序路径,这个路径下的war包会自动解压  
`path` : 访问路径,根据需求修改(一般默认即可)  
`docBase` : 程序路径。如果是war包，需带上后缀名，例如:`/data/wwwroot/default/mysite.war`