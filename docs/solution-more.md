# More

Each of the following solutions has been proven to be effective and we hope to be helpful to you.

## Domain binding

The precondition for binding a domain is that LEMP can accessed by domain name.

Nonetheless, from the perspective of server security and subsequent maintenance considerations, the **Domain Binding** step cannot be omitted.

LEMP domain name binding steps:

1. Connect your Cloud Server
2. Modify [Nginx vhost configuration file](/stack-components.md#nginx), change the **server_name**'s value to your domain name
   ```text
   server
   {
   listen 80;
   server_name www.example.com;  # 此处修改为你的域名
   index index.html index.htm index.php;
   root  /data/wwwroot/www.example.com;
   ...
   }
   ```
3. Save it and restart [Nginx Service](/admin-services.md#nginx)


## Use Rewrite

Rewrite was enabled by default on LEMP, three steps to use rewrite for your application:

1.  Add a new rewirte rules configuration file(e.g. wordpress.conf) to the directory:  */etc/nginx/conf.d/rewrite* on your Server
2.  Edit the **server{ }** segment of your [Nginx vhost configuration file](/stack-components.md#nginx), include your rewirte rules configuration file
   ```text
   server
   {
   listen 80;
   server_name mysite2.yourdomain.com;  # modify it to your domain
   index index.html index.htm index.php;
   root  /data/wwwroot/mysite2;
   ...

   ## Includes one of your Rewrite rules if you need, examples
   include conf.d/rewrite/wordpress.conf;  # inculde your rewrite rules here
   }
   ```
3. Save it, then [Restart Nginx service](/admin-services.md#nginx)

## Rest MySQL *root* password

1. Connect to your Cloud Server by SSH
2. Run the below command
   ```
   sudo git clone https://github.com/Websoft9/linux.git; cd linux/Mysql_ResetPasswd_Script;sudo sh reset_mysql_password.sh
   ```

## Modify the php.ini

When you want to modify The PHP File Upload Limit, Max Execution Time, Memory Limit...for example:

1. Use SFTP to modify the */etc/php.ini* 
```
# File upload limit
post_max_size = 16M
upload_max_filesize = 16M

# Max Execution Time
max_execution_time = 90

# Memory Limit
memory_limit – Minimum: 256M
```
2. Save it and restart [Nginx Service](/admin-services.md#nginx)

## PHP Version Upgrade

Refert to the docs *[PHP version upgrade](https://support.websoft9.com/docs/linux/zh/lang-php.html#verion-upgrade)*

## PHP Install Module

Refert to the docs *[PHP Modules installation](https://support.websoft9.com/docs/linux/lang-php.html#install-module)*