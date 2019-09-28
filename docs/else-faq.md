# FAQ

#### What's different between LEMP and LEMP?
LEMP is LEMP, just different names used by different people

#### What is the default character set?
UTF-8

#### What is the Nginx vhost configuration file?
The Nginx vhost configuration file is the function for Nginx to manage multiple applications. It's path is: */etc/nginx/conf.d/default.conf*.
There have `server{ }` , each segment is corresponding to a application

#### How to modify the path of example application?

Example application's path is: */data/wwwroot/www.example.com*, you can modify it by [Nginx vhost configuration file](/stack-components.md#nginx)

#### Does the LEMP support deploying multiple applications?

Yes, add new application, you should add new VirtualHost segment in the file [Nginx vhost configuration file](/stack-components.md#nginx) for it

#### Can I use this LEMP if I don't understand the Linux command?
Yes, you can use GUI tool WinSCP to start LAMP, no commands

#### If there is no domain name, can I deploy LEMP?

Yes, visit LEMP by *http://Internet IP*

#### What is the password for the database root user?

The password is stored in the server related file: `/credentials/password.txt`

#### Is there a web-base GUI database management tools?

Yes, phpMyAdmin is on it, visit by *http://Internet IP/phpmyadmin*

#### How to disable phpMyAdmin access?

Edit the  [phpMyAdmin configuration file](/stack-components.md#phpmyadmin), replace `Require all granted` with `Require ip 192.160.1.0`, then restart Nginx service

#### Is it possible to modify the code source path?

Yes, modify it by [Nginx vhost configuration file](/stack-components.md#nginx)

#### How to delete 9Panel?

Please delete all files in 9Panel */data/apps/9panel* and keep an empty 9Panel folder

#### Do I need to change the owner(group) for the files which I upload by SFTP?

No, you don't need to change them because LEMP Image have change it automaticly

#### How can I reset my php.ini to return to the initial?
Download the [php.ini](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) from Websoft9 LEMP project on Github, upload to Server and cover /ect/php.ini

#### Do I need to change the owner(group) for the files which I upload by SFTP?
No, you don't need to change them because LEMP Image have change it automaticly

#### How to bind a domain name for your application?
Modify the **server_name** configuration item of VirtualHost template in the file `default.conf`

#### How can I install JAVA on LEMP?
Just run the command below, JAVA and Tomcat will be installed on your Cloud Server
```shell
yum install tomcat-* -y && systemctl enable tomcat && systemctl start tomcat
```

#### How to change the permissions of filesytem?

Change owner(group) or permissions like below:

```shell
chown -R nginx.nginx /data/wwwroot
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```

#### How to set HTTP redirect to HTTPS automatically?

Insert these Rewrite rules in the file *server{ }* segment of [Nginx vhost configuration file](/stack-components.md#nginx)
```
 if ($scheme != "https") 
    {
    return 301 https://$host$request_uri;
    }
```
#### How to set Rewrite rules for your application?
LEMP Image has installed Nginx rewrite module and there some preset rewrite rules in the directory: */etc/nginx/conf.d/rewrite*. You just need to modify the xxx.conf file in the rewrite directory, if there not a configuration file for your application, refer to the [Set the Rewrite Rules](/solution-more.md#use-rewrite)

#### Which Nginx modules are installed by default by LEMP?

Use command `nginx -V` to list all modules

#### Which PHP modules are installed by default by LEMP?

Use command `php -m` to list all modules

#### How to enable or disable Nginx module?

No

#### How to disable IP access my application?

Refer to the docs [Nginx configuration](https://support.websoft9.com/docs/linux/webs-nginx.html#disable-ip-access)

#### Is there a domain name that can be accessed via http://public IP/mysite1?

Yes, refer to the docs [Deploy a PHP application](/lamp/solution-deployment.html#deploy-second-application)

#### What's the difference between Deployment and Installation?

- Deployment is a process of installing and configuring a sequence of software in sequence in a different order, which is a complex system engineering.  
- Installation is the process of starting the initial wizard after the application is prepared.  
- Installation is simpler than deployment. 

#### What's Cloud Platform?

Cloud platform refers to platform manufacturers that provide cloud computing services, such as: **Azure, AWS, Alibaba Cloud, HUAWEI CLOUD, Tencent Cloud**, etc.

#### What is the difference between Instance, Cloud Server, Virtual Machine, ECS, EC2, CVM, and VM?

No difference, just the terminology used by different manufacturers, actually cloud servers